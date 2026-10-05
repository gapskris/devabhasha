# Devabhasha Modernization — Final Phase-Wise Strategic Plan & Preservation Doctrine
*(देवभाषा — The Language of the Gods / The Wonder that is Sanskrit)*
**Macromedia Director (1997–2000 CD-ROM) → Modern Open-Web Progressive Web Application (2026)**

---

## 1. Executive Overview & Scope

The objective of this project is to convert the complete contents of the historical multimedia CD-ROM **"Devabhasha — The Language of the Gods"** (1997–2000), produced by the **Sri Aurobindo Society** (Pondicherry), into a modern, browser-based, cross-device Progressive Web Application (PWA).

By replacing obsolete legacy runtimes (Macromedia Director, Flash, Indeo AVI, uncompressed 16-bit PCM WAV, 8-bit typewriter fonts) with open web standards (**HTML5, Modular CSS3, ES6+ JavaScript, JSON, dual M4A/MP3, and Faststart MP4**), the modern application maximizes cultural longevity, academic accessibility, and zero-install portability across desktop computers, mobile devices, tablets, and Smart TVs.

```mermaid
graph TD
    subgraph Archival Baseline [Devabhasha_master/ (Immutable Source)]
        DXR[19 Director Movies .dxr]
        CXT[20 Director Casts .cxt]
        WAV[149 Recitations .wav 314 MB]
        AVI[1 Opening Montage .avi 37 MB]
        SWF[85 Flash Animations .swf]
        IMG[127 Master Visuals .jpg / .bmp]
    end

    subgraph Forensic Modernization Pipeline [Non-Destructive Extraction]
        P1[Dual Audio: M4A AAC-LC + MP3 Fallback]
        P2[Video: Faststart H.264 / AAC MP4]
        P3[Typography: VedicBrahma2 -> Devanagari Unicode & IAST]
        P4[Flash Decompilation: Native HTML5 / Canvas / SVG]
        P5[Canonical Contract: content/data.json -> js/data.js]
    end

    subgraph Target Web Deliverable [Devabhasha_modern/ PWA]
        APP[Responsive Single-Page Shell]
        CH[10 Thematic Curriculum Chapters]
        SHL[Master Shlokas Concordance & Audio Explorer]
        SRC[Sanskrit & Devanagari Search Engine]
        TV[10-Foot Smart TV D-Pad Interface]
        PWA_C[Service Worker Media-Safe Offline PWA]
    end

    DXR --> P3
    CXT --> P3
    WAV --> P1
    AVI --> P2
    SWF --> P4
    IMG --> P5

    P1 --> SHL
    P2 --> APP
    P3 --> P5
    P4 --> CH
    P5 --> APP
    P5 --> CH
    P5 --> SHL
    P5 --> SRC
    APP --> TV
    APP --> PWA_C
```

### Architectural Core
- **Behavioral Baseline**: Legacy files (`.swf`, `.dxr`, `.cxt`, `.wav`, `.avi`) serve strictly as migration sources and do **NOT** exist as runtime dependencies in the final application.
- **Decoupled Architecture**: Educational, philosophical, and recitation content is strictly separated from the presentation layer.
- **Canonical Data Layer**: A single source of truth in JSON (`content/data.json`) is mirrored to an in-memory database (`js/data.js`) via automated synchronization (`tools/sync_data_js.py`), allowing seamless zero-install portability across both HTTP/HTTPS servers and direct double-click `file:///` protocols without CORS restrictions.

### Archival Boundary & Asset Separation
A strict, immutable boundary separates original archival materials from modern web deliverables:
1. **`Devabhasha_master/` — Immutable Archival Source**: Represents the permanent historical baseline. Files in this directory must never be modified, renamed, overwritten, or deleted.
2. **`Devabhasha_modern/` — Modern Web Deliverable**: Contains all derived modern assets (`assets/audio/`, `assets/images/`, `assets/video/`), the canonical content layer (`content/data.json`), application controllers (`js/`), and styling (`css/`).
3. **Mandatory Workspace Creation**: Prior to commencing any extraction, transcoding, or development work, the developer or autonomous AI agent **MUST** create the target project directory `Devabhasha_modern/` in the workspace root alongside `Devabhasha_master/`. All modernization work, source code, converted assets, databases, styles, and tests **MUST** be executed exclusively within `Devabhasha_modern/`. Under no circumstance should converted files be written back into `Devabhasha_master/`.
4. **Non-Destructive Invariant**: Never replace the archival source with an optimized delivery derivative. All conversions are strictly additive transformations from the archival baseline into the modern project directory.

---

## 2. Core Heritage Preservation Doctrines & Operational Rules

To ensure forensic integrity and protect the project from well-intentioned but unauthorized changes by autonomous agents, the following five preservation rules are mandatory and non-negotiable:

> [!IMPORTANT]
> ### The 5 Non-Negotiable Preservation Rules
> 1. **Rule 1 — Source Immutability**: The folder `Devabhasha_master/` is immutable and read-only. No file within this directory may be modified, renamed, moved, replaced, or deleted under any circumstances.
> 2. **Rule 2 — Historical Authority**: The legacy CD-ROM is the authoritative behavioral and content baseline. Modernization alters presentation and technological implementation, never historical substance.
> 3. **Rule 3 — Zero Content Invention**: Under no circumstance shall an agent invent, interpolate, or extrapolate missing historical content, Sanskrit verses, author commentaries, or biographical details that cannot be proven directly from legacy artifacts.
> 4. **Rule 4 — No Semantic Alteration During Modernization**: Autonomous agents must **never** alter Sanskrit spelling based on personal grammar opinions, change punctuation because it "looks better", rewrite English translations, modify historical biographies, or silently correct apparent historical errors. The source text must be preserved exactly. Any genuine corrections, if ever required, must be documented separately as editorial annotations in metadata.
> 5. **Rule 5 — Unbroken Traceability Chain**: Every migrated asset, verse, image, and behavior must maintain an unbroken, verifiable 6-stage lineage:
>    $$\text{Legacy Source} \longrightarrow \text{Extracted Content} \longrightarrow \text{Converted Asset} \longrightarrow \text{Canonical ID} \longrightarrow \text{Modern UI Component} \longrightarrow \text{Automated Forensic Test}$$

---

## 3. Feature Classification Taxonomy (P / M / E / D)

Every architectural component, screen, user interaction, and data element in this modernization plan carries an explicit classification:

- **`[P]` Preservation** — Existed in the original 1997–2000 CD-ROM; must be reproduced with 100% forensic fidelity.
- **`[M]` Modernization** — Equivalent functional capability as the original, implemented using modern open web standards (HTML5/CSS3/ES6+).
- **`[E]` Enhancement** — New capability not present in the original CD-ROM, introduced to maximize modern usability, accessibility, and discoverability.
- **`[D]` Deferred** — Potential future feature intentionally postponed outside the initial production deliverable.

> [!NOTE]
> **Search Engine Classification Note**: The Sanskrit & Devanagari Search Engine is explicitly classified as a **Modernization Enhancement `[E]`** unless forensic evidence establishes that an equivalent search facility existed in the original Director projector. This prevents agents from conflating modern convenience features with historic baseline behavior.

### Feature Classification Matrix

| Application Module / Feature | Classification | Original 1997 Basis | Modern Implementation |
| :--- | :---: | :--- | :--- |
| **Opening Montage & Calligraphy** | `[P / M]` | `startup.dxr`, `open.cxt`, `montage.avi` | GPU progressive dissolve & Faststart MP4 |
| **10 Thematic Curriculum Chapters** | `[P / M]` | `chapter1.dxr` – `chapter10.dxr`, CXTs | 10-Chapter Responsive Reader & Cards |
| **Master Shlokas Concordance** | `[P / M]` | `shlokas.dxr`, `shlokas.cxt` | Dual-index Browser (by Chapter & Author) |
| **149 Recitation Audio Playback** | `[P / M]` | 149 WAVs in `indexmusic.cxt` | Dual-format 192kbps M4A / MP3 streams |
| **Chapter 2 Interactive Phonetics** | `[P / M]` | `chap2/` 8 SWFs + 46 JPEGs | Interactive SVG vocal tract & audio triggers |
| **Chapter 3 Chitrakavya Puzzles** | `[P / M]` | `chap03/` 21 SWFs + `chess.jpg` | HTML5 Canvas/SVG Chess Knight & Drum |
| **Chapter 4 Scientific Timelines & AI** | `[P / M]` | `chap04/` 19 SWFs + text casts | Interactive HTML5/CSS cards & timelines |
| **3-Way Sanskrit/English Switcher** | `[E]` | Split across separate Director frames | Instant live DOM toggle without audio interruption |
| **Sanskrit Search Engine** | `[E]` | None in original CD-ROM | In-memory inverted index (`js/search.js`) |
| **10-Foot Smart TV Remote UI** | `[M (Secondary)]` | None (fixed 640×480 mouse-only) | Spatial D-pad remote listener (`js/tv-remote.js`) |
| **Progressive Web App (Offline)** | `[M]` | CD-ROM standalone zero-install | Service Worker (`sw.js`) & `manifest.json` |
| **Synchronized Recitation Highlighting**| `[M]` | Manual slide advance in Director | `requestAnimationFrame` + `media.currentTime` |

---

## 4. Target Platforms, Performance Budget & Technology Stack

### Primary Scope (Guaranteed Target Environments)
- **Desktop & Laptop PCs**: Windows, macOS, Linux (via Chrome, Firefox, Safari, Edge)
- **Mobile & Tablet Devices**: Android (Chrome, Firefox) and iOS / iPadOS (Safari)

### Secondary Compatibility Considerations
- **Smart TV Browsers**: Classified as **`[M — Optional/Secondary Target]`**. Dedicated 10-foot UI (`css/tv.css`) with spatial D-pad remote navigation (`js/tv-remote.js`) supporting Arrow keys, Enter/OK, Spacebar, and Escape/Back. Retained for living-room display but must not consume disproportionate implementation resources over desktop/mobile parity.
- **Universal Audio Fallbacks**: Dual-encoded M4A (192kbps AAC-LC) and 192kbps MP3 audio for guaranteed universal playback across all modern and legacy browser runtimes.

### Explicit Performance Budget
To ensure instantaneous loading across global educational environments and low-bandwidth connections, the following performance budget is mandatory:
1. **Initial Payload**: Strictly under **500 KB** uncompressed (HTML + CSS + Core JS).
2. **Render Performance**: First Contentful Paint (**FCP**) < 1.0s; Time to Interactive (**TTI**) < 1.5s on desktop and fast 4G mobile.
3. **Search Index Budget**: Lightweight inverted search index strictly under **250 KB** heap memory upon initialization.
4. **Concurrency Limit**: Maximum of **1 active audio element** and **1 active video element** concurrently; previous streams must be torn down cleanly.
5. **Image Loading**: Native `loading="lazy"` for all chapter canvases and gallery visuals below the viewport.
6. **Offline Precache**: PWA Service Worker precache bundle strictly under **5.0 MB** (core app shell, typography, icons, and opening frames).

### Target Technology Stack
| Layer | Target Standard | Rationale |
| :--- | :--- | :--- |
| **Entry Point** | `index.html` + `run_local.py` | Works via static web server, GitHub Pages, or zero-install Python launcher |
| **UI & Presentation** | Semantic HTML5, Modular CSS3 | CSS Variables, Flexbox, Grid, Fluid Typography |
| **Logic & State** | Vanilla ES6+ JavaScript | Centralized state controller, zero third-party framework overhead |
| **Search Engine** | Client-Side Inverted Index (`js/search.js`) | Devanagari ligature normalization, IAST accent folding, phonetic consonant search |
| **Data Layer** | `content/data.json` mirrored to `js/data.js` | Single source of truth, 100% schema integrity |
| **Audio** | 192 kbps M4A (AAC-LC) + 192 kbps MP3 | Voice clarity, universal browser support |
| **Video** | Faststart MP4 (H.264 / AAC, CRF 18) | Progressive zero-delay streaming, `+faststart` moov atom |
| **PWA & Offline** | Service Worker (`sw.js`) + `manifest.json` | Range-request bypass for audio scrubbing, video passthrough |
| **Visual Assets** | 127 Master Visuals (WebP / JPEG / PNG) | Uncompressed quality preservation |
| **Runtime Prohibitions** | ❌ No Flash, SWF, Ruffle, Director, DXR, CXT, Java | 100% legacy technical debt elimination |

---

## 5. Approved Visual Interface Specifications (Landing Page & Main Screen UI)

The visual design system honors the historic 1997 Sri Aurobindo Society CD-ROM character while upgrading to modern, responsive, high-fidelity web aesthetics. The approved design architecture is modeled directly on the interactive prototype (`devabhasha_interactive_preview.html`) and encompasses two foundational screens:

### Visual Aesthetic & Design Tokens
- **Color Palette**: Sacred, scholarly aesthetic built upon deep sandalwood (`#120c08`), dark teak (`#1e140d`), and antique gold/amber (`#d4af37`) surfaces with glowing brass filigree accents (`rgba(212, 175, 55, 0.35)`).
- **Typography Hierarchy**:
  - Headings & Royal Titles: `Cinzel` / `Cinzel Decorative`
  - Classical Sanskrit Verses & Ligatures: `Tiro Devanagari Sanskrit` / `Noto Serif Devanagari`
  - English Academic Translations & Commentaries: `Georgia` / `Garamond`
- **Animation Dynamics**: Progressive 60fps/120fps GPU dissolves utilizing `transform: translateZ(0)` and `will-change: opacity`, preserving the smooth crossfade behavior of the 1997 Director projector without frame stutter.

---

### Screen 1: The Landing Page (Splash Gateway)
Serves as the cultural entry portal and the browser transient activation gateway required by the Web Audio / Autoplay security policy.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        ॥ ॐ श्री अरविन्दाय नमः ॥                        │
│                ✦ वाग् वै ब्रह्म • Speech is the Supreme Divine ✦         │
│                                                                        │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ ✥                                                            ✥ │   │
│   │                  DEVABHĀṢĀ • देवभाषा                            │   │
│   │             The Language of the Gods                            │   │
│   │       Historic 1997 CD-ROM • Sri Aurobindo Society             │   │
│   │                                                                │   │
│   │   [ S01.jpg ──► S02 ──► S03 ──► S04 ──► S05 ──► S06.jpg ]     │   │
│   │        (Authentic Illuminated Calligraphy GPU Dissolve)        │   │
│   │                                                                │   │
│   │ ✥                                                            ✥ │   │
│   └────────────────────────────────────────────────────────────────┘   │
│                                                                        │
│   [ ▶ प्रवेशः • Play Authentic Opening Montage & Invocations ]         │
│   [            प्रविश्यताम् • Enter Directly ▶               ]         │
│                                                                        │
│   ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌─────────────┐   │
│   │ 10 Chapters  │ │ 149 Audio    │ │ Interactive  │ │ Chitrakāvya │   │
│   │ Curriculum   │ │ Recitations  │ │ Phonetics    │ │ Puzzles     │   │
│   └──────────────┘ └──────────────┘ └──────────────┘ └─────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Sacred Spiritual Crest**: Centered invocation crest featuring `॥ ॐ श्री अरविन्दाय नमः ॥` with the Sri Aurobindo Society gold emblem and the Upanishadic motto: *✦ वाग् वै ब्रह्म • Speech is the Supreme Divine ✦*.
2. **Illuminated Calligraphy Frame**: Framed in an ornate deep-amber radial vignette with brass corner ornaments (`✥`), showcasing the 6-frame illuminated title calligraphy sequence (`S01.jpg` to `S06.jpg`) transitioning smoothly via GPU opacity crossfades. Emblazoned with *DEVABHĀṢĀ • The Language of the Gods* in Cinzel and Devanagari typography.
3. **Dual Action Gateways**:
   - `▶ प्रवेशः • Play Authentic Opening Montage & Invocations`: Launches the full 1997 cinematic sequence (title calligraphy dissolve $\rightarrow$ cultural mosaic $03 \rightarrow 02 \rightarrow 01$ $\rightarrow$ center-cutout 320×240 video player).
   - `प्रविश्यताम् • Enter Directly ▶`: Enables immediate entry into the curriculum portal with audio context pre-primed.
4. **Heritage Scope Badges**: Four responsive preview cards highlighting the 10 Curriculum Chapters, 149 High-Fidelity Recitations, Paninian Grammar & Phonetics, and Chitrakāvya Wordplay Puzzles.

---

### Screen 2: The Main Application Screen (Curriculum Portal & Chapter Reader)
The core pedagogical workspace featuring a responsive three-pane layout:

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ☰  ॐ देवभाषा • Devabhasha    [ देवनागरी | Bilingual / द्विभाषी | English (IAST) ]   🔍 📺 ❓ ⛶  │
├───────────────────┬──────────────────────────────────────────────────────────────────────────────┤
│ ॥ विषयसूची ॥     │ Chapter 1 of 10 • प्रथमोऽध्यायः                               [6 Pages • 1 Audio]│
│                   │ ════════════════════════════════════════════════════════════════════════════ │
│ 01. Language      │ An Extraordinary Language (अपूर्वा देवनिर्मिता भाषा)                          │
│ 02. Grammar       │ "What is language? What is its purpose? How does it communicate?..."         │
│ 03. Chitrakāvya   │                                                                              │
│ 04. Sciences & AI │ ┌──────────────────────────────────────────────────────────────────────────┐ │
│ 05. Poetry (Kāvya)│ │ Verse 1.1: Raghuvaṃśam (Canto 1, Verse 1)             [▶ Listen (श्रूयताम्)] │ │
│ 06. Wisdom        │ │ वागर्थाविव सम्पृक्तौ वागर्थप्रतिपत्तये ।                                  │ │
│ 07. Sacred Mantra │ │ जगतः पितरौ वन्दे पार्वतीपरमेश्वरौ ॥                                       │ │
│ 08. National Link │ │                                                                          │ │
│ 09. Doubts & FAQ  │ │ vāgarthāviva sampṛktau vāgarthapratipattaye ।                            │ │
│ 10. India's Soul  │ │ jagataḥ pitarau vande pārvatīparameśvarau ॥                              │ │
│                   │ │                                                                          │ │
│ ── Concordance ── │ │ Meaning: "For the right comprehension of speech and its meaning,         │ │
│ 📜 Shlokas Index  │ │ I bow down to the parents of the universe, Pārvatī and Śiva..."          │ │
│ 🏛️ Institutions   │ └──────────────────────────────────────────────────────────────────────────┘ │
│                   │                                                                              │
│ [149/149 M4A]     │ ┌─────────────────────────┐  ┌─────────────────────────┐                     │
│                   │ │ Prof. Friedrich Schlegel│  │ Prof. Max Müller        │                     │
│                   │ │ "Clarity and perfection"│  │ "Greatest language..."   │                     │
│                   │ └─────────────────────────┘  └─────────────────────────┘                     │
├───────────────────┴──────────────────────────────────────────────────────────────────────────────┤
│ 🎵 chap1.m4a (192kbps)   ⏮  [▶]  ⏭   0:14 ━━━━●────────────────────────────── 1:48   [1.0x] 🔊 ━━ │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

