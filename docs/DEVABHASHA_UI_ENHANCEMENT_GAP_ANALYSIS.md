# Devabhāṣā (1997 CD-ROM -> Modern Web) — UI Enhancement & Forensic Analysis Report

> **Document Status**: Root Cause Analysis & Proposed Architectural Solutions  
> **Rule Adherence**: Strictly **NO CODE CHANGES IMPLEMENTED**. Submitted for User Review & Approval.  
> **Target Application**: `Devabhasha_modern/`  

---

## 1. Executive Summary of User-Reported Gaps

Based on the review of the screenshots provided by the user (`media_1791108894996.png`, `media_1791109006690.png`, and `media_1791109028807.png`), four distinct architectural and UI issues were investigated:

| # | User Observation | Root Cause Diagnosis | Proposed Architectural Remedy |
|---|------------------|----------------------|-------------------------------|
| **1** | **Pic 1**: Text cards completely overlap the background image | The dual-pane layout (`diagram-mode`) is currently restricted only to slides with `slide.diagram`. All other slides stretch `slide.canvas` to full stage background with opaque cards centered directly on top. | Make the **Dual Content Layout (Left Visual + Right Text Cards)** universal across **all slides and chapters**. |
| **2** | **Pic 3**: Devanagari is selected on top, but cards show both English and Devanagari | In `index.html`, the Devanagari button is visually marked `.active`, but in `app.js`, `this.displayView` was hardcoded to `'bilingual'`. Furthermore, card titles and prose cards were not language-mode aware. | Synchronize initial state to `devanagari` and enforce strict 3-way display filtering across all cards and headings. |
| **3** | Left menu shows Ch. 1 to 10 taking excessive vertical space | All 10 curriculum chapters are permanently expanded in the sidebar, despite the top carousel already providing 1-click access to all 10 chapters (`Page 1` to `Page 10`). | Convert `मुख्यपाठ्यक्रमः • The Curriculum` into a **collapsible accordion section** with a compact indicator. |
| **4** | Left menu is missing "Install to Mobile/PC" option (present in Ashtavadhanam) | The drawer button `<button id="btn-install-pwa-drawer">` and the PWA `beforeinstallprompt` event handler were present in Ashtavadhanam but missing in Devabhāṣā. | Add the Install button under "Tools & System" and wire the PWA install prompt and platform-specific offline installation modal. |

---

## 2. Detailed Root Cause Analysis & Proposed Solutions

---

### Issue 1: Cards Overlapping Background Images (Pic 1 vs Pic 2)

#### Visual Evidence:
* **Pic 1 (Chapter 3, Slide 1)**: The author portrait of Kalidasa (`kalidas.jpg`) is loaded as `#stage-canvas-bg` behind the cards. The text cards are centered with a width of ~75%, completely covering the portrait.
* **Pic 2 (Chapter 3, Slide 3 — Muraja Drum)**: `diagram-mode` is active. The Left 50% contains the framed sacred drum diagram, and the Right 50% contains the text cards. **Zero overlap occurs, and readability is optimal.**
* **Pic 3 (Chapter 1, Slide 1)**: The temple artwork (`chap1page01.jpg`) is on the left background, but the cards still extend over it without a structured boundary.

#### Root Cause:
In `Devabhasha_modern/js/app.js` (`renderSlide`), the dual-pane layout is conditionally toggled:
```javascript
if (slide.diagram) {
  this.canvasStageWrapper.classList.add('diagram-mode');
  // Left: Diagram, Right: Cards
} else {
  this.canvasStageWrapper.classList.remove('diagram-mode');
  // Cards placed in center directly over background image
}
```
When `slide.diagram` is `null`, `diagram-mode` is disabled, and `#stage-canvas-bg` takes `width: 100%; height: 100%`, while `.dialogues-wrapper` sits directly on top of it.

#### Proposed Solution — Universal Dual-Pane Layout:
Extend the clean, dual-pane architecture seen in Pic 2 to **ALL slides across ALL 10 chapters**:
1. **Left Visual Pane (45%–50% Width)**:
   - Displays the slide's visual asset in its authentic uncropped aspect ratio (whether `slide.diagram` or `slide.canvas`).
   - Housed within an ornate gold-bordered museum frame (`.stage-visual-frame`).
   - Includes a visual caption badge (e.g. `Sage Kalidasa — Master of Classical Poetry` or `Sacred Temple of Devabhāṣā`).
   - Includes a **`[ 🔍 Expand Visual ]`** button that opens the high-resolution lightbox modal.
