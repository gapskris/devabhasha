from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1200, 'height': 800})
    page.goto('file:///C:/DataScience/Vijay%20Ji%27s%20Music%20Conversion/Devabhasha_modern/index.html')
    page.wait_for_timeout(1000)
    page.click('#btn-enter-gateway')
    page.wait_for_timeout(500)
    page.evaluate("() => { const btn = document.querySelector('.chapter-pill[data-chapter-id=\"2\"]'); if (btn) btn.click(); }")
    page.wait_for_timeout(1000)
    page.screenshot(path='tools/test_ch2_snap.png')
    print('Saved tools/test_ch2_snap.png')
    browser.close()
