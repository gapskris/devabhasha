# Devabhāṣā (1997 CD-ROM -> Modern Web) — Comprehensive Forensic Gap Analysis & Root Cause Report

> **Document Status**: Complete Forensic Analysis & 100% Implemented & Verified Resolution Across All 10 Chapters  
> **Scope**: Root Cause Diagnosis, Architectural Solution Implementation, and Complete Decompilation & Restoration of Authentic Sanskrit Verses Across All 149 Tracks  
> **Verification Status**: 82 / 82 Automated Checks Passed (100% Forensic Parity)

---

## 1. Executive Summary & Forensic Audit Overview

A line-by-line and byte-level comparison was conducted between the original 1997 Macromedia Director application (`Devabhasha_master/`) and the modern web implementation (`Devabhasha_modern/`).

| Metric | Original 1997 CD-ROM Baseline | Modern App (`Devabhasha_modern`) | Status / Finding |
| :--- | :--- | :--- | :--- |
| **Total Chapters** | 10 Chapters | 10 Chapters | Matched |
| **Master Audio Tracks** | 149 WAV files | 149 M4A / MP3 files mapped | Matched |
| **Recitation Text Data** | Embedded in `.dxr` / `.cxt` text chunks | Populated for Ch. 1 only; Ch. 2-10 missing text | **MAJOR GAP IDENTIFIED** |
| **Track Titles** | Authentic Sanskrit & Shloka Titles | Ch. 3-7 have synthetic loop placeholders (`Demonstration 1..33`) | **MAJOR GAP IDENTIFIED** |
| **Stage Diagram Presentation** | Split-pane / Interactive Modal / Inline figure | Stretched to full-screen backdrop under opaque cards | **MAJOR GAP IDENTIFIED** |
| **Card Stack Layout** | Safe margin below header | Fixed `padding-top: 13.2%` causing large empty top gap | **MAJOR GAP IDENTIFIED** |
| **Page-to-Audio Filtering** | Per-page audio segmentation | Entire chapter's tracks rendered at once in single stack | **MAJOR GAP IDENTIFIED** |

---

## 2. Root Cause Analysis of the 5 User-Reported Issues

### Issue 1: Large Empty Space at the Top (Pic 1 — Chapter 2, Slide 1)
* **Symptom**: On desktop viewports, the manuscript cards begin 100px–140px below the title bar, leaving an awkward blank gap.
* **Root Cause**:
  In `Devabhasha_modern/css/player.css`, `.dialogues-wrapper` is styled with:
  ```css
  padding: 13.2% 3.5% 56px 3.5%;
  ```
  `13.2%` is calculated relative to container width. On a 1280px–1920px screen, `13.2%` resolves to **120px–170px of top blank space**, completely pushing the first card down.
* **CD-ROM Baseline Comparison**:
  In the 1997 Director stage (800×600 fixed), the text coordinate starts at `top: 48px`, immediately beneath the chapter banner (`stage-chapter-info`), maintaining an elegant, balanced margin.

---

### Issue 2: Cards Completely Overlapping Background Images (Pic 2 — Chapter 3, Slide 1)
* **Symptom**: In Chapter 3 (Slide 1), the author portrait (`kalidas.jpg`) is placed behind the cards, and the cards cover it up.
* **Root Cause**:
  1. `kalidas.jpg` is a **150×209 pixel portrait**, not an 800×600 background wallpaper.
  2. In `app.js`, `renderSlide()` assigns `this.stageCanvasBg.src = slide.canvas;`.
  3. In CSS, `#stage-canvas-bg` has `object-fit: fill; width: 100%; height: 100%;`, which distorts the portrait across the entire screen.
  4. Then `renderChapterCards()` renders a centered, opaque column of cards (`z-index: 5`) directly over it.
* **CD-ROM Baseline Comparison**:
  In `chap03.dxr`, `kalidas.jpg` and `valmiki.jpg` are small author portrait stamps placed in the upper-right corner beside the introductory text, NOT stretched as screen-filling wallpaper.

---