2. **Right Text Pane (50%–55% Width)**:
   - Dedicated scrollable column containing the synchronized verse recitations, audios, and commentary.
   - Text never covers the artwork.
3. **Background Atmosphere**:
   - The stage background image remains as a subtle, blurred ambient texture (`opacity: 0.12`, `filter: blur(8px)`), providing visual warmth without clutter.
4. **Mobile Responsiveness**:
   - On screens `< 768px`, automatically stacks with the visual frame on top and scrollable text cards below.

---

### Issue 2: Language Switcher Discrepancy (Pic 3: Devanagari Active, but Cards Show Bilingual)

#### Visual Evidence:
* In Pic 3, the top navigation pill **`[ देवनागरी ]`** is highlighted in gold as active.
* However, the cards below display:
  1. Sanskrit Devanagari: `वागर्थाविव सम्पृक्तौ वागर्थप्रतिपत्तये...`
  2. Romanized IAST: `vāgarthāviva sampṛktau...`
  3. English translation: `For the mastery of word and sense, I bow to the Parents...`
  4. Second prose card heading and body are entirely in English (`Entering the Ancient Temple of Speech`).

#### Root Cause:
1. **State Desynchronization on Init**:
   In `index.html` (line 141):
   ```html
   <button class="view-btn btn-lang-toggle active" data-view="devanagari">देवनागरी</button>
   ```
   The HTML button has class `active` on `devanagari`.
   However, in `app.js` (line 11):
   ```javascript
   this.displayView = 'bilingual'; // Hardcoded default
   ```
   When the app loads and renders cards, `this.displayView === 'devanagari'` evaluates to `false`. Therefore, the bilingual template is executed, rendering Sanskrit + IAST + English simultaneously!
2. **Card Titles and Prose Cards Ignore Language State**:
   - Card headers currently display English titles (`〔 Raghuvamsham Invocation — Kalidasa 〕`) even when Devanagari is active.
   - Prose sections (`contentSections`) currently display only English body text without language-aware formatting.

#### Proposed Solution:
1. **Synchronize Initial State**:
   Set `this.displayView = 'devanagari'` in `app.js` to match the default active button.
2. **Enforce Strict 3-Way Language Filtering**:
   * **Mode 1: `देवनागरी` (Devanagari Only)**:
     - Shows strictly the Devanagari verse (`.text-sanskrit`).
     - Hides English IAST transliteration and English translation.
     - Displays Sanskrit title seal (e.g. `〔 रघुवंशम् — महाकवि-कालिदासः 〕`).
   * **Mode 2: `Bilingual / द्विभाषी` (Side-by-Side Dual View)**:
     - Shows Devanagari verse + IAST transliteration + English translation.
     - Seal displays bilingual identifier.
   * **Mode 3: `English (IAST)` (Romanized IAST + Translation)**:
     - Shows Romanized IAST with macrons + English translation.
     - Hides Devanagari script.
3. **Reactivity**:
   Clicking any of the 3 buttons immediately updates `this.displayView`, toggles `.mode-devanagari`, `.mode-bilingual`, `.mode-english` on `document.body`, and re-renders the cards with a smooth transition.

---

### Issue 3: Left Menu Chapter List Collapsing

#### Visual Evidence:
* The left navigation sidebar lists all 10 chapters under `मुख्यपाठ्यक्रमः • The Curriculum` with full descriptions, icons, and Sanskrit subtitles.
* This takes up 400px+ of vertical space, pushing "Treatises & Philosophy", "Historical Archives", and "Tools" below the fold.
* Meanwhile, the top carousel (`.chapter-carousel-bar`) already displays:
  `[ ◀ ] [ Page 1 ] [ Page 2 ] [ Page 3 ] ... [ Page 10 ] [ ▶ ]`
  providing direct access to every chapter.

#### Root Cause:
The curriculum group is currently rendered as a static, permanently open list:
```html
<div class="nav-group">
  <div class="nav-category-header">
    <span class="cat-sa">मुख्यपाठ्यक्रमः</span>
    <span class="cat-en">The Curriculum</span>
  </div>
  <ul class="nav-links" id="chapter-nav-list"> ... </ul>
</div>
```

#### Proposed Solution — Collapsible Curriculum Accordion:
1. Convert the category header into an interactive toggle button:
   ```html
   <button class="nav-category-toggle" id="btn-toggle-curriculum" aria-expanded="false">
     <div class="cat-title">
       <span class="cat-sa">मुख्यपाठ्यक्रमः</span>
       <span class="cat-en">The Curriculum (10 Chapters)</span>
     </div>
     <span class="accordion-arrow">▶</span>
   </button>
   ```