1. **Top Header Controller**: Persistent top bar containing brand emblem (`ॐ`), title, the **3-Way Sanskrit & English Live Switcher** (`देवनागरी` / `Bilingual द्विभाषी` / `English IAST`) allowing instant script switching without interrupting audio playback, Global Search trigger (`Ctrl+K` or `/`), Smart TV 10-foot UI toggle, Help modal trigger, and Fullscreen toggle.
2. **Docked Curriculum Navigation Sidebar**: Comprehensive table of contents listing all 10 Chapters with verse counts and Sanskrit subheadings, followed by the **Master Shlokas Concordance divider** (providing dual browsing by Chapter 1–10 and by Classical Author: *Kālidāsa, Vālmīki, Vyāsa, Bhartṛhari, Bāṇa, Jayadeva, Kṣemendra, Nārāyaṇa, Śaṅkarācārya*), and links to Sanskrit Institutions, SAS Memorial, and Patrons.
3. **Interactive Study Stage**:
   - Chapter Banner displaying chapter number, title, and historical overview.
   - Recitation Verse Cards featuring Sanskrit text, IAST macrons, English commentary, and one-click recitation triggers (`▶ Listen`).
   - Interactive Phonetics Matrix (Chapter 2) with clickable Paninian consonants (*Ka, Cha, Tta, Ta, Pa*) triggering oral audio.
   - Interactive Chitrakāvya Puzzles (Chapter 3) featuring the 8×8 Chessboard Knight Tour (*Aśva-gati*).
   - World Scholars Testimonials Grid (Schlegel, Max Müller, Will Durant, David Frawley, C.V. Raman, William Jones).
4. **Persistent Floating High-Fidelity Audio Player**: Fixed bottom audio controller displaying track metadata (`chap1.m4a` / 192kbps AAC), central scrubber with continuous waveform progress, play/pause, seek forward/back, speed selector (`0.75x`, `1.0x`, `1.25x`), and volume slider.

---

## 6. Phase-by-Phase Execution Plan with Mandatory Phase Gates

### Phase 0 — Legacy Content Inventory, Architectural Mapping & Workspace Scaffolding
- **Objective**: Perform an exhaustive audit of all legacy assets, logic flows, and dependencies prior to conversion, initialize the `Devabhasha_modern/` directory structure, and generate the formal Legacy Behavior Matrix.
- **Step 0.1 — Workspace Directory Scaffolding**: As the first concrete action of the modernization project, the agent or developer **MUST** create the target project directory `Devabhasha_modern/` at the workspace root alongside `Devabhasha_master/`, and scaffold its standard directory tree:
  ```text
  Devabhasha_modern/
  ├── assets/
  │   ├── audio/
  │   ├── images/
  │   └── video/
  ├── content/
  ├── css/
  ├── js/
  └── tools/
  ```
  All subsequent extraction, transcoding, and coding tasks operate strictly within this directory boundary.
- **Asset Matrix Assembly**: Cataloged every source file across `Devabhasha_master` (415 files total: 149 WAVs, 1 AVI, 124 JPGs, 3 BMPs, 85 SWFs, 19 DXRs, 20 CXTs, 11 Xtras, 2 EXEs).
- **Module Mapping**: Mapped all legacy Director movies and casts to modern semantic components: 10 thematic curriculum chapters (`chapter1` to `chapter10`), `shlokas` master concordance, `devabhasha` main hub, `ashmain`, `startup` launcher, opening choreography, `acknowledge`, `institu`, `sas`, `help`, and `exit` confirmation.
- **Legacy Behavior Matrix**: Create the formal project artifact `LEGACY_BEHAVIOR_MATRIX.md` documenting every legacy Director and Flash feature with explicit columns:
  $$\text{[Legacy Source} \mid \text{Screen/Feature} \mid \text{Trigger} \mid \text{Behavior} \mid \text{Timing} \mid \text{Media} \mid \text{State} \mid \text{Modern Component} \mid \text{Test Verification]}$$
- **Global State Audit**: Documented all global Lingo state variables (`swTitle`, `movieProps`, `soundchanneloop`, `originPoint`, `originMode`, and navigation markers) to establish the centralized modern JavaScript state controller.

> [!IMPORTANT]
> **🔒 Mandatory Completion Gate — Phase 0**: The directory `Devabhasha_modern/` and all core subdirectories must be fully created and verified on disk, and no asset, media track, or behavioral requirement may proceed to conversion or implementation without an established, verified mapping in `LEGACY_BEHAVIOR_MATRIX.md`.

---

### Phase 1 — Audio Modernization & Multi-Parameter Forensic Validation
- **Objective**: Convert raw, high-bandwidth uncompressed `.wav` audio into web-optimized, dual-format `.m4a` and `.mp3` audio streams and perform rigorous forensic validation.
- **Primary Standard**: Encode all 149 voice recitation WAV files (314.26 MB) into AAC-LC in an `.m4a` container at 192 kbps CBR, 44.1 kHz, 16-bit stereo/mono.
- **Special Music & Themes**: Extract internal Director sound effects, chimes, and the master opening theme soundtrack at 256 kbps AAC.
- **Universal Fallback**: Generate parallel 192 kbps MP3 files for all 149 recitation tracks and special audio tracks for guaranteed legacy browser support.
- **Forensic Audio Validation Suite**: Before declaring audio conversion complete, every converted audio file must pass 7 forensic checks:
  1. *Duration match* with source WAV within $\pm 100\text{ ms}$;
  2. *Sample rate* verified at exactly $44,100\text{ Hz}$;
  3. *Channel count parity* (stereo/mono maintained 1-to-1);
  4. *Exact track count parity* (149 recitations + special sound effects);
  5. *Start and end silence* sanity inspection (no audible truncation);
  6. *Digital clipping check* ($\text{true peak} \le -0.5\text{ dBTP}$);
  7. *Source/output waveform sanity check*.
- **Target Directory**: `assets/audio/` (`chap1/`, `chapter2/`, `Chap3/`, `Chap4/`, `Chap5/`, `Chap6/`, `Chap7/`, `Chap10/`, `special/`).

> [!IMPORTANT]
> **🔒 Mandatory Completion Gate — Phase 1**: 100% of the 149 recitation WAVs must have verified dual M4A and MP3 derivatives on disk, passing all 7 forensic validation parameters.

---

