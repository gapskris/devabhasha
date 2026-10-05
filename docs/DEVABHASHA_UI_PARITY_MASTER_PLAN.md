# DEVABHASHA UI & ANIMATION MODERNIZATION MASTER PLAN
## Exact Visual, Functional, and Animation Parity with Ashtavadhanam (Screenshots 1, 2, and 3)

---

### Executive Overview & Objectives

Based on the three reference screenshots from the proven **Ashtavadhanam** implementation:
- **Pic 1**: Classical Amber/Bronze Landing Page with Sacred Crest, Ornate Calligraphy Box, and Dual Action Gates.
- **Pic 2**: Framed Cultural Mosaic Stage with Seamless Dissolve, Embedded Archival Video Window, and Theater Mode.
- **Pic 3**: Complete Performance/Curriculum Shell with Top Navigation Header, 3-Way Sanskrit/English Script Switcher, Collapsible Categorized Sidebar, Chapter Carousel, and Parchment Canvas Reader with Stacked Audio Recitation Cards.

This plan details the exact architectural, CSS, JavaScript, and animation overhaul required to make **Devabhāṣā Modern** identical in visual elegance, interaction design, and feature richness, while resolving all animation stutter and frame-drops for **butter-smooth 60fps/120fps hardware-accelerated performance**.

---

### 1. Root Cause Analysis: Animation Stutter & Solutions

#### A. Landing Page Calligraphic Dissolve (S01 to S06)
* **Observed Problem**: Frame hesitation, sudden pop-ins, and uneven pacing during the progressive reveal of the title calligraphy.
* **Technical Root Causes**:
  1. **Main-Thread Image Decoding**: Browsers decode JPEG images synchronously on the UI thread when their opacity is first toggled, dropping frames.
  2. **Timer Drift**: Using uncoordinated `setTimeout` or `setInterval` intervals (e.g., 400ms) that do not synchronize with the monitor's vertical sync (V-Sync).
  3. **Compositing Recalculations**: Stacking images without GPU layer promotion forces ancestor layout recomputation.
* **Definitive Modern Solution**:
  - **Asynchronous Pre-decoding**: Pre-load and decode all 6 title frames (`S01.jpg` – `S06.jpg`) using `HTMLImageElement.decode()` prior to starting the animation:
    ```javascript
    await Promise.all(frames.map(img => img.decode()));
    ```
  - **GPU Hardware Promotion**: Apply `transform: translate3d(0, 0, 0); will-change: opacity; contain: strict;` to ensure GPU composited layers.
  - **Web Animations API / rAF Driver**: Drive cross-fading through `requestAnimationFrame` with high-precision timestamps (`performance.now()`), or declarative CSS transitions with cubic-bezier easing (`cubic-bezier(0.25, 1, 0.5, 1)`).

#### B. Montage Video & Cultural Mosaic Animation (03 -> 02 -> 01 -> Video)
* **Observed Problem**: Choppy cross-fade between mosaic frames (03 Color $\rightarrow$ 02 Sepia $\rightarrow$ 01 Cutout), followed by a 200–500ms freeze before the video starts playing.
* **Technical Root Causes**:
  1. **Cold Video Decoder Spin-up**: The browser's H.264 video hardware decoder is spun up only when `video.play()` is called inside the `01.jpg` cutout, creating an inevitable startup stall.
  2. **Chained `setTimeout` Delays**: Using 1200ms and 2400ms timers that get delayed if garbage collection or script execution occurs.
* **Definitive Modern Solution**:
  - **Pre-primed Video Decoder**: During the user's initial click on "Play Opening Montage", synchronously call `video.load()`, set `video.currentTime = 0`, and keep the first decoded frame ready in memory.
  - **Synchronized Visual Hand-off**: When `01.jpg` reaches full opacity, unhide `#mosaic-video-window` with `video.play()` already pre-warmed.
  - **Dedicated Layer Compositing**: Wrap the video inside a hardware-composited container with fixed aspect-ratio (`4 / 3`) and overflow clipping.

---

### 2. Comprehensive UI Screen Specification

#### Screen 1: Landing Page (Pic 1 Parity)