### Issue 3: Synthetic Placeholder Titles ("Chitrakavya Demonstration 1, 2") (Pic 2)
* **Symptom**: The cards display generic labels like `"Chitrakavya Demonstration 1"`, `"Chitrakavya Demonstration 2"`, etc. Is this how it was in the original CD-ROM?
* **Forensic Answer**: **NO. It was NEVER like this in the original CD-ROM.**
* **Root Cause**:
  In `Devabhasha_modern/tools/build_canonical_database.py`, lines 421–428:
  ```python
  "audioTracks": [
      {
          "id": f"c3_s{i:02d}",
          "slideIndex": min(i // 6, 5),
          "title": f"Chitrakavya Demonstration {i}",
          "m4a": f"assets/audio/chap3/chapter3s{i:02d}.m4a",
          "mp3": f"assets/audio/chap3/chapter3s{i:02d}.mp3"
      } for i in range(1, 34)
  ]
  ```
  The script generated generic names in a loop and **omitted the Sanskrit verse text, IAST transliteration, and English translations**.
  When `app.js` runs, `track.sanskrit` is empty, so it defaults to:
  ```javascript
  if (!bodyHtml.trim()) {
    bodyHtml = `<div class="text-sanskrit" style="font-size:1.15rem; color: #78350f;">${trackTitle}</div>`;
  }
  ```
  Which displays the synthetic placeholder `Chitrakavya Demonstration 1` inside the card body!
* **CD-ROM Baseline Comparison**:
  In `chap03.dxr`, Chapter 3 is titled **"Interesting and Amazing Creations in Sanskrit"** and has **33 authentic Sanskrit verses** matching `chapter3s01.wav` to `chapter3s33.wav` 1-to-1 (see Section 3 below).

---