### Phase 2 — Video Modernization & Streaming Validation
- **Objective**: Convert legacy `.avi` video sources into universally supported MP4 (H.264 / AAC) video files optimized for instant network streaming.
- **Encoding Pipeline**: Converted opening montage AVI (`Devabhasha_master/media/opening/montage.avi`, 37.66 MB, 320×240, 15fps Indeo 5) to universal MP4 using MPEG-4 AVC / H.264 (CRF 18 visually lossless, `slow` preset, `yuv420p`) with 192 kbps AAC stereo audio.
- **Streaming Optimization**: Applied `-movflags +faststart` flag in FFmpeg to relocate the `moov` atom to the beginning of the MP4 file for zero-delay progressive web streaming.
- **Forensic Video Validation Suite**:
  1. *Total duration match*: 2m 57.47s ($\pm 0.5\text{ s}$);
  2. *Frame rate parity*: exactly 15 fps;
  3. *Resolution parity*: exactly 320×240;
  4. *Total frame count parity*: 2,662 frames;
  5. *Audio stream duration*: 2m 57.47s;
  6. *Video codec verified* as H.264 (`avc1`) / Audio as AAC-LC;
  7. *Atom alignment*: verified `moov` atom positioned before `mdat` atom;
  8. *First and last frame visual comparison* against source AVI.
- **Target Directory**: `assets/video/montage.mp4`.

> [!IMPORTANT]
> **🔒 Mandatory Completion Gate — Phase 2**: Converted MP4 video must play progressively without delay across all browsers and pass all 8 forensic video validation checks.

---

### Phase 3 — Visual & Graphic Asset Extraction & Archival Separation
- **Objective**: Recover raw graphics, UI elements, backdrops, historical portraits, and diagrams from legacy containers while maintaining strict archival separation.
- **Master Visuals Audit**: Preserved and verified all 127 master visuals:
  - 46 Chapter 2 phonetic and anatomical diagrams
  - 20 Chapter 5 poetry canvases
  - 16 Chapter 7 spiritual canvases
  - 12 Chapter 6 wisdom canvases
  - 7 Chapter 1 introduction visuals
  - 6 Chapter 3 chitrakavya diagrams
  - 9 opening sequence frames (`S01–S06`, `01–03`)
  - Historical portraits of world scholars (Schlegel, Max Müller, Will Durant, David Frawley, C.V. Raman, Sir William Jones, Rabindranath Tagore, Jawaharlal Nehru, Mahatma Gandhi, Karl Marx, Friedrich Engels, Adi Shankaracharya)
- **Resolution & Delivery Specification**: The original Windows BMP files (`01.bmp`, `02.bmp`, `03.bmp`) remain immutable in `Devabhasha_master/jpeg/opening/`. Modern web delivery derivatives in JPEG and WebP are generated in `Devabhasha_modern/assets/images/opening/`. We specify: *"Preserves the original 640×480 pixel dimensions; visual fidelity is validated against the source."* Modern lossy/lossless WebP derivatives do not replace the archival master.
- **Forensic Image Validation Suite**:
  1. *Dimension parity* against source bitmap records;
  2. *Aspect ratio preservation*;
  3. *Crop boundary verification*;
  4. *Alpha channel transparency parity*;
  5. *Visual side-by-side inspection*.
- **Target Directory**: `assets/images/` (`chap1/` ... `chap10/`, `opening/`, `acknowledge/`, `sas/`, `institution/`).

> [!IMPORTANT]
> **🔒 Mandatory Completion Gate — Phase 3**: All 127 master visuals and 31 embedded Director `BITD` bitmaps accounted for, validated against source dimensions, and organized in modern delivery paths.

---

