# Forensic Root Cause Analysis & Proposed Solutions

**Project**: Devabhāṣā (1997 CD-ROM → 2026 Modern Web Application)  
**Reference Screenshot**: `media_1791111650235.png` (Chapter 1, Slide 1 of 6)  
**Status**: Analysis Complete — Awaiting User Review before Implementation  

---

## Executive Summary & Findings Matrix

| # | Reported Issue | Root Cause | Original 1997 CD-ROM Parity Check | Proposed Remedy |
|---|---|---|---|---|
| **1** | **Top Right Expand (⛶) & TV (📺) Icons Not Working** | Neither `#btn-fullscreen` nor `#btn-tv-mode` has event listeners registered in `js/app.js` `bindEvents()`. | CD-ROM ran in fixed 800×600 projector mode. Modern web app introduces 10-foot Smart TV remote navigation (`js/tv-remote.js`) and HTML5 Fullscreen API, but buttons were left unwired. | Wire `#btn-fullscreen` to `document.documentElement.requestFullscreen()` / `document.exitFullscreen()` and `#btn-tv-mode` to `this.tvRemote.toggleTvMode()`. |
| **2** | **Devanagari Selected but English Texts Displayed** *(Is this in original CD-ROM?)* | **Yes, in the 1997 CD-ROM, Chapter 1 was an introductory essay written in English.** However, in the modern app, when `देवनागरी` is selected, English badges, English card titles, and English prose cards are still displayed because the language filter only hid `.text-english` on verse cards. | In the 1997 CD-ROM, Chapter 1 ("The Language of India") was written in English by the Sri Aurobindo Society authors to introduce Sanskrit to international seekers, accompanied by 1 Sanskrit shloka audio (`chap 1.wav` = *Raghuvamsham* 1:1). | 1. Use Sanskrit Devanagari seals/titles for cards (e.g. `〔 रघुवंश-मङ्गलाचरणम् • कालिदासः 〕`).<br>2. In `देवनागरी` mode, hide purely English prose commentary cards so only authentic Devanagari verses appear. |
| **3** | **Enlarge Chapter Container** *(Excess space on left, right, and below)* | `.stage-container` has an artificial `max-width: 1080px` constraint, `.main-content` has `max-width: 1440px`, and `.canvas-stage-wrapper` has `aspect-ratio: 800 / 600`. On modern widescreen displays, this leaves over 500px of empty borders and squeezes dual panes to only 540px. | The 1997 CD-ROM had a single 800×600 stage. The modern app uses a dual-pane presentation (left visual, right cards), which requires a wider, fluid widescreen canvas (`max-width: min(1500px, 96%)`). | Expand `.stage-container` max-width to `min(1500px, 96%)`, increase `.main-content` width, remove rigid 4:3 aspect ratio in dual-pane mode, and set fluid height (`clamp(520px, 70vh, 760px)`). |
| **4** | **Audio Started from Card Cannot be Paused from Card** | `playClip(index)` in `js/player.js` unconditionally restarts playback (`playTrack()`). It lacks toggle logic to check if `this.currentIndex === index && this.isPlaying`. | In Director Lingo, clicking a sound sprite triggered `sound playFile` or toggled sound channels. | Update `playClip(index)`: If `this.currentIndex === index && this.isPlaying`, call `togglePlay()` to pause audio. If already paused, resume playback. If a different card is clicked, play new track. |

---

## Detailed Root Cause Analysis

### Issue 1: Top-Right Fullscreen (⛶) and Smart TV (📺) Buttons Not Working