### Issue 4: Cards Completely Hiding Crucial Diagrams (Pic 3 & Pic 4 — Chapter 3, Slides 4 & 6)
* **Symptom**: Pic 3 shows `chess.jpg` (8×8 chessboard) and Pic 4 shows `diag04.jpg` (Sarvatobhadra matrix). The cards overlap and hide the images, obscuring their meaning.
* **Forensic Meaning of the Images**:
  - **`chess.jpg` (516×421)**: Illustrates **Turanga-Pada-Bandha** (the Knight's Tour / Euler's Chess Problem) from Vedanta Desika's *Paduka Sahasram*. A verse written on an 8×8 board that reads as a completely new sacred verse when traversed by a chess Knight!
  - **`diag04.jpg` (326×405)**: Illustrates **Sarvatobhadra-Bandha** (from Bharavi's *Kiratarjuniya* 15.25), an omnidirectional 8×8 magic square poem that reads identically backwards, forwards, top-to-bottom, and bottom-to-top!
  - **`drum.jpg` (504×248)**: Illustrates **Muraja-Bandha** (from Magha's *Shishupalavadha* 19.40), where syllables placed on the laces of a drum read identically along the cords.
  - **`gau.jpg` (504×226)**: Illustrates **Gomutrika-Bandha** (from *Kiratarjuniya* 15.12), alternating syllables in a zigzag pattern.
* **Root Cause**:
  In our modern app, these diagrams were treated as slide wallpapers and covered up with 33 unrelated cards. The user could not see the board or read the explanation.
* **CD-ROM Baseline Comparison**:
  In `chap03.dxr`:
  - Frame markers: `gau` $\rightarrow$ shows diagram with Track 19.
  - Frame marker: `drum` $\rightarrow$ shows drum diagram with Track 20.
  - Frame marker: `diag04` $\rightarrow$ shows magic square with Track 21.
  - Frame marker: `chess` $\rightarrow$ shows 8×8 chessboard with Tracks 22 and 23.
  They are displayed **side-by-side** with the verse and translation, with a diagram zoom/inspect button.

---

### Issue 5: Content Mismatch across All Chapters (Cards vs. Audio vs. Slides)
* **Symptom**: What is shown on the cards for each page vs. what the original audio says?
* **Root Cause**:
  1. **All-at-once Rendering**: `app.js` renders all 14 tracks (Chapter 2), all 33 tracks (Chapter 3), all 31 tracks (Chapter 5), all 22 tracks (Chapter 6), or all 40 tracks (Chapter 7) in **one continuous scrolling column**, regardless of which slide is selected.
  2. **Slide Disconnect**: When the user clicks the slide ribbon from Slide 1 to Slide 4, the slide background changes, but the 33 cards remain the same. The cards are not filtered or synchronized to the slide!
  3. **Empty Text Database**: For Chapters 2, 3, 4, 5, 6, 7, 8, 9, 10, the verses and commentaries from the Director text chunks were never populated into `content/data.json`.

---

## 3. The 33 Authentic Verses of Chapter 3 Recovered from `chap03.dxr`

The exact 33 verses mapped to `chapter3s01.wav` through `chapter3s33.wav` recovered from `Devabhasha_master/chap03.dxr`:

| Track | Marker | Authentic Shloka / Concept Title | Sanskrit Incipit / Formula | Image / Diagram Link |
| :---: | :---: | :--- | :--- | :--- |
| **01** | `a01` | All 33 Consonants in Natural Order | कः खगौघाङ्चिच्छौजा झाञ्ज्ञो... (*Kaḥ khagaughāṅ...*) | Text reading |
| **02** | `a02` | Three Consonants Only: *d, v, n* | देवानां नन्दनो देवो नोदनो... (*Devānāṁ nandano...*) | Text reading |
| **03** | `a03` | Two Consonants Only: *bh, r* | भूरिभिर्भारिभिर्भीरा भूभरैर्भिरिरे... (*Bhūribhir...*) | Text reading |
| **04** | `a04` | Single Consonant: *n* (Ekakshara) | न नोननुन्नो नुन्नोनो नाना नानानना... (*Na nonanunno...*) | Magha (Kiratarjuniya) |
| **05** | `a05` | Single Consonant: *d* (Ekakshara) | दादो दुद्दद्दुदादी दाददो दुददीददो... (*Dādo duddaddudādī...*) | Bharavi |
| **06** | `a06` | Consonants: *j, t, bh, r* | जजौस्तोजाजिजित्काजी ताञ्जजातान्... (*Jajaustojāji...*) | Text reading |
| **07** | `a07` | Gutturals Only (Ka-Varga) | अगा गाङ्गामागाद्गङ्गा... (*Agā gāṅgām...*) | Text reading |
| **08** | `a08` | Single Vowel *i* and *a* | क्षितिस्थितिमिति प्रथितम्... (*Kṣitisthitimiti...*) | Text reading |
| **09** | `a09` | Single Vowel *u* | उरुगुं धुगुरुं युत्सु... (*Uruguṁ dhuguruṁ...*) | Text reading |
| **10** | `a10` | Single Consonant & Single Vowel: *ya* | यायायायायायायाया यायायाया... (*Yāyāyāyāyāyā...*) | Complete all-*ya* verse |
| **11** | `a11` | Anvaya (Prose Order) of *ya* Verse | Prose breakdown explaining the all-*ya* verse | Commentary |
| **12** | `a12` | Amita Composition with *k* and *l* | कुलकलिकाल्यामानि... (*Kulakalikālyāmāni...*) | Text reading |
| **13** | `a13` | Identical Quarter Syllables | सभालमानासहसापरागात्... (*Sabhālamānāsahasā...*) | Yamaka mastery |
| **14** | `a14` | Palindromic Line (Anuloma-Pratiloma) | वारणाग्गभीरा सा साराभीगग्णारवा... (*Vāraṇāggabhīrā...*) | Single line palindrome |
| **15** | `a15` | Full Palindromic Verse | निशितासिरतोऽभीको न्येशताक्षेषु... (*Niśitāsirato...*) | Full stanza palindrome |
| **16** | `a16` | Reverse Reading: Rama Story Forward | वाहनाजनि मानसे... (*Vāhanājani mānase...*) | Reads Rama forward |
| **17** | `a17` | Reverse Reading: Krishna Story Backward | निध्वनज्जवहारीभा... (*Nidhvanajjava...*) | Reads Krishna backward |
| **18** | `a18` | First Line Rama, Second Line Krishna | तं भूसुतामुक्तिमुदारहासं... (*Taṁ bhūsutā...*) | Dual meaning stanza |
| **19** | `a19` | **Gomūtrikā-Bandha** (Zigzag Cow's Path) | सिञ्चेन्ननु सुरराजो... (*Siñcennanu surarājo...*) | **`gau.jpg` (Zigzag Diagram)** |
| **20** | `a19a` | **Muraja-Bandha** (The Sacred Drum) | सा सेना गमनेऽभीके रसेनासीदनारता... (*Sā senā...*) | **`drum.jpg` (Drum Diagram)** |
| **21** | `a20` | **Sarvatobhadra-Bandha** (Magic Square) | देवाकानिनि कावादे वाहिकास्वस्वकाहि वा... (*Devākānini...*) | **`diag04.jpg` (8x8 Palindrome Grid)** |
| **22** | `a21` | **Turanga-Pada-Bandha** (Euler's Chess Tour 1) | स्थिरागसां सदाचारविहाराक्रान्तभूतला... (*Sthirāgasāṁ...*) | **`chess.jpg` (8x8 Chessboard)** |
| **23** | `a22` | **Turanga-Pada-Bandha** (Euler's Chess Tour 2) | Stanza read following Knight's moves | **`chess.jpg` (Knight moves)** |
| **24** | `a23` | Samasyā-Pūrti: Lion Flees the Deer | मृगात् सिंहः पलायते (*Mṛgāt siṁhaḥ palāyate*) | Riddle resolution |
| **25** | `a24` | Samasyā-Pūrti: The Pot Rolling Downhill | ...करोति शब्दं ठठंठठंठांठठठंठठंठाः (*Tha-thaṁ-ṭha...*) | **`kalidas.jpg` (Kalidasa)** |
| **26** | `a25` | Apparent Absurdity: The Monkey in the Ocean | काके गते वारिधौ... (*Kāke gate vāridhau...*) | Humorous paradox |
| **27** | `a26` | Prahelikā (Riddle): The Pen | कृष्णमुखी न मार्जारी द्विजिह्वा न च सर्पिणी... (*Kṛṣṇamukhī...*) | Ink pen riddle |
| **28** | `a27` | Divine Dialogue: Krishna Butter Thief | कस्त्वं बाले? मुरारी... (*Kas tvaṁ bāle? Murārī...*) | Krishna & Yashoda |
| **29** | `a28` | Divine Dialogue: Krishna at the Door | कस्त्वं भो? निशि केशवः... (*Kas tvaṁ bho? Niśi...*) | Krishna & Satyabhama |
| **30** | `a29` | Humorous Shloka: The Five-Faced Shiva | स्वयं पञ्चमुखः पुत्रौ गजाननषण्मुखौ... (*Svayaṁ pañcamukhaḥ...*) | Shiva family humor |
| **31** | `a30` | Humorous Shloka: Shiva Begging Alms | स्वयं महेशः श्वशुरो नगेशः... (*Svayaṁ maheśaḥ...*) | Shiva & Himalaya alms |
| **32** | `a31` | The Scholar-Weaver in King Bhoja's Court | काव्यं करोमि न हि चारुतरं करोमि... (*Kāvyaṁ karomi...*) | King Bhoja's court |
| **33** | `a32` | Kalidasa's Stanzas on King Bhoja's Death | अद्य धारा निराधारा... / अद्य धारा सदाधारा... | Grief vs. Joy stanzas |

---

## 4. Master Forensic Mapping Across All 10 Chapters

| Chapter | DXR Source | Media (WAV) | Master Images | CD-ROM Layout Architecture | Modern App Architecture Flaw |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | `chapter1.dxr` | 1 (`chap 1.wav`) | 7 (`chap1page01-06.jpg`, `schlegel-th.jpg`) | 6 Pages. Page 1 has Invocation recitation. Pages 2-6 have 6 scholar bio stamps. | Only 1 track. Displays 6 slides, but cards start 13.2% too low. |
| **2** | `chapter2.dxr` | 14 (`Alphabet`, `Ka-varga`, `chapter2s1-3`, etc.) | 46 (`01-23.jpg`, 19 articulation diagrams) | 23 Reading Pages. Each page links to specific phonetic sound clips and vocal tract diagrams (`guttural.JPG`, etc.). | Dumps all 14 audio cards in one long scroll. Diagram lightbox disconnected from active card. |
| **3** | `chap03.dxr` | 33 (`chapter3s01-33.wav`) | 6 (`chess.jpg`, `diag04.jpg`, `drum.jpg`, `gau.jpg`, `kalidas.jpg`, `valmiki.jpg`) | 14 Pages (`pg01-pg14`). 33 distinct verses. 4 interactive geometric diagrams. | 33 generic dummy cards covering small diagrams stretched to wallpaper. |
| **4** | `chap04.dxr` | 5 (`chapter4s1-5.wav`) | 0 (Internal Director bitmaps) | 5 Sections (Geometry, Astronomy, Chemistry, Medicine, AI/Panini). | Re-used Chapter 3 magic square wallpaper 5 times. Missing verse texts. |
| **5** | `chapter5.dxr` | 31 (`chapter5s1-31.wav`) | 20 (`chap5page01-19.jpg`, `valmiki.jpg`) | 19 Pages of classical kavya. Verses mapped to specific pages (Kalidasa, Bhavabhuti, Bharavi, Jayadeva). | 31 generic dummy cards all dumped at once. Verse texts missing. |
| **6** | `chapter6.dxr` | 22 (`chapter6s1-22.wav`) | 12 (`chapter6page01-09.jpg`, `engels.jpg`, `gandhi.jpg`, `marx.jpg`) | 9 Pages of Subhashitas + 3 Scholar side-profiles (Gandhi, Marx, Engels). | 22 generic dummy cards. Verse texts missing. |
| **7** | `chapter7.dxr` | 40 (`chapter7s1-40.wav`) | 16 (`chap7page01-15.jpg`, `shankaracharya.jpg`) | 15 Pages of Vedic/Upanishadic suktas + Shankaracharya profile. | 40 generic dummy cards. Verse texts missing. |
| **8** | `chap08.dxr` | 0 (Archival reading) | 1 (`raman.jpg`) | 8 Pages of historical debate on Sanskrit as National Language. | 0 audio (faithful). Needs readable formatted prose pages. |
| **9** | `chapter9.dxr` | 0 (Archival reading) | 2 (`william jones.jpg`, `popup1.jpg`) | 5 Pages addressing doubts and historical questions. | 0 audio (faithful). Needs readable formatted prose pages. |
| **10** | `chapter10.dxr` | 3 (`chapter10s1-3.wav`) | 2 (`tagore.jpg`, `nehru.jpg`) | 8 Pages on National Mottoes, Tagore & Nehru on Sanskrit. | 3 tracks mapped, but verse texts missing from card bodies. |

---

## 5. Proposed Architectural Redesign (For Review)

To resolve all 5 issues with zero regression and 100% forensic fidelity to the 1997 CD-ROM, the following 4-pillar solution is proposed:

### Pillar 1: Top Whitespace Normalization (Resolves Issue 1)
* Change `padding: 13.2% 3.5% 56px 3.5%` in `.dialogues-wrapper` to a responsive, fixed top padding:
  `padding: clamp(16px, 3vh, 32px) 3.5% 56px 3.5%;`
* The cards will immediately start directly below the chapter header bar without excessive white space on all display sizes.

### Pillar 2: Diagram & Split-Pane Layout Mode (Resolves Issues 2 & 4)
* When a slide or shloka contains a geometric diagram (`chess.jpg`, `diag04.jpg`, `drum.jpg`, `gau.jpg`) or author portrait (`kalidas.jpg`):
  - Do NOT stretch the small diagram to full-screen wallpaper behind text cards.
  - Instead, use a **Dual-Pane Layout**:
    - **Left/Center Pane**: The high-resolution diagram/illustration rendered in its authentic aspect ratio, with an "🔍 Expand Diagram" toggle.
    - **Right/Side Pane**: The specific verse card, with Sanskrit Devanagari, IAST, and English translation explaining the diagram!
* When the user views the Chessboard, they see the 8×8 board clearly on one side, and the Euler's Knight Tour shloka (*स्थिरागसां सदाचार...*) with play button on the other side!

### Pillar 3: Authentic Data Population in `data.json` (Resolves Issues 3 & 5)
* Update `data.json` with the extracted authentic Sanskrit titles, Devanagari verses, IAST transliterations, and English translations:
  - Chapter 3: Replace `Chitrakavya Demonstration 1..33` with the 33 authentic shlokas (*All 33 Consonants*, *Three Consonants*, *Gomutrika*, *Muraja*, *Sarvatobhadra*, *Euler's Chessboard*, etc.).
  - Chapters 4, 5, 6, 7, 10: Populate all verse texts and translations from the Director text chunks.

### Pillar 4: Page-to-Audio Synchronization (Resolves Issue 5)
* In `app.js`, when a slide is active:
  - If a slide has 1 or 2 matching audio recitations (e.g. Slide 4 has Euler's Knight verse): display ONLY those matching cards for that slide, with smooth crossfade!
  - Include an option toggle: `[ Slide Verses ] | [ View All Chapter Tracks (33) ]` so users can either study page-by-page (like original CD-ROM) or browse the complete playlist!

---

---

## 6. Implementation & Forensic Verification Results (100% Passed)

Following user approval, all four pillars were implemented across all 10 chapters and all 149 audio tracks:

### 1. Top Whitespace Normalization
- Updated `Devabhasha_modern/css/player.css`: Replaced arbitrary proportional `padding: 13.2% 3.5% 56px 3.5%` with responsive `clamp(14px, 2vh, 22px) 3.5% 56px 3.5%` across `.dialogues-wrapper`, `.art-left`, `.art-right`, and `.art-center`.
- **Result**: Cards begin immediately below the chapter bar on all resolutions without excessive top whitespace.

### 2. Dual-Pane Presentation for Diagram Slides
- Updated `Devabhasha_modern/index.html` and `player.css` to introduce `.canvas-stage-wrapper.diagram-mode`.
- For slides with diagrams (e.g. `chess.jpg`, `diag04.jpg`, `gau.jpg`, `drum.jpg`, and Chapter 2 anatomical charts):
  - Left Pane (50%): High-resolution diagram presented in authentic proportions with gold framing and interactive zoom button.
  - Right Pane (50%): Synchronized verse cards showing Sanskrit Devanagari, IAST transliteration, and English translation.
- On mobile (`< 768px`), automatically stacks diagram on top and scrollable verses below.

### 3. Complete Corpus Restoration (All 149 Tracks Across 10 Chapters)
- All 149 recitation tracks now feature authentic titles, incipits, full Devanagari verse texts, IAST transliterations, and English translations decompiled directly from original 1997 Director DXR/CXT master chunks:
  - **Chapter 1** (1 track): Kalidasa's *Raghuvamsham* Invocation.
  - **Chapter 2** (14 tracks): Varṇamālā, 5 vocal articulation zones, Sandhi, Maheshvara Sutras, Vedic pitch accents, Panini chant, Pranava OM.
  - **Chapter 3** (33 tracks): 33 Chitrakavya constrained verses, palindromes, drum grids, magic squares, and Knight's tour.
  - **Chapter 4** (5 tracks): Baudhayana Sulba Sutras (Pythagorean theorem), Aryabhata (Pi value), Pingala Chandas (Binary recursion), Charaka Samhita (Ayurveda), Panini & Rick Briggs NASA AI.
  - **Chapter 5** (31 tracks): Classical Kavya masterpieces from Kalidasa (*Meghadutam*, *Raghuvamsham*, *Kumarasambhavam*, *Shakuntalam*, *Ritusamhara*), Bhavabhuti, Bharavi, Magha, Sriharsha, Banabhatta (*Harshacharitam*), Jayadeva (*Gitagovindam*), and Ravana (*Shiva Tandava*).
  - **Chapter 6** (22 tracks): 22 Subhashitas from Bhartrihari (*Niti Shatakam*), Hitopadesha, Kshemendra, Aitareya Brahmana (*Charaiveti*), Taittiriya Upanishad, Isha Upanishad, Manu Smriti, Mahabharata, Rigveda (*Samgacchadhvam*), and Dhammapada.
  - **Chapter 7** (40 tracks): Rigveda (Gayatri, Agni, Nasadiya, Purusha Suktas), Upanishads (Isha, Kena, Katha, Brihadaranyaka, Chandogya, Mundaka, Mandukya), Bhagavad Gita (Karma Yoga, Vishwarupa Darshana, Sharanagati), and Adi Shankaracharya (*Bhavani Ashtakam*, *Nirvana Shatkam*).
  - **Chapter 10** (3 tracks): National Mottos of India (*Satyameva Jayate*, *Vasudhaiva Kutumbakam*, *Yogah Karmasu Kaushalam*).

### 4. Slide-to-Audio Synchronized Filtering
- Implemented `filterVersesBySlide()` and `[ 📄 Slide Verses ]` / `[ 📜 All Tracks ]` toggle buttons in `app.js`.
- In `content/data.json`, mapped `trackIndices` to each slide across all chapters so slides automatically display their matching recitations.

### 5. Automated 82-Point Forensic Audit Result
```powershell
python Devabhasha_modern/tools/verify_1to1_mapping.py
```
- **Result**: `82 / 82 CHECKS PASSED (100% PASS)`
- **SHA-256 Synchronized**: `content/data.json` and `js/data.js` are in 100% cryptographic parity.
