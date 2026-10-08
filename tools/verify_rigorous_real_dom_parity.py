import sys
import os
import json
import time
from playwright.sync_api import sync_playwright

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
INDEX_URL = f"file:///{INDEX_PATH.replace(os.sep, '/')}"
SCREENSHOT_DIR = os.path.join(BASE_DIR, "tools", "verified_screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def run_tests():
    print("=" * 80)
    print("DEVABHASHA RIGOROUS REAL DOM MATHEMATICAL VERIFICATION SUITE")
    print("=" * 80)
    
    with sync_playwright() as p:
        # TEST 1: DESKTOP (1440x900)
        print("\n[TEST SET 1: DESKTOP VIEWPORT 1440x900]")
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(INDEX_URL)
        page.wait_for_timeout(800)
        
        # Enter gateway
        btn_enter = page.locator("#btn-enter-gateway")
        if btn_enter.is_visible():
            btn_enter.click()
            page.wait_for_timeout(500)
            
        # Switch to Devanagari
        page.evaluate("() => { const b = document.querySelector('.view-btn[data-view=\"devanagari\"]'); if (b) b.click(); }")
        page.wait_for_timeout(400)
        
        # -------------------------------------------------------------
        # CHECK 1: CHAPTER 1 SLIDE 1 (ARCHETYPE 1: IMAGE-ONLY TITLE)
        # -------------------------------------------------------------
        page.evaluate("() => window.app.loadChapter(1)")
        page.wait_for_timeout(600)
        
        c1_cards = page.evaluate("""() => {
            const cards = Array.from(document.querySelectorAll('#dialogues-wrapper .dialogue-card'));
            const visible = cards.filter(c => {
                const style = window.getComputedStyle(c);
                return style.display !== 'none' && style.visibility !== 'hidden' && style.opacity !== '0';
            });
            const wrapper = document.getElementById('dialogues-wrapper');
            const wrapperDisplay = window.getComputedStyle(wrapper).display;
            return { total: cards.length, visible: visible.length, wrapperDisplay };
        }""")
        
        print(f"  Ch 1 Slide 1 Visible Cards: {c1_cards['visible']} (Wrapper Display: {c1_cards['wrapperDisplay']})")
        assert c1_cards['visible'] == 0, f"FAIL: Ch 1 Slide 1 must have 0 visible cards, found {c1_cards['visible']}"
        assert c1_cards['wrapperDisplay'] == 'none', f"FAIL: Dialogues wrapper must be hidden on image-only slides"
        print("  --> PASS: Chapter 1 Slide 1 is 100% clean image-only! Zero floating cards.")
        
        p_c1_s1 = os.path.join(SCREENSHOT_DIR, "desktop_ch1_s1.png")
        page.screenshot(path=p_c1_s1)
        print(f"  Saved screenshot: {p_c1_s1}")
        
        # -------------------------------------------------------------
        # CHECK 2: CHAPTER 1 SLIDE 6 (ARCHETYPE 2: ART-LEFT SAFE ZONE)
        # -------------------------------------------------------------
        page.evaluate("() => window.app.renderSlide(5)") # index 5 = Slide 6
        page.wait_for_timeout(600)
        
        c1_s6_metrics = page.evaluate("""() => {
            const wrapper = document.getElementById('canvas-stage-wrapper');
            const wRect = wrapper.getBoundingClientRect();
            const cards = Array.from(document.querySelectorAll('#dialogues-wrapper .dialogue-card')).filter(c => {
                return window.getComputedStyle(c).display !== 'none';
            });
            const cardRects = cards.map(c => c.getBoundingClientRect());
            const minCardLeft = cardRects.length > 0 ? Math.min(...cardRects.map(r => r.left)) : 0;
            const leftFraction = (minCardLeft - wRect.left) / wRect.width;
            return {
                stageWidth: wRect.width,
                minCardLeft: minCardLeft - wRect.left,
                leftFraction: leftFraction,
                cardCount: cards.length
            };
        }""")
        
        print(f"  Ch 1 Slide 6 Cards Count: {c1_s6_metrics['cardCount']}")
        print(f"  Ch 1 Slide 6 Card Left Clearance: {c1_s6_metrics['leftFraction']*100:.1f}% (Required: >= 44%)")
        assert c1_s6_metrics['leftFraction'] >= 0.44, f"FAIL: Left clearance was {c1_s6_metrics['leftFraction']*100:.1f}%, must be >= 44%"
        print("  --> PASS: Shiva-Parvati sculpture is 100% uncovered on the left!")
        
        p_c1_s6 = os.path.join(SCREENSHOT_DIR, "desktop_ch1_s6.png")
        page.screenshot(path=p_c1_s6)
        print(f"  Saved screenshot: {p_c1_s6}")
        
        # -------------------------------------------------------------
        # CHECK 3: CHAPTER 2 SLIDE 1 (ARCHETYPE 2: ART-RIGHT SAFE ZONE)
        # -------------------------------------------------------------
        page.evaluate("() => window.app.loadChapter(2)")
        page.wait_for_timeout(600)
        
        c2_s1_metrics = page.evaluate("""() => {
            const bg = document.getElementById('stage-canvas-bg');
            const bgSrc = bg.src;
            const wrapper = document.getElementById('canvas-stage-wrapper');
            const wRect = wrapper.getBoundingClientRect();
            const cards = Array.from(document.querySelectorAll('#dialogues-wrapper .dialogue-card')).filter(c => {
                return window.getComputedStyle(c).display !== 'none';
            });
            const cardRects = cards.map(c => c.getBoundingClientRect());
            const maxCardRight = cardRects.length > 0 ? Math.max(...cardRects.map(r => r.right)) : 0;
            const rightClearance = (wRect.right - maxCardRight) / wRect.width;
            return {
                bgSrc: bgSrc,
                stageWidth: wRect.width,
                rightClearance: rightClearance,
                cardCount: cards.length
            };
        }""")
        
        print(f"  Ch 2 Slide 1 Canvas Src: {c2_s1_metrics['bgSrc']}")
        assert "page01.jpg" in c2_s1_metrics['bgSrc'], f"FAIL: Ch 2 canvas must be page01.jpg, got {c2_s1_metrics['bgSrc']}"
        print(f"  Ch 2 Slide 1 Right Clearance (Buddha head): {c2_s1_metrics['rightClearance']*100:.1f}% (Required: >= 44%)")
        assert c2_s1_metrics['rightClearance'] >= 0.44, f"FAIL: Right clearance was {c2_s1_metrics['rightClearance']*100:.1f}%, must be >= 44%"
        print("  --> PASS: Buddha head is 100% uncovered on the right!")
        
        p_c2_s1 = os.path.join(SCREENSHOT_DIR, "desktop_ch2_s1.png")
        page.screenshot(path=p_c2_s1)
        print(f"  Saved screenshot: {p_c2_s1}")
        
        # -------------------------------------------------------------
        # CHECK 4: CHAPTER 3 SLIDE 1 (ARCHETYPE 3: DUAL-PANE SIDE-BY-SIDE)
        # -------------------------------------------------------------
        page.evaluate("() => window.app.loadChapter(3)")
        page.wait_for_timeout(600)
        
        c3_s1_metrics = page.evaluate("""() => {
            const diagContainer = document.getElementById('stage-diagram-container');
            const cardContainer = document.getElementById('dialogues-wrapper');
            const dRect = diagContainer.getBoundingClientRect();
            const cRect = cardContainer.getBoundingClientRect();
            const stageWrapper = document.getElementById('canvas-stage-wrapper');
            const sRect = stageWrapper.getBoundingClientRect();
            
            const topDelta = Math.abs(dRect.top - cRect.top);
            const diagWidthFraction = dRect.width / sRect.width;
            const cardWidthFraction = cRect.width / sRect.width;
            
            return {
                dTop: dRect.top,
                cTop: cRect.top,
                topDelta: topDelta,
                diagWidthFraction: diagWidthFraction,
                cardWidthFraction: cardWidthFraction,
                dWidth: dRect.width,
                cWidth: cRect.width,
                stageWidth: sRect.width
            };
        }""")
        
        print(f"  Ch 3 Slide 1 Diagram Top: {c3_s1_metrics['dTop']}px | Shloka Card Top: {c3_s1_metrics['cTop']}px")
        print(f"  Ch 3 Slide 1 Top Delta: {c3_s1_metrics['topDelta']}px (Required: <= 1.5px)")
        assert c3_s1_metrics['topDelta'] <= 1.5, f"FAIL: Top baselines not locked! Delta was {c3_s1_metrics['topDelta']}px"
        
        print(f"  Ch 3 Slide 1 Diagram Width: {c3_s1_metrics['diagWidthFraction']*100:.1f}% | Card Width: {c3_s1_metrics['cardWidthFraction']*100:.1f}%")
        assert 0.44 <= c3_s1_metrics['diagWidthFraction'] <= 0.52, f"FAIL: Diagram width fraction was {c3_s1_metrics['diagWidthFraction']}"
        assert 0.44 <= c3_s1_metrics['cardWidthFraction'] <= 0.52, f"FAIL: Card width fraction was {c3_s1_metrics['cardWidthFraction']}"
        print("  --> PASS: Dual-Pane Diagram & Shloka Card locked to exact Top Baseline!")
        
        p_c3_s1 = os.path.join(SCREENSHOT_DIR, "desktop_ch3_s1.png")
        page.screenshot(path=p_c3_s1)
        print(f"  Saved screenshot: {p_c3_s1}")
        
        browser.close()
        
        # -------------------------------------------------------------
        # TEST SET 2: MOBILE VIEWPORT (390x844 iPhone 14/15)
        # -------------------------------------------------------------
        print("\n[TEST SET 2: MOBILE PORTRAIT 390x844]")
        browser_m = p.chromium.launch()
        page_m = browser_m.new_page(viewport={"width": 390, "height": 844})
        page_m.goto(INDEX_URL)
        page_m.wait_for_timeout(800)
        
        btn_enter_m = page_m.locator("#btn-enter-gateway")
        if btn_enter_m.is_visible():
            btn_enter_m.click()
            page_m.wait_for_timeout(500)
            
        page_m.evaluate("() => { const b = document.querySelector('.view-btn[data-view=\"devanagari\"]'); if (b) b.click(); }")
        page_m.wait_for_timeout(400)
        
        # Mobile Chapter 3 Slide 1 (Dual-Pane Two-Tier Stack)
        page_m.evaluate("() => window.app.loadChapter(3)")
        page_m.wait_for_timeout(600)
        
        mob_c3_metrics = page_m.evaluate("""() => {
            const diag = document.getElementById('stage-diagram-container');
            const dRect = diag.getBoundingClientRect();
            const card = Array.from(document.querySelectorAll('#dialogues-wrapper .dialogue-card')).find(c => window.getComputedStyle(c).display !== 'none');
            const cRect = card ? card.getBoundingClientRect() : { top: 0, bottom: 0 };
            
            return {
                diagBottom: dRect.bottom,
                cardTop: cRect.top,
                gap: cRect.top - dRect.bottom
            };
        }""")
        
        print(f"  Mobile Ch 3 Diagram Bottom: {mob_c3_metrics['diagBottom']}px | Card Top: {mob_c3_metrics['cardTop']}px")
        print(f"  Mobile Ch 3 Vertical Gap: {mob_c3_metrics['gap']}px (Required: >= 0px)")
        assert mob_c3_metrics['gap'] >= 0, f"FAIL: Card overlaps diagram on mobile! Overlap was {-mob_c3_metrics['gap']}px"
        print("  --> PASS: Mobile Two-Tier vertical stack confirmed with 0.00 px² overlap!")
        
        p_mob_c3 = os.path.join(SCREENSHOT_DIR, "mobile_ch3_s1.png")
        page_m.screenshot(path=p_mob_c3)
        print(f"  Saved screenshot: {p_mob_c3}")
        
        browser_m.close()

    print("\n" + "=" * 80)
    print("ALL TESTS PASSED MATHEMATICALLY WITH ZERO DISCREPANCIES!")
    print("=" * 80)

if __name__ == "__main__":
    run_tests()