```
+-------------------------------------------------------------------------+
|                                                                         |
|                         [ ☸ Sacred Gold Emblem ]                        |
|                        ॥ ॐ श्री अरविन्दाय नमः ॥                         |
|             ✦ वाग् वै ब्रह्म • SPEECH IS THE SUPREME DIVINE ✦            |
|                                                                         |
|                +---------------------------------------+                |
|                | ✥                                   ✥ |                |
|                |                                       |                |
|                |      [ S01-S06 Calligraphy Frames ]   |                |
|                |       "THE WONDER THAT IS SANSKRIT"   |                |
|                |         (Smooth 60fps Cross-fade)     |                |
|                |                                       |                |
|                | ✥                                   ✥ |                |
|                +---------------------------------------+                |
|                                                                         |
|                 Devabhāṣā — The Language of the Gods                    |
|       Historic 1997 CD-ROM Master Production • Sri Aurobindo Society     |
|                                                                         |
|  [ ▶ प्रवेशः • Play Opening Montage ]   [ प्रविश्यताम् • Enter Curriculum ▶ ] |
|                                                                         |
+-------------------------------------------------------------------------+
```

* **Background**: Royal amber-bronze radial gradient (`radial-gradient(circle at 50% 40%, #5c3a21 0%, #301a0d 60%, #150a04 100%)`).
* **Sacred Inscription Crest**:
  - Circular gold medallion with sage/scholar emblem.
  - Devanagari text in *Noto Serif Devanagari* with gold drop shadow.
* **Visual Frame Box**:
  - Ornate dark bronze frame with gold inner border and corner florets (`✥`).
  - Stacked 6-frame calligraphy sequence (`S01` to `S06`) smoothly revealing the title artwork and star sparkle on the letter 'T'.
* **Dual Action Buttons**:
  - Primary (Gold Gradient): `▶ प्रवेशः • Play Authentic Opening Montage & Invocations`
  - Secondary (Dark Bronze / Gold Border): `प्रविश्यताम् • Enter Curriculum Directly ▶`

---

#### Screen 2: Authentic Cultural Mosaic & Montage Stage (Pic 2 Parity)

```
+-------------------------------------------------------------------------+
|                                                                         |
|                +---------------------------------------+                |
|                | [ 03.jpg (Color) -> 02.jpg (Sepia) ]  |                |
|                | [ -> 01.jpg (B&W Cutout with Video) ] |                |
|                |                                       |                |
|                | [ 🔲 Expand Theater ]     [ 🔊 Sound: ON ] |            |
|                +---------------------------------------+                |
|                                                                         |
|                     Authentic 1997 Cultural Mosaic                      |
|                        Phase 2: Transition Mosaic                       |
|                     [==============--------] (Progress)                |
|                                                                         |
|                     [ प्रविश्यताम् • Enter Curriculum ▶ ]               |
|                                                                         |
+-------------------------------------------------------------------------+
```

* **Dissolve Pipeline**:
  - `03.jpg` (Full Color Cultural Collage) fades in smoothly.
  - Transitions over 1.2s to `02.jpg` (Sepia Tone Transition).
  - Transitions over 1.2s to `01.jpg` (Monochrome Cutout).
  - Center window (`#mosaic-video-window`) displays `montage.mp4` with high-fidelity audio.
* **Floating Badges**:
  - `🔲 Expand Theater` / `🖼️ 1997 Mosaic Frame` (toggles full frame video vs authentic 1997 cutout).
  - `🔊 Sound: ON` / `🔇 Sound: OFF` (instant volume toggle).
* **Live Progress Bar**: Synchronized with video playback duration (`0%` to `100%`).
* **Direct Navigation**: Skip button to immediately enter the main portal.

---

#### Screen 3: Main Performance / Curriculum Portal (Pic 3 Parity)