2. **Behavior**:
   - By default, keep it collapsed (or collapsed on mobile, compact on desktop), showing the concise summary: `Ch. 1 – Ch. 10`.
   - Clicking expands/collapses the full list with smooth CSS height animation.
   - Users can navigate directly using either the top bar pills (`Page 1..10`) or by expanding the curriculum drawer.
   - This brings Treatises, Historical Archives, and System Tools into immediate view without scrolling.

---

### Issue 4: "Install App to Mobile/PC" Option Missing in Left Menu

#### Comparison with Ashtavadhanam Baseline:
In `Ashtavadhanam_modern/index.html` (lines 320-325) and `app.js` (lines 1565-1615):
* A dedicated drawer button is provided under Category 4 ("Tools & System"):
  ```html
  <li>
    <button class="nav-link nav-link-install" id="btn-install-pwa-drawer">
      <span class="nav-icon">📲</span>
      <span class="nav-text">
        <span class="text-primary-label">Install App to PC / Mobile</span>
        <span class="text-secondary-label">यन्त्रे संस्थाप्यताम्</span>
      </span>
    </button>
  </li>
  ```
* In `Ashtavadhanam_modern/js/app.js`:
  - Listens for browser `beforeinstallprompt` event and saves `deferredPrompt`.
  - When the user clicks the button:
    - If `deferredPrompt` is available: triggers native browser prompt.
    - If in standalone mode or on iOS Safari: displays an informative modal with step-by-step guidance for Android, iOS Safari ("Add to Home Screen"), and Desktop Chrome/Edge.

#### Root Cause:
`Devabhasha_modern/index.html` has `sw.js` and `manifest.json` configured, but the UI install trigger button and prompt controller were never added to the drawer.

#### Proposed Solution:
1. **Add Install Button in Left Menu**:
   Insert the `Install App to PC / Mobile` (`यन्त्रे संस्थाप्यताम्`) button under Category 4 ("साधनानि • Tools & System") in `index.html`.
2. **Implement PWA Install Controller in `app.js`**:
   - Add `initPWAInstallPrompt()`:
     - Global listener for `beforeinstallprompt` to capture install capability.
     - Install click handler that invokes `.prompt()`.
     - Platform guidance modal fallback for iOS Safari (`Share ⎋ > Add to Home Screen`), Chrome/Edge PC (`Install icon in address bar`), and Android.
   - When running as an installed standalone app (`display-mode: standalone`), gracefully update the label to `✓ App Installed (Offline Ready)`.

---

## 3. Implementation Plan & Scope Boundary

Once approved, the implementation will touch only the necessary files:

1. **`Devabhasha_modern/css/player.css`**:
   - Generalize `.canvas-stage-wrapper.diagram-mode` into the universal `.canvas-stage-wrapper.dual-pane-mode`.
   - Style the Left Visual Frame (`.stage-visual-frame`) with antique gold borders, centered uncropped imagery, caption badge, and zoom trigger.
   - Adjust `.dialogues-wrapper` to cleanly take the right 50% without covering the visual.
   - Add accordion animation styles for `#btn-toggle-curriculum`.
2. **`Devabhasha_modern/index.html`**:
   - Structure `#stage-visual-container` and `#stage-visual-img` in the stage wrapper.
   - Add `#btn-toggle-curriculum` accordion toggle for the Curriculum category in `#nav-drawer`.
   - Add `#btn-install-pwa-drawer` under Category 4 in `#nav-drawer`.
   - Add install guidance modal (`#modal-install-guide`).
3. **`Devabhasha_modern/js/app.js`**:
   - Update `renderSlide()` to display the active slide's visual in the Left Visual Frame for all slides across all 10 chapters.
   - Fix `this.displayView = 'devanagari'` initialization and update `renderChapterCards()` to strictly follow Devanagari, Bilingual, and English modes.
   - Add accordion toggle handler for Curriculum in the left menu.
   - Implement `initPWAInstallPrompt()` and wire `#btn-install-pwa-drawer`.
4. **Verification**:
   - Run `python Devabhasha_modern/tools/sync_data_js.py`.
   - Run `python Devabhasha_modern/tools/verify_1to1_mapping.py` to ensure all 82 checks pass at 100%.

---

## 4. Review Request

Please review this root cause diagnosis and proposed solution. Upon your confirmation, implementation will proceed.
