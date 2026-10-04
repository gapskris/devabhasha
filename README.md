# Devabhāṣā — The Wonder that is Sanskrit (देवभाषा)

[![Verification Audit](https://img.shields.io/badge/Forensic%20Audit-82%2F82%20PASS%20(100%25)-success?style=for-the-badge&logo=checkmarx)](AUDIT_REPORT.md)
[![Zero Runtime Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Vanilla%20ES6%2B)-blue?style=for-the-badge)](index.html)
[![PWA Ready](https://img.shields.io/badge/PWA-Offline%20Ready-purple?style=for-the-badge&logo=pwa)](manifest.json)
[![Platform](https://img.shields.io/badge/Platform-Web%20%7C%20Mobile%20%7C%20Smart%20TV-gold?style=for-the-badge)](index.html)

A modern, universal Progressive Web Application (PWA) preserving and presenting the landmark multimedia cultural heritage project **"Devabhāṣā — The Wonder that is Sanskrit"**, originally produced in **1997** by the **Sri Aurobindo Society** and participating national Sanskrit academies.

Forensically reverse-engineered from the original 1997 Macromedia Director CD-ROM (`.dxr`, `.cxt`, Flash SWF, Cinepak AVI, and 16-bit PCM audio) into open, future-proof web standards with **100% forensic fidelity and zero data loss**.

---

## 🌟 Key Highlights

- **10 Thematic Curriculum Chapters**:
  1. *The Language of India* — Antiquity, Indo-European linguistic tree, and historical scholars.
  2. *The Mother of Languages* — Science of phonetics (*Śikṣā*), anatomical vocal tract resonance, and Māheśvara Sūtras.
  3. *Chitrakāvya Visual Diagrams* — Classical wordplay, geometric bandhas, anagrams, and Knight's Tour chess puzzles (*Turaṅga-gati*).
  4. *The Language of Science* — Mathematics (*Baudhāyana Śulba Sūtras*), Astronomy, Medicine (*Āyurveda*), and Rick Briggs' NASA AI paper.
  5. *An Inexhaustible Literature* — The poetic trinity (Kālidāsa, Bhavabhūti, Bhāravi) and classical Mahākāvya verses.
  6. *Subhāṣitas (Gems of Wisdom)* — Epigrammatic ethical verses on character, learning, and friendship.
  7. *Sacred & Spiritual Heritage* — Foundational Vedic hymns, Upaniṣadic inquiries, and Bhagavad Gītā recitations.
  8. *Sanskrit and Indian Languages* — Cognates and shared vocabulary across Indo-Aryan and Dravidian language families.
  9. *Doubts & Clarifications* — Scholarly refutations of misconceptions regarding Sanskrit antiquity and accessibility.
  10. *The Soul of India* — Sanskrit as the national cultural foundation, state mottos (*Satyameva Jayate*, *Yogaḥ Karmasu Kauśalam*), and emblems.

- **149 Master Voice Recitations**: High-fidelity 192 kbps AAC-LC voice audio (+ 192 kbps MP3 fallback) with synchronised lyrics, progress scrubbers, in-place pausing, and verse filtering.
- **149-Verse Master Shlokas Concordance**: Interactive searchable index (`shlokas.dxr`) enabling instant lookup by chapter, theme, author, or meter.
- **40 Participating Sanskrit Institutions Directory**: Complete directory of partner universities, research institutes, and manuscript libraries with categorized state and national academies.
- **Anatomical Vocal Tract Lightbox**: High-resolution diagrams illustrating point-of-articulation resonance across gutturals, palatals, retroflexes, dentals, and labials.
- **Chitrakāvya Puzzle Solvers**: Interactive geometric diagrams for Drum (*Muraja-bandha*), Cow's Path (*Gomūtrikā*), and Omnidirectional (*Sarvatobhadra*) patterns.
- **3-Way Live Sanskrit & English Switcher**:
  1. *Devanagari (देवनागरी)* — Pure classical Sanskrit typography.
  2. *Bilingual Side-by-Side* — Sanskrit verse on top, English commentary beneath.
  3. *English + IAST* — Academic transliteration with macrons (*ā, ī, ū, ṛ, ṅ, ñ, ś, ṣ*).
- **Interactive Sanskrit Search Engine**: Client-side inverted index searching all 149 verses and 10 chapters with Devanagari ligature normalization, phonetic Romanization, and deep-linking.
- **Smart TV 10-Foot UI**: Spatial D-pad remote navigation, keyboard shortcuts, and high-contrast gold focus outlines.
- **Zero-Dependency Architecture**: Pure Semantic HTML5, Modular CSS3, and Vanilla ES6+. Zero npm packages, zero build steps, zero legacy runtimes.

---

## 🚀 Live Demo on GitHub Pages

The application is deployed directly via GitHub Pages:  
👉 **`https://gapskris.github.io/devabhasha/`**

---

## 💻 Quick Start & Running Locally

The modernized application is completely portable and requires no build pipeline:

### Option 1: Direct Double-Click (`file:///`)
Double-click **`index.html`** in any modern web browser. All chapter text and metadata are pre-packaged synchronously in `js/data.js` to bypass local-file CORS restrictions cleanly.

### Option 2: High-Performance Local Launcher
Run the embedded Python HTTP server with **native HTTP 206 Partial Content (Range Seeking)** for smooth audio/video scrubbing:
```bash
# Clone the repository
git clone https://github.com/gapskris/devabhasha.git
cd devabhasha

# Launch the local HTTP runner (opens browser at http://localhost:8080)
python run_local.py
```

---

## 🧪 Automated Test & Verification Suite

To run the automated 82-point forensic verification suite:
```bash
python tools/verify_1to1_mapping.py
```
This tests:
* 100% presence and integrity of all 149 M4A + 149 MP3 recitation tracks
* Zero-delay streaming with `+faststart` moov atom alignment on opening montage video
* Multi-slide slide sequencing and anatomical diagram linkages
* All modal dialogs, search indexing, and 3-way typography switches

---

## 🏛️ Heritage Acknowledgments

* **Original CD-ROM Production (1997)**: Sri Aurobindo Society, Pondicherry, India.
* **Preservation & Modernization (2026)**: Open-source digital heritage preservation under modern web standards.
