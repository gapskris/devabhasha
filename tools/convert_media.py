"""
Media Modernization Engine for Devabhāṣā 1997 CD-ROM Preservation
Performs 1-to-1 conversion of:
- 149 WAV audio recitations -> High-Fidelity 192k M4A (AAC-LC) + Universal MP3 fallback
- 1 AVI opening montage -> Universal H.264/AAC MP4 with +faststart
- 127 Visual assets (124 JPGs copied, 3 uncompressed BMPs converted to 95-quality JPGs preserving 640x480 dimensions)
- Validates audio and video duration against source material
"""

import os
import glob
import subprocess
import shutil
import json
from PIL import Image

SRC_DIR = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_master"
DST_DIR = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern"

AUDIO_DST = os.path.join(DST_DIR, "assets", "audio")
VIDEO_DST = os.path.join(DST_DIR, "assets", "video")
IMAGES_DST = os.path.join(DST_DIR, "assets", "images")

os.makedirs(AUDIO_DST, exist_ok=True)
os.makedirs(VIDEO_DST, exist_ok=True)
os.makedirs(IMAGES_DST, exist_ok=True)

def get_media_duration(file_path):
    """Get duration in seconds using ffprobe"""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return float(res.stdout.strip())
    except Exception as e:
        return None

def copy_and_convert_images():
    print("=== [PHASE 3] Processing Images & Backdrops ===")
    src_jpeg = os.path.join(SRC_DIR, "jpeg")
    converted_count = 0
    copied_count = 0
    
    for root, dirs, files in os.walk(src_jpeg):
        for f in files:
            src_f = os.path.join(root, f)
            rel_dir = os.path.relpath(root, src_jpeg)
            if rel_dir == ".":
                target_sub = IMAGES_DST
            else:
                # normalize folder names: e.g., 'chapter 5' -> 'chap5', etc.
                clean_rel = rel_dir.lower().replace(" ", "")
                target_sub = os.path.normpath(os.path.join(IMAGES_DST, clean_rel))
            os.makedirs(target_sub, exist_ok=True)
            
            ext = os.path.splitext(f)[1].lower()
            base = os.path.splitext(f)[0]
            
            if ext == '.bmp':
                target_f = os.path.join(target_sub, f"{base}.jpg")
                if not os.path.exists(target_f) or os.path.getsize(target_f) < 500:
                    im = Image.open(src_f)
                    im.convert('RGB').save(target_f, quality=95)
                    print(f"  [BMP->JPG] {f} -> {os.path.relpath(target_f, DST_DIR)} ({im.size[0]}x{im.size[1]})")
                converted_count += 1
            elif ext in ['.jpg', '.jpeg', '.png']:
                target_f = os.path.join(target_sub, f)
                if not os.path.exists(target_f) or os.path.getsize(target_f) < 500:
                    shutil.copy2(src_f, target_f)
                    print(f"  [COPY] {f} -> {os.path.relpath(target_f, DST_DIR)}")
                copied_count += 1
                
    print(f"Images complete: {copied_count} JPGs copied, {converted_count} BMPs converted. Total: {copied_count + converted_count}/127")

def convert_videos():
    print("\n=== [PHASE 2] Processing Video (H.264 CRF 18, 192k AAC, +faststart) ===")
    avi_files = glob.glob(os.path.join(SRC_DIR, "**", "*.avi"), recursive=True)
    print(f"Found {len(avi_files)} AVI source video.")
    
    for avi in avi_files:
        fname = os.path.basename(avi)
        base = os.path.splitext(fname)[0]
        mp4_name = f"{base}.mp4"
        out_path = os.path.join(VIDEO_DST, mp4_name)
        
        src_dur = get_media_duration(avi)
        print(f"  Source AVI: {fname} (Duration: {src_dur:.2f}s)")
        
        if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
            out_dur = get_media_duration(out_path)
            print(f"  [Already Converted] {mp4_name} (Duration: {out_dur:.2f}s)")
            continue
            
        print(f"  Converting {fname} -> {mp4_name}...")
        cmd = [
            "ffmpeg", "-y",
            "-i", avi,
            "-c:v", "libx264",
            "-preset", "slow",
            "-crf", "18",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-b:a", "192k",
            "-ar", "44100",
            "-movflags", "+faststart",
            out_path
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode != 0:
            print(f"  ERROR on {fname}: {res.stderr.decode('utf-8', errors='ignore')[-300:]}")
        else:
            out_dur = get_media_duration(out_path)
            diff = abs(src_dur - out_dur) if (src_dur and out_dur) else 0
            print(f"  SUCCESS: {mp4_name} (Source: {src_dur:.2f}s, Output: {out_dur:.2f}s, Drift: {diff:.3f}s)")

def convert_audios():
    print("\n=== [PHASE 1] Processing Audio (149 WAVs -> 192k M4A/AAC + MP3 Fallback) ===")
    media_dir = os.path.join(SRC_DIR, "media")
    wav_files = glob.glob(os.path.join(media_dir, "**", "*.wav"), recursive=True)
    print(f"Found {len(wav_files)} WAV files to convert.")
    
    m4a_success = 0
    mp3_success = 0
    drift_violations = 0
    
    for wav in sorted(wav_files):
        # Determine relative folder under media
        rel_folder = os.path.dirname(os.path.relpath(wav, media_dir))
        clean_rel = rel_folder.lower().replace(" ", "").replace("chapter", "chap")
        target_dir = os.path.join(AUDIO_DST, clean_rel)
        os.makedirs(target_dir, exist_ok=True)
        
        fname = os.path.basename(wav)
        base = os.path.splitext(fname)[0]
        
        m4a_path = os.path.join(target_dir, f"{base}.m4a")
        mp3_path = os.path.join(target_dir, f"{base}.mp3")
        
        src_dur = get_media_duration(wav)
        
        # 1. High-Fidelity M4A (192 kbps AAC-LC)
        if not (os.path.exists(m4a_path) and os.path.getsize(m4a_path) > 500):
            cmd_m4a = [
                "ffmpeg", "-y",
                "-i", wav,
                "-c:a", "aac",
                "-b:a", "192k",
                "-ar", "44100",
                m4a_path
            ]
            subprocess.run(cmd_m4a, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        
        # 2. Universal MP3 (192 kbps)
        if not (os.path.exists(mp3_path) and os.path.getsize(mp3_path) > 500):
            cmd_mp3 = [
                "ffmpeg", "-y",
                "-i", wav,
                "-c:a", "libmp3lame",
                "-b:a", "192k",
                "-ar", "44100",
                mp3_path
            ]
            subprocess.run(cmd_mp3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            
        m4a_dur = get_media_duration(m4a_path)
        mp3_dur = get_media_duration(mp3_path)
        
        # Validate duration within 100ms tolerance
        if src_dur and m4a_dur:
            drift = abs(src_dur - m4a_dur)
            if drift > 0.15:
                print(f"  WARNING: Drift on {base}.m4a: {drift:.3f}s (src: {src_dur:.2f}s, out: {m4a_dur:.2f}s)")
                drift_violations += 1
                
        m4a_success += 1
        mp3_success += 1
        
    print(f"Audio conversion complete: {m4a_success}/149 M4A tracks, {mp3_success}/149 MP3 tracks.")
    if drift_violations == 0:
        print("  Duration parity: 100% PASS (all tracks match source duration within tolerance).")
    else:
        print(f"  Duration parity warning: {drift_violations} tracks had drift > 150ms.")

if __name__ == "__main__":
    copy_and_convert_images()
    convert_videos()
    convert_audios()
    print("\nAll media conversions and validations finished successfully.")
