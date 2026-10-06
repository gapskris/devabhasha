#!/usr/bin/env python3
"""
Devabhāṣā Modern — Master Test Suite Runner
Executes all verification suites and dynamic audit tests in sequence:
  1. Canonical Data Parity Test (sync_data_js.py --check)
  2. 43-Point / 82-Check Forensic Parity Audit (verify_1to1_mapping.py)
  3. Sanskrit Text & Ligature Corruption Audit (audit_sanskrit_cards.py)
  4. 9-Stage Deep Engineering & Playwright Runtime Audit (test_audit_9stage_deep_engineering.py)
"""

import os
import sys
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TESTS = [
    ("Canonical Data Parity Verification", [sys.executable, os.path.join(PROJECT_ROOT, "tools", "sync_data_js.py"), "--check"]),
    ("Sanskrit Devanagari Ligature & Corruption Audit", [sys.executable, os.path.join(PROJECT_ROOT, "tools", "audit_sanskrit_cards.py")]),
    ("Orthogonal Sanskrit Forensic Parity Audit (7 Axes / 52 Checks)", [sys.executable, os.path.join(PROJECT_ROOT, "tools", "audit_orthogonal_sanskrit.py")]),
    ("Automated Sanskrit Orthography & Forensic Test Suite", [sys.executable, os.path.join(PROJECT_ROOT, "tests", "test_orthogonal_sanskrit.py")]),
    ("43-Point / 82-Check Forensic 1-to-1 Mapping Audit", [sys.executable, os.path.join(PROJECT_ROOT, "tools", "verify_1to1_mapping.py")]),
    ("9-Stage Deep Engineering & Playwright Runtime Audit", [sys.executable, os.path.join(PROJECT_ROOT, "tests", "test_audit_9stage_deep_engineering.py")])
]

def run_all():
    print("=" * 80)
    print("DEVABHĀṢĀ MODERN — MASTER COMPREHENSIVE TEST & AUDIT SUITE")
    print("=" * 80)

    all_passed = True
    for name, cmd in TESTS:
        print(f"\n>>> RUNNING: {name} ...")
        res = subprocess.run(cmd, cwd=PROJECT_ROOT)
        if res.returncode != 0:
            print(f"FAILED: {name} (exit code {res.returncode})")
            all_passed = False
        else:
            print(f"PASSED: {name}")

    print("\n" + "=" * 80)
    if all_passed:
        print("ALL TEST & AUDIT SUITES PASSED AT 100%! READY FOR GLOBAL PRODUCTION!")
    else:
        print("FAILURES DETECTED IN MASTER TEST SUITE.")
    print("=" * 80)

    sys.exit(0 if all_passed else 1)

if __name__ == '__main__':
    run_all()