### Phase 4 — Flash Vector & Interactive Component Re-engineering (Behavior-First)
- **Objective**: Inspect Flash interactions using emulation and decompilation tools as reference environments, eliminating SWF runtime entirely in production.
- **Behavior-First Doctrine**: Strict operational principle: *"Do not reproduce Flash implementation; reproduce observable behavior."* Agents must inspect Flash MovieClips, identify user-visible behavior and timing, document it in `LEGACY_BEHAVIOR_MATRIX.md`, and implement clean modern HTML5/SVG/Canvas code. Do not perform mechanical ActionScript-to-JavaScript line-by-line translation.
- **Clean HTML5 Reimplementation**:
  1. **Illuminated Drop Caps** (`ldrop`, `ddrop`, `idrop`, `mdrop`, `wdrop`, `tdrop`): Recreated as crisp CSS `initial-letter` and SVG glyphs.
  2. **Chapter 2 Interactive Phonetics**: Vocal tract cross-sections, articulatory organs, and Varga matrices built as responsive SVG charts with interactive audio pronunciation triggers.
  3. **Chapter 3 Chitrakavya Visual Puzzles**:
     - *Chess Knight Tour* (Ashva-gati on 8×8 chessboard from Vedānta Deśika's *Pādukā-sahasram*)
     - *Gomūtrikā* zigzag pattern visualizer
     - *Muraja* drum pattern layout
     - *Sarvatobhadra* magic squares
  4. **Chapter 4 Scientific Heritage**: Baudhayana geometry interactives, Aryabhatta planetary orbits, and ancient medicine timelines rebuilt as semantic HTML/CSS cards.

> [!IMPORTANT]
> **🔒 Mandatory Completion Gate — Phase 4**: All 85 SWF assets decompiled, user-visible behaviors documented, and 100% of interactive components reimplemented in native HTML5/SVG/Canvas without SWF runtime dependencies.

---

### Phase 5 — Native Web Reimplementation & High-Precision Audio Synchronization
- **Objective**: Rebuild Flash and Director interfaces, state logic, and animations using pure HTML5, CSS, and JavaScript with defined, measurable timing tolerances.
- **High-Rate Render Loop**: Implemented `requestAnimationFrame` as the primary 60fps/120fps animation clock for smooth visual updates, transitions, and hover effects.
- **Measurable Synchronization Targets**: Rather than claiming unsubstantiated "millisecond-perfect" synchronization, the application enforces explicit measurable tolerance targets:
  1. *Audio synchronization tolerance*: $\pm 50\text{ ms}$ max drift between audio playback and verse card highlighting;
  2. *Visual transition tolerance*: $\pm 16\text{ ms}$ (within 1 display frame at 60fps);
  3. *Animation timing tolerance*: $\pm 25\text{ ms}$ across dissolves;
  4. *Seek behavior*: card highlighting updates within $100\text{ ms}$ of scrubber release;
  5. *Pause/resume state retention*: exact sample alignment maintained;
  6. *Throttling behavior*: background audio continues smoothly with visual state catching up instantaneously upon tab refocus.

> [!IMPORTANT]
> **🔒 Mandatory Completion Gate — Phase 5**: Audio-visual synchronization verified with measured timing drift strictly within $\pm 50\text{ ms}$ across all recitation tracks.

---

### Phase 6 — Director (DXR / CXT) Migration & Typography Decoding
- **Objective**: Extract assets and translate Lingo logic and typography from protected Macromedia Director files with zero semantic alteration.
- **Typography Decoding**: Built automated decoders (`tools/krutidev_decoder.py` and `tools/vedic_brahma_codec.py`) to translate legacy 8-bit `VedicBrahma2` and `VedicBrahma2 Bold` fonts into standard Devanagari Unicode, and `Palatino-RomanDiac` fonts into academic IAST diacritical macrons (ā, ī, ū, ṛ, ṝ, ḷ, ṅ, ñ, ṭ, ḍ, ṇ, ś, ṣ, ṃ, ḥ).
- **Unresolved Record Handling**: Every extracted legacy text record must either be decoded successfully with 100% verified character parity, or explicitly recorded as `UNRESOLVED_TEXT_RECORD` in migration metadata. Agents are strictly forbidden from guessing, autocorrecting, or smoothing text.

> [!IMPORTANT]
> **🔒 Mandatory Completion Gate — Phase 6**: 100% of extracted text records verified: zero silently altered words, and all unresolved records documented in metadata.

---

### Phase 7 — Technology-Independent Content Layer & Canonical Data Contract
- **Objective**: Decouple all curriculum content, recitation transcripts, treatises, and navigation structure from UI rendering code via a strict data contract.
- **Canonical Data Contract**:
  1. `content/data.json` is the **ONLY** editable canonical source of truth;
  2. `js/data.js` is strictly a generated artifact produced by `tools/sync_data_js.py`;
  3. AI agents and human contributors must **NEVER** manually edit `js/data.js`;
  4. Automated validation `python tools/sync_data_js.py --check` must pass with zero drift before any commit or release.

```text
content/data.json  (Canonical Source of Truth)
       │
       ▼
tools/sync_data_js.py  (--check parity validator)
       │
       ▼
js/data.js  (In-Memory Zero-Install Database for file:/// and HTTP)
```

> [!IMPORTANT]
> **🔒 Mandatory Completion Gate — Phase 7**: `python tools/sync_data_js.py --check` returns exit code 0 (100% parity verified between `content/data.json` and `js/data.js`).

---

### Phase 8 — Web Application Architecture, Dual Execution & Autoplay Gateway
- **Objective**: Assemble the front-end application shell and ensure robust cross-platform execution.
- **Dual Execution Architecture**: Supports both hosted/local web server deployment and direct double-click execution via `file:///` protocol without CORS security exceptions.
- **Zero-Dependency Local Launcher**: Provided `run_local.py` utilizing Python's built-in `http.server` with HTTP/1.1 Range request support for media scrubbing.
- **Autoplay Policy Compliance**: Designed landing page with an explicit user interaction gateway (*"प्रविश्यताम् • Enter Devabhāṣā"*) establishing the transient user gesture context required by modern browsers for unmuted audio/video auto-advancing playback.

> [!IMPORTANT]
> **🔒 Mandatory Completion Gate — Phase 8**: Application loads and navigates cleanly on both `file:///` and local HTTP without CORS blocks, autoplay rejections, or script errors.

---

### Phase 9 — Interactive Feature & Heritage User Experience (UX & Accessibility)
- **Objective**: Recreate all original educational features, navigation menus, and transition effects with first-class accessibility and heritage fidelity.
- **3-Way Sanskrit & English Live Switcher `[E]`**: Instant runtime toggle between Devanagari (देवनागरी), English (IAST), and Bilingual (द्विभाषी) stacked layouts without interrupting audio playback.
- **Authentic Opening Choreography `[P / M]`**: 2-phase cinematic sequence featuring 6-frame illuminated title calligraphy progressive GPU dissolve (`S01–S06`), cultural mosaic transition (`03 -> 02 -> 01`), center-cutout montage video (320×240), and reverse-dissolve outro.
- **Master Shlokas Concordance & Explorer `[P / M]`**: Dedicated explorer with dual indexing (Chapter-wise Index 1–10 and Author-wise Index) with one-click instant audio playback.
- **Dedicated Archival Sections `[P / M]`**: Acknowledgments (`acknowledge.dxr`), User Guide & Help (`help.dxr/swf`), Sanskrit Institutions (`institu.dxr`), Sri Aurobindo Society Memorial (`sas.dxr`), and Artwork Master Gallery featuring all 127 visuals with lightbox inspection.
- **Dedicated Accessibility Architecture (WCAG 2.1 AA)**:
  1. *Semantic HTML*: `<main>`, `<nav>`, `<header>`, `<article>`, `<button>`, `<audio>`, `<video>`;
  2. *Full keyboard navigation*: Tab, Shift+Tab, Enter, Space, Escape;
  3. *Explicit focus indicators*: visible high-contrast `.focus-visible` ring;
  4. *ARIA landmarks and live regions* for dynamic recitation text;
  5. *Screen-reader friendly Sanskrit text* fallbacks;
  6. *Color contrast*: $\ge 4.5:1$ for body text, $\ge 3.0:1$ for large text;
  7. *Reduced-motion support*: `@media (prefers-reduced-motion: reduce)` disabling dissolves and kinetic motion.
- **Smart TV 10-Foot UI `[M — Secondary Target]`**: Integrated 10-foot television mode (`css/tv.css`) with spatial D-pad remote control navigation (`js/tv-remote.js`).

> [!IMPORTANT]
> **🔒 Mandatory Completion Gate — Phase 9**: Every legacy CD-ROM feature has either a modern implementation or a documented intentional exclusion, and accessibility audit passes WCAG 2.1 AA.

---

### Phase 10 — Sanskrit & Devanagari Search Engine `[E — Modernization Enhancement]`
- **Objective**: Implement high-performance, client-side search across all 10 chapters, educational treatises, and shloka recitations as an explicitly classified Modernization Enhancement `[E]`.
- **In-Memory Inverted Index**: Lightweight search index (`js/search.js`) indexing over 300 document fragments and verses in under 200 KB memory upon application load.
- **Linguistic Normalization Pipeline**:
  - Normalizes Devanagari homorganic nasal ligatures before stops (ङ्, ञ्, ण्, न्, म्) into anusvāra (ं)
  - Strips daṇḍas, avagrahas, and metrical markers
  - Decomposes IAST diacritics via Unicode NFD
- **Phonetic Roman Consonant Skeleton**: Matches English phonetic inputs directly to Sanskrit terms (e.g. `chitrakavya` $\rightarrow$ चित्रकाव्य, `panini` $\rightarrow$ पाणिनि).
- **Interactive UI & Deep Linking**: Debounced live query execution (150ms), category filter chips (All, Chapters, Shlokas, Grammar, Scholars), matched text highlighting (`<mark>`), smooth scrolling to target verses with pulsating gold glow, and direct audio playback triggers (`▶ Listen`). Accessible via `/`, `Ctrl+K`, or the top header button.

> [!IMPORTANT]
> **🔒 Mandatory Completion Gate — Phase 10**: Search engine executes queries in $<15\text{ ms}$, consumes $<250\text{ KB}$ heap memory, and accurately matches both phonetic English and Devanagari inputs.

---

### Phase 11 — Progressive Web App (PWA) & Conservative Media Safety
- **Objective**: Implement offline installation capabilities while strictly guaranteeing that Service Worker caches never break media streaming or byte-range scrubbing.
- **Range Request Safety Rule**: Hard operational rule: *"The Service Worker must never interfere with media Range requests."* Any request containing a `Range: bytes=` header strictly bypasses the Service Worker, allowing the browser and server to negotiate HTTP 206 Partial Content byte ranges natively.
- **Video Passthrough**: All `.mp4` video files bypass the Service Worker completely, preserving native hardware decoders and zero-delay streaming.
- **Audio Runtime Cache**: Recitation audio tracks are cached dynamically only upon receiving complete 200 OK responses.
- **Mandatory 8-Point PWA Regression Test Suite**:
  1. *200 OK full audio delivery*;
  2. *206 Partial Content audio seeking/scrubbing*;
  3. *200 OK video metadata*;
  4. *206 Partial Content progressive video streaming*;
  5. *Offline app shell execution*;
  6. *Offline cached audio playback*;
  7. *`file:///` protocol execution without registration errors*;
  8. *HTTP/HTTPS production deployment*.

> [!IMPORTANT]
> **🔒 Mandatory Completion Gate — Phase 11**: Service Worker passes all 8 media Range and offline regression tests with zero playback stalling or cache corruption.

---

### Phase 12 — Evidence-Based Forensic 75-Point Validation & Target Deliverable
- **Objective**: Execute the automated forensic audit suite and conduct comprehensive manual audits to guarantee 100% behavioral and content parity.
- **Evidence-Based Audit Architecture**: Every check in `tools/verify_1to1_mapping.py` must produce verifiable evidence (file hash, waveform analysis, screenshot artifact, or execution log) rather than an unsubstantiated status flag:
  1. **Master Image Assets Audit (127 Master Visuals)**: 12 / 12 CHECKS PASSED (All 124 JPGs + 3 BMPs preserved, dimensions verified, active in UI)
  2. **Master Video Assets Audit (1 MP4 Video)**: 4 / 4 CHECKS PASSED (H.264/AAC faststart MP4 video verified, duration & frame rate confirmed)
  3. **Master Audio Assets Audit (149 Recitations + Special)**: 8 / 8 CHECKS PASSED (All 149 recitations exist in dual M4A/MP3, duration within $\pm 100\text{ ms}$)
  4. **Data Layer Schema & 1-to-1 Mapping Audit**: 15 / 15 CHECKS PASSED (All 10 chapters, shlokas index, biographies, metadata verified)
  5. **UI Implementation & User Interaction Audit**: 20 / 20 CHECKS PASSED (Nav, chapters, audio sync, modals, interactive tools verified)
  6. **Progressive Web App (PWA) Architecture Audit**: 8 / 8 CHECKS PASSED (`sw.js`, `manifest.json`, Range bypass, 8-point regression suite passed)
  7. **Sanskrit & Devanagari Search Engine Audit**: 8 / 8 CHECKS PASSED (Normalization, phonetic index, search UI, deep-linking verified)
- **Mandatory Manual Visual & Behavioral Audit Protocol**: In addition to automated tests, human reviewers conduct a 7-point manual audit:
  1. *Visual fidelity* against 1997 CD-ROM screen captures;
  2. *Devanagari typography* and conjunct ligature rendering;
  3. *Animation smoothness* and dissolve aesthetics;
  4. *Audio synchronization* natural feel;
  5. *Interaction feel* across drop caps and puzzles;
  6. *Responsive layout integrity* across desktop, mobile, and tablet;
  7. *Smart TV D-pad remote navigation* feel.

> [!IMPORTANT]
> **🔒 Mandatory Completion Gate — Phase 12**: **75 / 75 automated checks pass with recorded evidence** AND all 7 manual visual/behavioral audit categories are formally signed off.

---

## 7. Complete Legacy Coverage Matrix

The following matrix serves as the master completeness proof for the entire Devabhāṣā modernization, accounting for every legacy module from source to verification:

| Legacy Module | Source Artifacts | Extracted Content | Converted Asset | Modern Component | Verification Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Opening Sequence** | `startup.dxr`, `open.cxt`, `montage.avi`, `01-03.bmp`, `S01-S06.jpg` | 9 frames, 1 AVI video, Director score | Faststart MP4, progressive JPG/WebP | Opening Choreography Controller (`js/app.js`) | `test_opening_video_and_calligraphy()` |
| **Main Hub & Portal** | `devabhasha.dxr`, `ashmain.dxr`, `navigation.cxt` | Lingo navigation scripts, button casts | JSON chapter routes & state model | DevabhashaHub / Portal Shell (`js/app.js`) | `test_hub_navigation_and_routes()` |
| **Chapter 1: Language** | `chapter1.dxr`, `chapter1.cxt`, `ldrop.swf`, 7 JPGs, 1 WAV | 6 pages text, dropcap, 7 scholar portraits | Unicode Devanagari, IAST, M4A/MP3 | Chapter1Section / Scholar Cards | `test_chapter1_texts_and_audio()` |
| **Chapter 2: Grammar** | `chapter2.dxr`, `chapter2.cxt`, 8 SWFs, 46 JPGs, 14 WAVs | 20 screens, phonetic anatomy, 14 varga WAVs | Interactive SVG vocal tract, 14 M4A/MP3 | Chapter2Section / Phonetic Explorer | `test_chapter2_phonetics_and_audio()` |
| **Chapter 3: Chitrakavya** | `chap03.dxr`, `chap03.cxt`, 21 SWFs, 6 JPGs, 33 WAVs | 15 pages, knight tour, drum, 33 WAVs | HTML5 Canvas Knight Tour, 33 M4A/MP3 | Chapter3Section / Chitrakavya Puzzles | `test_chapter3_puzzles_and_audio()` |
| **Chapter 4: Sciences** | `chap04.dxr`, `chap04.cxt`, 19 SWFs, 5 WAVs | 17 pages, Baudhayana, AI text, 5 WAVs | HTML5 timeline cards, 5 M4A/MP3 | Chapter4Section / Sciences & AI | `test_chapter4_timelines_and_audio()` |
| **Chapter 5: Poetry** | `chapter5.dxr`, `chapter5.cxt`, 1 SWF, 20 JPGs, 31 WAVs | 19 pages, kavya trinity, 31 poetry WAVs | 20 backdrops, 31 M4A/MP3 recitations | Chapter5Section / Poetry Reader | `test_chapter5_poetry_and_audio()` |
| **Chapter 6: Wisdom** | `chapter6.dxr`, `chapter6.cxt`, 1 SWF, 12 JPGs, 22 WAVs | 9 pages, subhashitas, 22 wisdom WAVs | 12 backdrops, 22 M4A/MP3 recitations | Chapter6Section / Subhashita Reader | `test_chapter6_wisdom_and_audio()` |
| **Chapter 7: Spiritual** | `chapter7.dxr`, `chapter7.cxt`, 1 SWF, 16 JPGs, 40 WAVs | 15 pages, Vedas, Gita, 40 mantra WAVs | 16 backdrops, 40 M4A/MP3 recitations | Chapter7Section / Sacred Reader | `test_chapter7_mantras_and_audio()` |
| **Chapter 8: National** | `chap08.dxr`, `chap08.cxt`, 9 SWFs, 1 JPG | 8 pages, linguistic affinity charts | Interactive linguistic comparison cards | Chapter8Section / National Language | `test_chapter8_linguistic_charts()` |
| **Chapter 9: Doubts** | `chapter9.dxr`, `chapter9.cxt`, 5 SWFs, 2 JPGs | 5 pages, secular architecture, Jones | Interactive FAQ / Scholar Cards | Chapter9Section / Doubts & Answers | `test_chapter9_faq_and_scholars()` |
| **Chapter 10: Soul** | `chapter10.dxr`, `chapter10.cxt`, 8 SWFs, 2 JPGs, 3 WAVs | 8 pages, national mottos, 3 WAVs | 2 backdrops, 3 M4A/MP3 recitations | Chapter10Section / India's Soul | `test_chapter10_soul_and_audio()` |
| **Master Shlokas** | `shlokas.dxr`, `shlokas.cxt`, 3 SWFs | Dual index (by Chapter & by Author) | Canonical shlokas JSON index | ShlokasConcordanceExplorer (`js/app.js`) | `test_shlokas_concordance_parity()` |
| **Acknowledgments** | `acknowledge.dxr`, `acknowledge.cxt`, `back.jpg` | Patrons and contributors text, back.jpg | Modern acknowledgment card & backdrop | AcknowledgeSection (`js/app.js`) | `test_acknowledgments_screen()` |
| **Institutions** | `institu.dxr`, `institu.cxt`, `institution .jpg` | Participating Sanskrit institutions text | Modern institution directory card | InstitutionSection (`js/app.js`) | `test_institutions_screen()` |
| **SAS Memorial** | `sas.dxr`, `sas.cxt`, `sas.jpg` | Sri Aurobindo Society historical office text | Modern memorial card & photo backdrop | SasSection (`js/app.js`) | `test_sas_memorial_screen()` |
| **Help & User Guide** | `help.dxr`, `help.cxt`, `help.swf` | Multimedia navigation guide text | Modal Help Guide & Keyboard Reference | HelpModal (`js/app.js`) | `test_help_modal_and_shortcuts()` |
| **Exit Screen** | `exit.dxr`, `exit.jpg` | Exit confirmation prompt, `exit.jpg` | Clean exit overlay / restart modal | ExitModal (`js/app.js`) | `test_exit_confirmation_screen()` |

---

## 8. Production Deliverable Directory Structure

```text
Devabhasha_modern/
├── index.html              # Modern web entry point, autoplay gateway & search modal
├── manifest.json           # Web App Manifest (for HTTPS/PWA deployment)
├── sw.js                   # Conservative Service Worker (Range-request & video passthrough)
├── run_local.py            # Zero-dependency local HTTP launcher (Range-request enabled)
├── LEGACY_BEHAVIOR_MATRIX.md # Master 1-to-1 reverse-engineering behavior specification
├── css/
│   ├── main.css            # Responsive CSS design system, typography & search modal
│   ├── player.css          # Recitation cards, speaker badges & audio scrubber
│   └── tv.css              # Smart TV 10-foot UI & spatial focus styling
├── js/
│   ├── app.js              # Modular ES6 JavaScript application logic & routing
│   ├── search.js           # Sanskrit & Devanagari Search Engine (Phase 10 [E])
│   ├── player.js           # High-precision audio player (requestAnimationFrame sync)
│   ├── tv-remote.js        # Smart TV remote control & keyboard D-pad listener
│   └── data.js             # Mirrored JSON database (all 10 chapters & shlokas)
├── content/
│   └── data.json           # Canonical single source of truth database (ONLY editable source)
├── assets/
│   ├── icons/              # Standard PWA icons (192, 512, maskable, apple-touch)
│   ├── images/             # 127 master historical visuals, backdrops & calligraphy
│   │   ├── chap1/ ... chap10/   (Chapter canvases, phonetic & grammar charts)
│   │   ├── opening/             (S01-S06 title frames, 01-03 mosaic frames)
│   │   ├── acknowledge/         (back.jpg, backup.jpg, backdn.jpg)
│   │   └── sas/, institution/, exit.jpg
│   ├── audio/              # 149 M4A + 149 MP3 recitation tracks + special sound tracks
│   │   ├── chap1/ ... chap10/
│   │   └── special/
│   └── video/              # Faststart H.264 MP4 opening video
│       └── montage.mp4
└── tools/
    ├── sync_data_js.py     # Canonical parity validator & database synchronizer
    ├── vedic_brahma_codec.py # VedicBrahma2 to Unicode Devanagari converter
    └── verify_1to1_mapping.py # Automated 75-point evidence-based forensic audit suite
```

---

## 9. Final Dependency Exclusion Checklist

The final production release contains zero legacy technical debt:
- ❌ No Flash / `.swf` files
- ❌ No Ruffle runtime in production
- ❌ No ActionScript code
- ❌ No Director `.dxr` / `.cxt` files
- ❌ No Shockwave plugin wrappers
- ❌ No Java Applets or JRE requirements
- ❌ No proprietary 8-bit typewriter fonts (`VedicBrahma2` / `VedicBrahma2 Bold`)
- ❌ No uncompressed 16-bit PCM WAV audio
