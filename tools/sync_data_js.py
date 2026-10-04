"""
Canonical Data Parity Synchronizer for Devabhāṣā
Guarantees 100% parity between content/data.json and js/data.js.
Usage:
  python tools/sync_data_js.py          # Generate/sync js/data.js from content/data.json
  python tools/sync_data_js.py --check  # Fail if drift exists between data.json and data.js
"""

import sys
import os
import json
import hashlib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(BASE_DIR, "content", "data.json")
JS_PATH = os.path.join(BASE_DIR, "js", "data.js")

def compute_json_hash(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()

def extract_json_from_js(js_content):
    prefix = "const DEVABHASHA_DATA = "
    start = js_content.find(prefix)
    if start == -1:
        return None
    start += len(prefix)
    end = js_content.find(";\n\nif (typeof", start)
    if end == -1:
        end = js_content.rfind(";")
    raw_json = js_content[start:end].strip()
    return json.loads(raw_json)

def generate_js_content(json_obj):
    json_str = json.dumps(json_obj, indent=2, ensure_ascii=False)
    header = """/**
 * DEVABHĀṢĀ (1997 -> 2026) IN-MEMORY DATABASE
 * -------------------------------------------------------------
 * AUTO-GENERATED FILE. DO NOT EDIT MANUALLY!
 * Canonical source of truth: content/data.json
 * Synchronized via: python tools/sync_data_js.py
 * -------------------------------------------------------------
 */

const DEVABHASHA_DATA = """
    return header + json_str + ";\n\nif (typeof window !== 'undefined') {\n  window.DEVABHASHA_DATA = DEVABHASHA_DATA;\n}\nif (typeof module !== 'undefined') {\n  module.exports = DEVABHASHA_DATA;\n}\n"

def sync_data(check_only=False):
    if not os.path.exists(JSON_PATH):
        print(f"[ERROR] Canonical file not found: {JSON_PATH}", file=sys.stderr)
        sys.exit(1)
        
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        canonical_obj = json.load(f)
        
    canonical_hash = compute_json_hash(canonical_obj)
    
    if os.path.exists(JS_PATH):
        with open(JS_PATH, "r", encoding="utf-8") as f:
            js_content = f.read()
        try:
            existing_obj = extract_json_from_js(js_content)
            existing_hash = compute_json_hash(existing_obj)
        except Exception:
            existing_hash = None
    else:
        existing_hash = None
        
    if check_only:
        if canonical_hash == existing_hash:
            print("[PASS] js/data.js is in 100% parity with content/data.json.")
            sys.exit(0)
        else:
            print("[FAIL] DRIFT DETECTED between content/data.json and js/data.js!", file=sys.stderr)
            sys.exit(1)
            
    # Write updated js/data.js
    new_js = generate_js_content(canonical_obj)
    os.makedirs(os.path.dirname(JS_PATH), exist_ok=True)
    with open(JS_PATH, "w", encoding="utf-8") as f:
        f.write(new_js)
    print(f"[SUCCESS] Synchronized js/data.js with content/data.json (SHA-256: {canonical_hash[:16]}...)")

if __name__ == "__main__":
    check_mode = "--check" in sys.argv
    sync_data(check_only=check_mode)