```
+---------------------------------------------------------------------------------------+
| ☰  (☸) देवभाषा • Devabhāṣā       [ देवनागरी | Bilingual / द्विभाषी | English ]   🔍 ❓ 🎨 ⛶ |
+---------------------------------------------------------------------------------------+
| [ < ]  (Ch. 1)  (Ch. 2)  (Ch. 3)  (Ch. 4)  (Ch. 5)  (Ch. 6)  (Ch. 7) ... [ > ]       |
+-------------------+-------------------------------------------------------------------+
| ॥ विषयसूची ॥  [ < ]| Chapter 1 of 10                                 [ ▶ Play All ]    |
| TABLE OF CONTENTS | 6 Audio Recitations • 6 Western & Indian Scholars                 |
|                   +-------------------------------------------------------------------+
| मुख्यपाठ्यक्रमः   | +---------------------------------------------------------------+ |
| 🕮 10 Chapters    | | ( अवधानी / वक्ता • Speaker )                             ( ▶ ) | |
|                   | | योऽन्तः प्रविश्य मम वाचमिमां प्रसुप्ताम् ...                  | |
| शास्त्रग्रन्थाः   | +---------------------------------------------------------------+ |
| 🪶 Linguistic     | +---------------------------------------------------------------+ |
| 📜 Chitrakavya    | | ( अनुवादः • Translation )                                     | |
|                   | | "He who entering within vitalizes my sleeping speech..."       | |
| ऐतिहासिकलेखागारः  | +---------------------------------------------------------------+ |
| 🏛 Institutions   |                                                                   |
| ⚜ Society (SAS)   |                       ▼ अधिकम् • Scroll for more                  |
| 🖼 Visual Gallery |                                                                   |
| 📜 Credits        |                                                                   |
+-------------------+-------------------------------------------------------------------+
```

1. **Top Application Header**:
   - Left: Hamburger toggle `☰`, Gold circular emblem, `देवभाषा • Devabhāṣā` and English subtitle.
   - Center: 3-way language toggle pill (`[ देवनागरी ]`, `[ Bilingual / द्विभाषी ]`, `[ English (IAST) ]`).
   - Right: Direct quick action buttons (`🔍 Search`, `❓ Help`, `🎨 Theme`, `⛶ Fullscreen`).
2. **Top Chapter Pagination Carousel**:
   - Navigation arrows `[ < ]` and `[ > ]`.
   - Distinct rounded pill buttons for each of the 10 chapters, with active chapter highlighted in rich gold with dark text.
3. **Collapsible Categorized Sidebar (`॥ विषयसूची ॥`)**:
   - `मुख्यपाठ्यक्रमः THE CURRICULUM` (Active chapter card and quick links).
   - `शास्त्रग्रन्थाः TREATISES & PHILOSOPHY` (Linguistic studies, Chitrakavya visual anagrams).
   - `ऐतिहासिकलेखागारः HISTORICAL ARCHIVES` (Participating Sanskrit Institutions, Sri Aurobindo Society, Master Visual Gallery of 127 assets, Credits).
   - `तन्त्राणि TOOLS & SYSTEM` (Sanskrit Search Engine, User Guide & Help, Replay Opening Montage, Install App to PC/Mobile, Temple Bell Chimes toggle, Exit).
4. **Parchment Stage Canvas & Recitation Cards**:
   - Stage header with `Chapter X of 10`, subtitle with track count, and `▶ Play All in Chapter`.
   - Warm parchment background with subtle left decorative illumination.
   - Stacked recitation cards with speaker badge `( अवधानी / वक्ता • Speaker )`, Devanagari typography (*Noto Serif Devanagari*), translation toggle, and circular play button `[ ▶ ]`.
   - Bottom scroll indicator badge: `▼ अधिकम् • Scroll for more`.

---

### 3. Step-by-Step Implementation Roadmap

| Phase | Milestone | Action Items | Deliverables & Verification |
| :---: | :--- | :--- | :--- |
| **1** | **CSS Modernization & Visual Layout** | Re-engineer `css/main.css` to match Ashtavadhanam's design tokens, amber radial background, ornate frames, typography, badges, and layout structure. | `css/main.css` updated; visual parity verified against Pics 1, 2, and 3. |
| **2** | **Landing & Montage Smooth Animations** | Implement image pre-decoding (`HTMLImageElement.decode()`), pre-buffer video decoder (`video.load()`), and GPU compositing rules to eliminate all jank. | 60fps smooth title dissolve and zero-stall video hand-off. |
| **3** | **HTML Structure Realignment** | Align `index.html` structure: splash gateway, dual-mode opening stage, top carousel bar, 4-tier sidebar drawer, and parchment canvas stage. | `index.html` fully mirrors Ashtavadhanam UI hierarchy. |
| **4** | **JS Application Controller Expansion** | Enhance `js/app.js` with carousel pagination, 3-way script toggling, stacked card audio triggers, modal bindings, and theater mode toggle. | All controls functional in `js/app.js` and `js/player.js`. |
| **5** | **Audit & Forensic Verification** | Run `verify_1to1_mapping.py` and inspect browser execution to guarantee 100% preservation of all 149 audio tracks, 127 images, 1 video, and 10 chapters. | Automated test suite passes 100% with zero regressions. |

---
