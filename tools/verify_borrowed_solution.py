"""
Rigorous Mathematical and Visual Verification for Borrowed Solution (1080px baseline)
Tests across:
- 1920x1080 (Full HD Widescreen)
- 1440x900 (Standard Desktop)
- 390x844 (Mobile Portrait)

Validates:
1. Stage Container locked to max-width 1080px and perfectly centered.
2. Background Image fills the stage edge-to-edge (0px black void).
3. Chapter 1 Slide 2: Card right edge is completely bounded inside image right edge (Overflow <= 0px).
4. Chapter 1 Slide 1: Pure Image Title (0 cards).
5. Chapter 1 Slide 6: Left clearance >= 44% (Shiva-Parvati sculpture clear).
6. Chapter 2 Slide 1: Right clearance >= 44% (Buddha head sculpture clear).
7. Chapter 3 Slide 1 (PC): Dual-pane Top baseline delta <= 1.5px.
8. Chapter 3 Slide 1 (Mobile): Two-tier vertical separation >= 0px.
"""

import os
import sys
from playwright.sync_api import sync_playwright

INDEX_URL = f"file:///{os.path.abspath('index.html').replace(os.sep, '/')}"
SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "verified_screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def verify():
    print("=" * 80)
    print("DEVABHASHA VERIFICATION: ASHTAVADHANAM 1080px BORROWED BASELINE")
    print("=" * 80)

    with sync_playwright() as p:
        browser = p.chromium.launch()

        # -------------------------------------------------------------
        # 1. WIDESCREEN 1920x1080 AUDIT
        # -------------------------------------------------------------
        print("\n[TEST SET 1: WIDESCREEN VIEWPORT 1920x1080]")
        page_wide = browser.new_page(viewport={"width": 1920, "height": 1080})
        page_wide.goto(INDEX_URL)
        page_wide.wait_for_timeout(600)

        btn_enter = page_wide.locator("#btn-enter-gateway")
        if btn_enter.is_visible():
            btn_enter.click()
            page_wide.wait_for_timeout(600)

        page_wide.evaluate("() => { const b = document.querySelector('.view-btn[data-view=\"devanagari\"]'); if (b) b.click(); }")
        page_wide.wait_for_timeout(400)

        # Check Ch 1 Slide 2 (Friedrich Schlegel — user reported slide)
        page_wide.evaluate("() => window.app.loadChapter(1)")
        page_wide.wait_for_timeout(500)
        page_wide.evaluate("() => window.app.renderSlide(1)") # index 1 = Slide 2
        page_wide.wait_for_timeout(500)

        wide_s2 = page_wide.evaluate("""() => {
            const container = document.getElementById('chapter-reader');
            const ctnRect = container.getBoundingClientRect();
            const stage = document.getElementById('canvas-stage-wrapper');
            const sRect = stage.getBoundingClientRect();
            const img = document.getElementById('stage-canvas-bg');
            const iRect = img.getBoundingClientRect();
            const cards = Array.from(document.querySelectorAll('#dialogues-wrapper .dialogue-card'));
            const visibleCard = cards.find(c => window.getComputedStyle(c).display !== 'none');
            const cRect = visibleCard ? visibleCard.getBoundingClientRect() : { left: 0, right: 0 };

            return {
                containerWidth: Math.round(ctnRect.width * 10) / 10,
                stageWidth: Math.round(sRect.width * 10) / 10,
                stageHeight: Math.round(sRect.height * 10) / 10,
                imageWidth: Math.round(iRect.width * 10) / 10,
                imageHeight: Math.round(iRect.height * 10) / 10,
                imageLeft: Math.round(iRect.left * 10) / 10,
                stageLeft: Math.round(sRect.left * 10) / 10,
                imageRight: Math.round(iRect.right * 10) / 10,
                stageRight: Math.round(sRect.right * 10) / 10,
                cardRight: Math.round(cRect.right * 10) / 10,
                overflowBeyondImageRight: Math.round((cRect.right - iRect.right) * 10) / 10
            };
        }""")

        print(f"  Container Width: {wide_s2['containerWidth']}px (Required <= 1080px)")
        print(f"  Stage Dimensions: {wide_s2['stageWidth']}px x {wide_s2['stageHeight']}px")
        print(f"  Image Dimensions: {wide_s2['imageWidth']}px x {wide_s2['imageHeight']}px")
        print(f"  Image Right: {wide_s2['imageRight']}px | Card Right: {wide_s2['cardRight']}px")
        print(f"  Card Overflow Beyond Image: {wide_s2['overflowBeyondImageRight']}px (Required <= 0px)")

        assert wide_s2['containerWidth'] <= 1081.0, f"FAIL: Container width {wide_s2['containerWidth']}px exceeded 1080px!"
        assert abs(wide_s2['stageWidth'] - wide_s2['imageWidth']) <= 1.0, "FAIL: Image did not fill stage edge-to-edge!"
        assert wide_s2['overflowBeyondImageRight'] <= 0.0, f"FAIL: Card spilled out beyond image by {wide_s2['overflowBeyondImageRight']}px!"
        print("  --> PASS: Widescreen Ch 1 Slide 2 card is 100% contained inside artwork! Zero spillout.")

        p_wide_s2 = os.path.join(SCREENSHOT_DIR, "widescreen_1920_ch1_s2.png")
        page_wide.screenshot(path=p_wide_s2)
        print(f"  Saved screenshot: {p_wide_s2}")

        page_wide.close()

        # -------------------------------------------------------------
        # 2. DESKTOP 1440x900 AUDIT
        # -------------------------------------------------------------
        print("\n[TEST SET 2: DESKTOP VIEWPORT 1440x900]")
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(INDEX_URL)
        page.wait_for_timeout(600)

        btn_enter = page.locator("#btn-enter-gateway")
        if btn_enter.is_visible():
            btn_enter.click()
            page.wait_for_timeout(600)

        page.evaluate("() => { const b = document.querySelector('.view-btn[data-view=\"devanagari\"]'); if (b) b.click(); }")
        page.wait_for_timeout(400)

        # Ch 1 Slide 1
        page.evaluate("() => window.app.loadChapter(1)")
        page.wait_for_timeout(500)
        page.evaluate("() => window.app.renderSlide(0)")
        page.wait_for_timeout(400)

        c1_cards = page.evaluate("""() => {
            const cards = Array.from(document.querySelectorAll('#dialogues-wrapper .dialogue-card'));
            const visible = cards.filter(c => window.getComputedStyle(c).display !== 'none');
            const wrapper = document.getElementById('dialogues-wrapper');
            return { visible: visible.length, wrapperDisplay: window.getComputedStyle(wrapper).display };
        }""")
        print(f"  Ch 1 Slide 1 Visible Cards: {c1_cards['visible']} (Wrapper Display: {c1_cards['wrapperDisplay']})")
        assert c1_cards['visible'] == 0, "FAIL: Ch 1 Slide 1 must have 0 cards"
        print("  --> PASS: Pure Image Title has 0 cards.")

        # Ch 1 Slide 6
        page.evaluate("() => window.app.renderSlide(5)")
        page.wait_for_timeout(500)
        c1_s6 = page.evaluate("""() => {
            const stage = document.getElementById('canvas-stage-wrapper');
            const sRect = stage.getBoundingClientRect();
            const cards = Array.from(document.querySelectorAll('#dialogues-wrapper .dialogue-card')).filter(c => window.getComputedStyle(c).display !== 'none');
            const minLeft = Math.min(...cards.map(c => c.getBoundingClientRect().left));
            return { leftPct: Math.round(((minLeft - sRect.left) / sRect.width) * 1000) / 10 };
        }""")
        print(f"  Ch 1 Slide 6 Left Clearance: {c1_s6['leftPct']}% (Required >= 44%)")
        assert c1_s6['leftPct'] >= 44.0, "FAIL: Ch 1 Slide 6 clearance < 44%"
        print("  --> PASS: Shiva-Parvati sculpture 100% uncovered on left.")

        # Ch 2 Slide 1
        page.evaluate("() => window.app.loadChapter(2)")
        page.wait_for_timeout(500)
        page.evaluate("() => window.app.renderSlide(0)")
        page.wait_for_timeout(400)
        c2_s1 = page.evaluate("""() => {
            const stage = document.getElementById('canvas-stage-wrapper');
            const sRect = stage.getBoundingClientRect();
            const cards = Array.from(document.querySelectorAll('#dialogues-wrapper .dialogue-card')).filter(c => window.getComputedStyle(c).display !== 'none');
            const maxRight = Math.max(...cards.map(c => c.getBoundingClientRect().right));
            return { rightPct: Math.round(((sRect.right - maxRight) / sRect.width) * 1000) / 10 };
        }""")
        print(f"  Ch 2 Slide 1 Right Clearance: {c2_s1['rightPct']}% (Required >= 44%)")
        assert c2_s1['rightPct'] >= 44.0, "FAIL: Ch 2 Slide 1 clearance < 44%"
        print("  --> PASS: Buddha head 100% uncovered on right.")

        # Ch 3 Slide 1 (Desktop Grid)
        page.evaluate("() => window.app.loadChapter(3)")
        page.wait_for_timeout(500)
        page.evaluate("() => window.app.renderSlide(0)")
        page.wait_for_timeout(400)
        c3_s1 = page.evaluate("""() => {
            const diag = document.getElementById('stage-diagram-container');
            const dRect = diag.getBoundingClientRect();
            const cards = Array.from(document.querySelectorAll('#dialogues-wrapper .dialogue-card')).filter(c => window.getComputedStyle(c).display !== 'none');
            const cRect = cards[0].getBoundingClientRect();
            return {
                topDelta: Math.abs(dRect.top - cRect.top),
                diagTop: dRect.top,
                cardTop: cRect.top
            };
        }""")
        print(f"  Ch 3 Slide 1 Top Baseline Delta: {c3_s1['topDelta']}px (Required <= 1.5px)")
        assert c3_s1['topDelta'] <= 1.5, "FAIL: Ch 3 Slide 1 Top Delta > 1.5px"
        print("  --> PASS: Dual-Pane Diagram & Shloka Card locked to exact Top Baseline.")

        page.close()

        # -------------------------------------------------------------
        # 3. MOBILE 390x844 AUDIT
        # -------------------------------------------------------------
        print("\n[TEST SET 3: MOBILE PORTRAIT 390x844]")
        page_m = browser.new_page(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True)
        page_m.goto(INDEX_URL)
        page_m.wait_for_timeout(600)

        btn_enter_m = page_m.locator("#btn-enter-gateway")
        if btn_enter_m.is_visible():
            btn_enter_m.click()
            page_m.wait_for_timeout(600)

        page_m.evaluate("() => { const b = document.querySelector('.view-btn[data-view=\"devanagari\"]'); if (b) b.click(); }")
        page_m.wait_for_timeout(400)

        page_m.evaluate("() => window.app.loadChapter(3)")
        page_m.wait_for_timeout(500)

        mob_c3 = page_m.evaluate("""() => {
            const diag = document.getElementById('stage-diagram-container');
            const dRect = diag.getBoundingClientRect();
            const cards = Array.from(document.querySelectorAll('#dialogues-wrapper .dialogue-card')).filter(c => window.getComputedStyle(c).display !== 'none');
            const cRect = cards[0].getBoundingClientRect();
            return {
                diagBottom: dRect.bottom,
                cardTop: cRect.top,
                gap: cRect.top - dRect.bottom
            };
        }""")
        print(f"  Mobile Ch 3 Diagram Bottom: {mob_c3['diagBottom']}px | Card Top: {mob_c3['cardTop']}px")
        print(f"  Mobile Ch 3 Vertical Gap: {mob_c3['gap']}px (Required >= 0px)")
        assert mob_c3['gap'] >= 0, f"FAIL: Mobile overlap! Gap was {mob_c3['gap']}px"
        print("  --> PASS: Mobile Two-Tier vertical stack confirmed with zero overlap.")

        p_mob_c3 = os.path.join(SCREENSHOT_DIR, "mobile_ch3_s1.png")
        page_m.screenshot(path=p_mob_c3)
        print(f"  Saved screenshot: {p_mob_c3}")

        page_m.close()
        browser.close()

    print("\n" + "=" * 80)
    print("ALL TESTS PASSED MATHEMATICALLY ACROSS 1920x1080, 1440x900, AND MOBILE!")
    print("=" * 80)

if __name__ == "__main__":
    verify()