#### Forensic Code Evidence
In [`Devabhasha_modern/index.html`](file:///c:/DataScience/Vijay%20Ji%27s%20Music%20Conversion/Devabhasha_modern/index.html) lines 151–152:
```html
<button id="btn-tv-mode" class="icon-btn" title="Toggle Smart TV 10-Foot Mode" aria-label="Smart TV Mode">📺</button>
<button id="btn-fullscreen" class="icon-btn" title="Toggle Fullscreen" aria-label="Fullscreen">⛶</button>
```
In [`Devabhasha_modern/js/tv-remote.js`](file:///c:/DataScience/Vijay%20Ji%27s%20Music%20Conversion/Devabhasha_modern/js/tv-remote.js):
- The `DevabhashaTvRemote` controller is fully implemented with D-pad navigation, focus management, and keyboard shortcut `T`.
- It defines `toggleTvMode()`.
In [`Devabhasha_modern/js/app.js`](file:///c:/DataScience/Vijay%20Ji%27s%20Music%20Conversion/Devabhasha_modern/js/app.js):
- Search, Shlokas concordance, Help, and Exit buttons are wired in `bindEvents()`.
- **Neither `#btn-tv-mode` nor `#btn-fullscreen` has any event listener attached.**

#### Proposed Remedy
Add in `bindEvents()` of `app.js`:
```javascript
// TV Mode Toggle Button
const btnTv = document.getElementById('btn-tv-mode');
if (btnTv) {
  btnTv.addEventListener('click', () => {
    if (this.tvRemote) {
      this.tvRemote.toggleTvMode();
      btnTv.classList.toggle('active', this.tvRemote.isTvMode);
    }
  });
}

// Fullscreen Toggle Button
const btnFs = document.getElementById('btn-fullscreen');
if (btnFs) {
  btnFs.addEventListener('click', () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => console.warn(err));
    } else {
      document.exitFullscreen().catch(err => console.warn(err));
    }
  });
  document.addEventListener('fullscreenchange', () => {
    btnFs.classList.toggle('active', !!document.fullscreenElement);
    btnFs.textContent = document.fullscreenElement ? '🗗' : '⛶';
  });
}
```

---

### Issue 2: Devanagari Selected but English Texts Displayed — Is this in the Original CD-ROM?

#### CD-ROM Forensic Source Analysis
We decompiled and inspected `chapter1.dxr` and the audio repository `media/chap1/` from the original 1997 CD-ROM:
1. **Audio Source**:
   - `media/chap1/chap 1.wav` is the **only audio file** in Chapter 1.
   - It contains the recitation of Mahakavi Kalidasa’s opening verse from *Raghuvamsham* (1:1):
     > वागर्थाविव सम्पृक्तौ वागर्थप्रतिपत्तये ।  
     > जगतः पितरौ वन्दे पार्वतीपरमेश्वरौ ॥
2. **Text Source in `chapter1.dxr`**:
   - The original text extracted from Director movie `chapter1.dxr` begins:
     > *"Let it be known right at the outset that this book is not written by a scholar and furthermore is not meant for scholars. In spite of never having studied Sanskrit in a systematic manner or in great depth, I too surrendered to the stereotype of Sanskrit being a very difficult language to learn... We took up a project called 'The Wonder that is Sanskrit'..."*
   - It then presents the quotes of Western and Indian scholars (Prof. Friedrich Schlegel, W.C. Taylor, Will Durant, Sri Aurobindo, Dr. David Frawley).
3. **Historical Verdict**:
   - **Yes, in the original 1997 CD-ROM, the introductory essay of Chapter 1 was written in English.**
   - The CD-ROM was designed by the Sri Aurobindo Society as an educational cultural multimedia application to introduce the world to Sanskrit. Chapters 1, 8, and 9 were conceptualized as English analytical essays.
   - Chapters 2, 3, 4, 5, 6, 7, and 10 were centered on Sanskrit recitation audio with Devanagari verses (Panini sutras, Chitrakavya visual puzzles, classical poetry, Subhashitas, Vedic hymns).

#### Why English Appeared in Modern App when `देवनागरी` Mode was Selected
1. **Verse Card Seal**:
   The seal header says `〔 Raghuvamsham Invocation — Kalidasa 〕` (English). In `देवनागरी` mode, the seal badge should be in Sanskrit: `〔 रघुवंश-मङ्गलाचरणम् • कालिदासः 〕`.
2. **Prose Card (`contentSections`)**:
   Chapter 1 has 6 prose sections containing the 1997 introductory essay ("Entering the Ancient Temple of Speech", "An Enthralling Discovery", etc.). Because these sections do not have Sanskrit verses, they displayed as English cards even when the user toggled `देवनागरी` ("Devanagari script only").

#### Proposed Remedy
1. **Sanskrit Seal Badges**:
   When `this.displayView === 'devanagari'`, format the card seal using Sanskrit titles:
   - Chapter 1: `〔 रघुवंश-मङ्गलाचरणम् • महाकवि-कालिदासः 〕`
   - In `bilingual` mode: `〔 रघुवंशम् • Raghuvamsham Invocation 〕`
   - In `english` mode: `〔 Raghuvamsham Invocation — Kalidasa 〕`
2. **Prose Cards Visibility in `देवनागरी` Mode**:
   - When the user selects `देवनागरी` ("Devanagari script only"): Hide purely English prose essay cards (`prose-card`), displaying only authentic Sanskrit recitation cards.
   - When the user selects `Bilingual / द्विभाषी` or `English (IAST)`: Display the prose essay cards alongside the recitations.
   - This ensures that in `देवनागरी` mode, **100% of visible card content is authentic Sanskrit Devanagari script**, fulfilling the user's expectation.

---

### Issue 3: Enlarge Chapter Container (Widescreen Dual-Pane Optimization)

#### Forensic Code Evidence
In [`Devabhasha_modern/css/main.css`](file:///c:/DataScience/Vijay%20Ji%27s%20Music%20Conversion/Devabhasha_modern/css/main.css):
```css
.stage-container {
  width: 100%;
  max-width: 1080px; /* <--- ARTIFICIAL RESTRICTION */
  margin: 0 auto;
}
.main-content {
  max-width: 1440px;
  padding: 16px 20px 95px 20px;
}
```
In [`Devabhasha_modern/css/player.css`](file:///c:/DataScience/Vijay%20Ji%27s%20Music%20Conversion/Devabhasha_modern/css/player.css):
```css
.canvas-stage-wrapper {
  aspect-ratio: 800 / 600; /* <--- FORCED 4:3 LEGACY PROPORTION */
  max-height: 820px;
}
```
- Because `.stage-container` was restricted to `max-width: 1080px`, on a standard 1080p desktop (1920px width), there was **over 500px of dead brown margin** surrounding the container.
- Each half of the dual-pane was constrained to only ~530px.
- The `aspect-ratio: 800 / 600` forced a boxy 4:3 frame, leaving an awkward empty gap below the container before the floating audio bar.

#### Proposed Remedy
1. **Increase Container Max-Width**:
   Change `.stage-container` `max-width` from `1080px` to `min(1520px, 96%)`.
   Update `.main-content` `max-width` to `min(1600px, 98%)`.
2. **Fluid Dual-Pane Height**:
   In `.canvas-stage-wrapper.diagram-mode`:
   - Replace fixed `aspect-ratio: 800 / 600` with `min-height: clamp(520px, 68vh, 760px); height: auto; aspect-ratio: auto;`.
3. **Expansive Visual & Card Panes**:
   - The left pane displaying the artwork/diagram expands comfortably to 650–720px width, allowing intricate diagrams (such as Chapter 2 vocal tracts and Chapter 3 Chitrakavya charts) to be viewed with superior clarity.
   - The right pane expands to 650–720px width, allowing Sanskrit verses and translations to breathe without cramped vertical stacking.

---

### Issue 4: In-Card Audio Cannot be Paused from the Card

#### Forensic Code Evidence
In [`Devabhasha_modern/js/app.js`](file:///c:/DataScience/Vijay%20Ji%27s%20Music%20Conversion/Devabhasha_modern/js/app.js) lines 758–770:
```javascript
card.addEventListener('click', () => {
  if (window.Player) window.Player.playClip(idx);
});

const btn = card.querySelector('.dialogue-audio-btn');
if (btn) {
  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    if (window.Player) window.Player.playClip(idx);
  });
}
```
In [`Devabhasha_modern/js/player.js`](file:///c:/DataScience/Vijay%20Ji%27s%20Music%20Conversion/Devabhasha_modern/js/player.js) lines 140–145:
```javascript
playClip(index) {
  if (!this.playlist || !this.playlist[index]) return;
  this.currentIndex = index;
  const track = this.playlist[index];
  this.playTrack(track); // <--- UNCONDITIONALLY RESTARTS PLAYBACK
}
```
- When a recitation track is actively playing, `player.js` changes the in-card button symbol to `❚❚` (pause).
- However, when the user clicks the card or the `❚❚` button, it calls `window.Player.playClip(idx)`.
- Because `playClip` has **no toggle logic**, it re-invokes `playTrack()`, which calls `audio.play()` from the beginning instead of pausing!

#### Proposed Remedy
Update `playClip(index)` in `Devabhasha_modern/js/player.js`:
```javascript
playClip(index) {
  if (!this.playlist || !this.playlist[index]) return;

  // 1. If currently playing this exact clip, PAUSE IT
  if (this.currentIndex === index && this.isPlaying) {
    this.togglePlay();
    return;
  }

  // 2. If this exact clip is paused, RESUME IT
  if (this.currentIndex === index && !this.isPlaying && this.audio.src) {
    this.togglePlay();
    return;
  }

  // 3. Otherwise, switch to the newly selected clip and start playback
  this.currentIndex = index;
  const track = this.playlist[index];
  this.playTrack(track);
}
```
- Clicking the active card or its `❚❚` button pauses audio immediately and flips the icon to `▶`.
- Clicking it again resumes playback seamlessly.
- Clicking any other card immediately switches to that new recitation track.

---

## Action Plan (Pending User Approval)

1. **Wire Top-Right Fullscreen (⛶) and Smart TV (📺) buttons** in `js/app.js` with active state visual feedback.
2. **Synchronize Devanagari Mode with Sanskrit Seals and Hide English Prose Cards** in `js/app.js` when `देवनागरी` is active, while preserving full English commentary in `Bilingual` and `English` modes.
3. **Expand Stage Container & Dual-Pane Width** in `css/main.css` and `css/player.css` to `min(1520px, 96%)` with fluid viewport height.
4. **Implement Card Play/Pause Toggle** in `js/player.js`.
5. **Run automated 82-point forensic verification suite** (`python tools/verify_1to1_mapping.py`) to confirm zero regressions.
