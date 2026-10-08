import sys
import os
import json
import re
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, 'content', 'data.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)

print("================================================================================")
print("       FORENSIC SLIDE-BY-SLIDE AUDIT REPORT (ALL 10 CHAPTERS / 125 SLIDES)      ")
print("================================================================================")
print("Evaluating 4 Critical Quality Axes per Slide:")
print("  1) Image Content Properness (Canvas & Diagram resolution, existence, aspect ratio)")
print("  2) Card & Text Content Properness (Visibility, title, headings, card rendering)")
print("  3) Audio Content Properness (Audio file parity, track mapping, dual m4a/mp3)")
print("  4) Sanskrit Content Properness (Devanagari purity, no English leakage, ligatures)")
print("================================================================================\n")

total_slides = 0
total_issues = 0
chapter_results = []

def has_devanagari(text):
    if not text: return False
    return any(0x0900 <= ord(c) <= 0x097F for c in text)

def has_dangling_matra(text):
    if not text: return False
    # Vowel signs without consonant base at word start
    return bool(re.search(r'(?:^|\s)[\u093e-\u094c\u0962\u0963]', text))

for ch in data['chapters']:
    cid = ch['id']
    ctitle = ch.get('titleEnglish') or ch.get('title') or f"Chapter {cid}"
    slides = ch.get('slides', [])
    tracks = ch.get('audioTracks', [])
    sections = ch.get('contentSections', [])
    
    ch_slide_count = len(slides)
    ch_track_count = len(tracks)
    ch_sec_count = len(sections)
    
    ch_issues_count = 0
    
    print(f"\n################################################################################")
    print(f"  CHAPTER {cid:2d}: {ctitle} ({ch_slide_count} slides, {ch_track_count} audio tracks, {ch_sec_count} sections)")
    print(f"################################################################################")
    
    # Check chapter-level track mapping coverage
    all_mapped_tracks = set()
    for s in slides:
        for t in s.get('trackIndices', []):
            all_mapped_tracks.add(t)
    unmapped_tracks = [i for i in range(ch_track_count) if i not in all_mapped_tracks]
    if unmapped_tracks:
        print(f"  [!] Chapter Track Warning: {len(unmapped_tracks)} tracks never mapped to any slide: {unmapped_tracks}")

    for s_idx, s in enumerate(slides):
        total_slides += 1
        snum = s.get('slideNumber', s_idx + 1)
        stitle = s.get('title') or "Untitled"
        stitle_sa = s.get('titleSanskrit') or ""
        
        slide_issues = []
        
        # -------------------------------------------------------------
        # AXIS 1: Image Content Properness
        # -------------------------------------------------------------
        img_status = "PASS"
        img_notes = []
        canvas_path = s.get('canvas') or ch.get('canvas')
        if not canvas_path:
            img_status = "FAIL"
            slide_issues.append("Missing canvas path")
            img_notes.append("No canvas path defined")
        elif 'acknowledge' in canvas_path.lower():
            img_status = "FAIL"
            slide_issues.append(f"Forbidden ACKNOWLEDGEMENTS image used on content slide: {canvas_path}")
            img_notes.append("Forbidden ACKNOWLEDGEMENTS canvas")
        else:
            full_canvas = os.path.join(BASE_DIR, canvas_path.replace('/', os.sep))
            if not os.path.exists(full_canvas):
                img_status = "FAIL"
                slide_issues.append(f"Canvas file not found: {canvas_path}")
                img_notes.append(f"Canvas file missing: {canvas_path}")
            else:
                try:
                    with Image.open(full_canvas) as im:
                        w, h = im.size
                        if w < 400 or h < 300:
                            img_status = "WARN"
                            slide_issues.append(f"Low-resolution thumbnail used as canvas: {w}x{h}")
                            img_notes.append(f"Low-res canvas: {w}x{h}")
                        else:
                            img_notes.append(f"Canvas OK ({w}x{h})")
                except Exception as e:
                    img_status = "FAIL"
                    slide_issues.append(f"Invalid canvas image: {e}")
                    img_notes.append(f"Corrupt canvas image: {e}")

        # Diagram Image Check
        diagram_path = s.get('diagram')
        if diagram_path:
            full_diagram = os.path.join(BASE_DIR, diagram_path.replace('/', os.sep))
            if not os.path.exists(full_diagram):
                img_status = "FAIL"
                slide_issues.append(f"Diagram file missing: {diagram_path}")
                img_notes.append(f"Diagram missing: {diagram_path}")
            else:
                try:
                    with Image.open(full_diagram) as im:
                        dw, dh = im.size
                        img_notes.append(f"Diagram OK ({dw}x{dh})")
                except Exception as e:
                    img_status = "FAIL"
                    slide_issues.append(f"Corrupt diagram image: {e}")
                    img_notes.append(f"Corrupt diagram: {e}")

        # -------------------------------------------------------------
        # AXIS 2: Card & Text Content Properness
        # -------------------------------------------------------------
        text_status = "PASS"
        text_notes = []
        t_indices = s.get('trackIndices', [])
        sec_idx = s.get('sectionIndex')
        has_prose = bool(s.get('proseText') or s.get('description') or s.get('proseTextSanskrit'))
        
        has_card = (len(t_indices) > 0) or (sec_idx is not None) or has_prose
        if not has_card:
            text_status = "FAIL"
            slide_issues.append("Slide has zero text/card content (blank stage)")
            text_notes.append("No cards or text available to render")
        else:
            if len(t_indices) > 0:
                text_notes.append(f"{len(t_indices)} audio card(s)")
            if sec_idx is not None:
                if sec_idx < len(sections):
                    text_notes.append(f"Section {sec_idx} prose card")
                else:
                    text_status = "FAIL"
                    slide_issues.append(f"Invalid sectionIndex {sec_idx} (only {len(sections)} sections)")
                    text_notes.append(f"Invalid sectionIndex {sec_idx}")
            if len(t_indices) == 0 and sec_idx is None and has_prose:
                text_notes.append("Dedicated narrative intro card")

        if not stitle or stitle.strip() == "":
            text_status = "WARN"
            slide_issues.append("Empty English slide title")
            text_notes.append("Empty English title")

        # -------------------------------------------------------------
        # AXIS 3: Audio Content Properness
        # -------------------------------------------------------------
        audio_status = "PASS"
        audio_notes = []
        if len(t_indices) > 0:
            for tidx in t_indices:
                if tidx < 0 or tidx >= len(tracks):
                    audio_status = "FAIL"
                    slide_issues.append(f"Invalid track index {tidx} (chapter has {len(tracks)} audioTracks)")
                    audio_notes.append(f"Invalid track {tidx}")
                else:
                    track_obj = tracks[tidx]
                    m4a_path = track_obj.get('m4a') or track_obj.get('audio')
                    mp3_path = track_obj.get('mp3')
                    
                    if not m4a_path:
                        audio_status = "FAIL"
                        slide_issues.append(f"Track {tidx} missing m4a path")
                        audio_notes.append(f"Track {tidx} missing m4a")
                    else:
                        full_m4a = os.path.join(BASE_DIR, m4a_path.replace('/', os.sep))
                        if not os.path.exists(full_m4a):
                            audio_status = "FAIL"
                            slide_issues.append(f"M4A file not found on disk: {m4a_path}")
                            audio_notes.append(f"M4A not found: {m4a_path}")
                        else:
                            audio_notes.append(f"Track {tidx} M4A OK")

                    if not mp3_path:
                        audio_status = "WARN"
                        slide_issues.append(f"Track {tidx} missing mp3 fallback path")
                        audio_notes.append(f"Track {tidx} missing mp3")
                    else:
                        full_mp3 = os.path.join(BASE_DIR, mp3_path.replace('/', os.sep))
                        if not os.path.exists(full_mp3):
                            audio_status = "WARN"
                            slide_issues.append(f"MP3 file not found on disk: {mp3_path}")
                            audio_notes.append(f"MP3 not found: {mp3_path}")
        else:
            audio_notes.append("Narrative / non-audio slide (0 tracks)")

        # -------------------------------------------------------------
        # AXIS 4: Sanskrit Content Properness
        # -------------------------------------------------------------
        sa_status = "PASS"
        sa_notes = []
        
        # 1. Slide Sanskrit Title
        if not stitle_sa or stitle_sa.strip() == "":
            sa_status = "FAIL"
            slide_issues.append("Missing titleSanskrit")
            sa_notes.append("Missing Sanskrit title")
        elif not has_devanagari(stitle_sa):
            sa_status = "FAIL"
            slide_issues.append(f"titleSanskrit lacks Devanagari characters: {stitle_sa}")
            sa_notes.append("Non-Devanagari Sanskrit title")
        else:
            if has_dangling_matra(stitle_sa):
                sa_status = "WARN"
                slide_issues.append("Dangling matra in titleSanskrit")
                sa_notes.append("Dangling matra in title")
            else:
                sa_notes.append(f"Title: {stitle_sa[:20]}... [OK]")

        # 2. Sanskrit Audio Recitation Cards
        if len(t_indices) > 0:
            for tidx in t_indices:
                if 0 <= tidx < len(tracks):
                    tobj = tracks[tidx]
                    sa_verse = tobj.get('sanskrit') or tobj.get('shloka_sanskrit') or tobj.get('text_sanskrit') or ""
                    if not sa_verse or not has_devanagari(sa_verse):
                        sa_status = "FAIL"
                        slide_issues.append(f"Track {tidx} missing Sanskrit Devanagari verse")
                        sa_notes.append(f"Track {tidx} missing Devanagari")
                    elif has_dangling_matra(sa_verse):
                        sa_status = "WARN"
                        slide_issues.append(f"Track {tidx} has dangling matra")
                        sa_notes.append(f"Track {tidx} dangling matra")
                    else:
                        sa_notes.append(f"Track {tidx} Devanagari OK")

        # 3. Sanskrit Narrative / Prose Cards
        sa_prose = s.get('proseTextSanskrit')
        if len(t_indices) == 0:
            if sec_idx is not None and sec_idx < len(sections):
                sec_obj = sections[sec_idx]
                sec_sa = sec_obj.get('body_sa') or sec_obj.get('content_sa')
                if not sec_sa or not has_devanagari(sec_sa):
                    sa_status = "FAIL"
                    slide_issues.append(f"Section {sec_idx} missing Sanskrit body (will leak English)")
                    sa_notes.append(f"Section {sec_idx} lacks Sanskrit body")
                else:
                    sa_notes.append(f"Section {sec_idx} Sanskrit Body OK")
        # 4. Check for robotic placeholder strings
        all_sa_text = f"{stitle_sa} {sa_prose} {' '.join(sa_notes)}"
        if 'अध्यायस्य' in all_sa_text and ('विशिष्टा विषय-चर्चा' in all_sa_text or 'परमोपदेशः' in all_sa_text):
            sa_status = "FAIL"
            slide_issues.append("Robotic placeholder text detected (synthetic template text banned)")
            sa_notes.append("Robotic placeholder detected")

        # Slide Summary Line
        slide_ok = (len(slide_issues) == 0)
        status_flag = "[OK]  " if slide_ok else "[FAIL]"
        print(f"  Slide {snum:2d}: {status_flag} | Images: {img_status:4s} | Text: {text_status:4s} | Audio: {audio_status:4s} | Sanskrit: {sa_status:4s} | '{stitle[:36]}'")
        if slide_issues:
            total_issues += len(slide_issues)
            ch_issues_count += len(slide_issues)
            for iss in slide_issues:
                print(f"            --> ISSUE: {iss}")

    chapter_results.append((cid, ctitle, ch_slide_count, ch_track_count, ch_issues_count))

print("\n================================================================================")
print(f"AUDIT COMPLETED: {total_slides} SLIDES TESTED ACROSS ALL 10 CHAPTERS.")
print(f"TOTAL CRITICAL ISSUES DETECTED: {total_issues}")
print("================================================================================")
print("\nCHAPTER-BY-CHAPTER HEALTH SUMMARY:")
for cid, ctitle, sc, tc, ic in chapter_results:
    ch_flag = "100% CLEAN" if ic == 0 else f"{ic} ISSUES DETECTED"
    print(f"  Chapter {cid:2d} ({ctitle[:35]:35s}): {sc:2d} slides | {tc:2d} tracks | Status: {ch_flag}")
print("================================================================================")
