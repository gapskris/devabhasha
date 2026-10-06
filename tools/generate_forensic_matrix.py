import os
import sys
import json
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

master_dir = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_master"
modern_dir = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern"

# Load modern data
with open(os.path.join(modern_dir, "content", "data.json"), "r", encoding="utf-8") as f:
    modern_data = json.load(f)

# Chapters mapping
chapters_meta = [
    (1, "chapter1.dxr", "chap1page"),
    (2, "chapter2.dxr", "page"),
    (3, "chap03.dxr", None),
    (4, "chap04.dxr", None),
    (5, "chapter5.dxr", "chap5page"),
    (6, "chapter6.dxr", "chapter6page"),
    (7, "chapter7.dxr", "chap7page"),
    (8, "chap08.dxr", None),
    (9, "chapter9.dxr", None),
    (10, "chapter10.dxr", None),
]

print("=" * 80)
print("EXTENSIVE CHAPTER & PAGE FORENSIC COMPARISON: ORIGINAL VS MODERN")
print("=" * 80)

for cid, dxr_name, img_prefix in chapters_meta:
    dxr_path = os.path.join(master_dir, dxr_name)
    m_ch = next((c for c in modern_data["chapters"] if c["id"] == cid), None)
    
    # 1. Director file analysis
    director_pages = []
    if os.path.exists(dxr_path):
        with open(dxr_path, "rb") as f:
            raw = f.read()
        # Find "Page X of Y"
        p_matches = re.findall(rb'Page\s+(\d+)\s+of\s+(\d+)', raw)
        if p_matches:
            total_orig_pages = int(p_matches[0][1])
            director_pages = list(range(1, total_orig_pages + 1))
        elif cid == 2:
            # Chapter 2 uses markers page01 to page23
            total_orig_pages = 23
            director_pages = list(range(1, 24))
        else:
            total_orig_pages = 0
    else:
        total_orig_pages = 0

    # 2. Modern slides analysis
    m_slides = m_ch.get("slides", []) if m_ch else []
    m_tracks = m_ch.get("audioTracks", []) if m_ch else []
    m_sections = m_ch.get("contentSections", []) if m_ch else []

    print(f"\n--- CHAPTER {cid}: {dxr_name} ---")
    print(f"Original 1997 Director Pages: {total_orig_pages}")
    print(f"Modern Web Slides Count:      {len(m_slides)}")
    print(f"Original Audio WAVs in Master: {len([f for f in os.listdir(os.path.join(master_dir, 'media')) if f.lower().startswith(f'chapter{cid}') or f.lower().startswith(f'c{cid}') or (cid==1 and 'kalidasa' in f.lower()) or (cid==2 and ('varga' in f.lower() or 'alpha' in f.lower() or 'sandhi' in f.lower() or 'ishat' in f.lower() or 'ushman' in f.lower() or 'gita' in f.lower() or 's1' in f.lower() or 's2' in f.lower() or 's3' in f.lower() or 'h.' in f.lower()))])}")
    print(f"Modern Audio Tracks Mapped:   {len(m_tracks)}")
    print(f"Modern Content Sections:      {len(m_sections)}")

    # Check images used in modern slides
    slide_canvases = [s.get("canvas") for s in m_slides]
    print(f"Modern Slide Canvases ({len(slide_canvases)}): {slide_canvases[:4]}...")

    # Gaps summary
    gaps = []
    if total_orig_pages != len(m_slides):
        gaps.append(f"Page Count Discrepancy: Original has {total_orig_pages} pages, Modern has {len(m_slides)} slides (Delta: {len(m_slides) - total_orig_pages})")
    
    # Check if slides have duplicate canvases
    unique_canvases = set(slide_canvases)
    if len(unique_canvases) < len(slide_canvases) and len(slide_canvases) > 1:
        gaps.append(f"Canvas Duplication: {len(slide_canvases)} slides reuse only {len(unique_canvases)} unique canvas files!")

    # Check if tracks have arbitrary slideIndex formula
    slide_indices = [t.get("slideIndex") for t in m_tracks]
    if len(slide_indices) > 0 and len(set(slide_indices)) <= len(m_slides):
        # check distribution
        counts_per_slide = {}
        for si in slide_indices:
            counts_per_slide[si] = counts_per_slide.get(si, 0) + 1
        gaps.append(f"Track-to-Slide Distribution: {counts_per_slide}")

    print("Gaps Identified:")
    for g in gaps:
        print(f"  - {g}")
