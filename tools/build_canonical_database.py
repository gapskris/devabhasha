"""
Canonical Database Generator for Devabhāṣā (1997 CD-ROM -> 2026 Modern Web)
Generates content/data.json containing:
- 10 Complete Curriculum Chapters with Multi-Slide Sub-Paging & Anatomical Resonance
- All 149 High-Fidelity Recitation Mappings (M4A & MP3)
- Opening Title Animation & Montage Video metadata
- Master Shlokas Concordance (149 tracks dual-indexed)
- Historical Archival Sections (Acknowledgments, Institutions, SAS Memorial, Help, Exit)
"""

import os
import json

ROOT = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern"
CONTENT_FILE = os.path.join(ROOT, "content", "data.json")

# Chapter 2 Slide Definitions
ch2_slides = [
    {
        "id": 1,
        "slideNumber": 1,
        "title": "The Sanskrit Alphabet (Varṇamālā)",
        "canvas": "assets/images/chap2/page01.jpg",
        "trackIndex": 0,
        "diagram": None,
        "diagramTitle": None
    },
    {
        "id": 2,
        "slideNumber": 2,
        "title": "Gutturals — Ka-Varga (क ख ग घ ङ)",
        "canvas": "assets/images/chap2/page02.jpg",
        "trackIndex": 1,
        "diagram": "assets/images/chap2/guttural.JPG",
        "diagramTitle": "Kaṇṭha (Guttural) Vocal Articulation"
    },
    {
        "id": 3,
        "slideNumber": 3,
        "title": "Palatals — Cha-Varga (च छ ज झ ञ)",
        "canvas": "assets/images/chap2/page03.jpg",
        "trackIndex": 2,
        "diagram": "assets/images/chap2/palatal.jpg",
        "diagramTitle": "Tālu (Palatal) Vocal Articulation"
    },
    {
        "id": 4,
        "slideNumber": 4,
        "title": "Cerebrals / Retroflex — Ṭa-Varga (ट ठ ड ढ ण)",
        "canvas": "assets/images/chap2/page04.jpg",
        "trackIndex": 3,
        "diagram": "assets/images/chap2/cerebal.jpg",
        "diagramTitle": "Mūrdhā (Retroflex) Vocal Articulation"
    },
    {
        "id": 5,
        "slideNumber": 5,
        "title": "Dentals — Ta-Varga (त थ द ध न)",
        "canvas": "assets/images/chap2/page05.jpg",
        "trackIndex": 4,
        "diagram": "assets/images/chap2/dental.JPG",
        "diagramTitle": "Danta (Dental) Vocal Articulation"
    },
    {
        "id": 6,
        "slideNumber": 6,
        "title": "Labials — Pa-Varga (प फ ब भ म)",
        "canvas": "assets/images/chap2/page06.jpg",
        "trackIndex": 5,
        "diagram": "assets/images/chap2/labialconso .jpg",
        "diagramTitle": "Oṣṭha (Labial) Vocal Articulation"
    },
    {
        "id": 7,
        "slideNumber": 7,
        "title": "Semi-Vowels — Antastha (य र ल व)",
        "canvas": "assets/images/chap2/page07.jpg",
        "trackIndex": 6,
        "diagram": "assets/images/chap2/ishat.jpg",
        "diagramTitle": "Antastha (Semi-Vowels) Resonance"
    },
    {
        "id": 8,
        "slideNumber": 8,
        "title": "Aspirate & Sibilants (श ष स ह)",
        "canvas": "assets/images/chap2/page08.jpg",
        "trackIndex": 7,
        "diagram": "assets/images/chap2/ha.JPG",
        "diagramTitle": "Ūṣman (Sibilants & Aspirate)"
    },
    {
        "id": 9,
        "slideNumber": 9,
        "title": "Euphonic Combination (Sandhi Rules)",
        "canvas": "assets/images/chap2/page09.jpg",
        "trackIndex": 8,
        "diagram": None,
        "diagramTitle": None
    },
    {
        "id": 10,
        "slideNumber": 10,
        "title": "Shiva Sutra Chants (Part 1)",
        "canvas": "assets/images/chap2/page10.jpg",
        "trackIndex": 9,
        "diagram": None,
        "diagramTitle": None
    },
    {
        "id": 11,
        "slideNumber": 11,
        "title": "Anatomical Vocalization Resonance",
        "canvas": "assets/images/chap2/page11.jpg",
        "trackIndex": 10,
        "diagram": "assets/images/chap2/anib.jpg",
        "diagramTitle": "Acoustic Vocal Tract Resonance"
    },
    {
        "id": 12,
        "slideNumber": 12,
        "title": "Vedic Accentuation: Udātta, Anudātta, Svarita",
        "canvas": "assets/images/chap2/page12.jpg",
        "trackIndex": 11,
        "diagram": None,
        "diagramTitle": None
    },
    {
        "id": 13,
        "slideNumber": 13,
        "title": "Traditional Paninian Recitation",
        "canvas": "assets/images/chap2/page13.jpg",
        "trackIndex": 12,
        "diagram": None,
        "diagramTitle": None
    },
    {
        "id": 14,
        "slideNumber": 14,
        "title": "Pranava OM Acoustic Synthesis",
        "canvas": "assets/images/chap2/page14.jpg",
        "trackIndex": 13,
        "diagram": None,
        "diagramTitle": None
    }
]

# Additional Paninian matrix slides for Chapter 2 (pages 15 to 23)
diag_extras = [
    ("assets/images/chap2/popb.jpg", "Internal Effort (Ābhyantara Prayatna)"),
    ("assets/images/chap2/ushman.jpg", "Sibilants Architecture (Ūṣma-Varṇa)"),
    ("assets/images/chap2/ya.JPG", "Palatal Semi-Vowel Articulation (Ya-kāra)"),
    ("assets/images/chap2/ra.JPG", "Retroflex Liquid Articulation (Ra-kāra)"),
    ("assets/images/chap2/la.JPG", "Dental Lateral Articulation (La-kāra)"),
    ("assets/images/chap2/va.JPG", "Dento-Labial Articulation (Va-kāra)"),
    ("assets/images/chap2/sa.JPG", "Palatal Sibilant Articulation (Śa-kāra)"),
    ("assets/images/chap2/saa.JPG", "Dental Sibilant Articulation (Sa-kāra)"),
    ("assets/images/chap2/alpha.jpg", "Sanskrit Phonetic Grid Overview")
]

for idx, (diag_img, diag_lbl) in enumerate(diag_extras, start=15):
    ch2_slides.append({
        "id": idx,
        "slideNumber": idx,
        "title": f"Paninian Phonetics & Articulation Matrix (Page {idx})",
        "canvas": f"assets/images/chap2/page{idx:02d}.jpg",
        "trackIndex": None,
        "diagram": diag_img,
        "diagramTitle": diag_lbl
    })

# Chapter 3 Slides (6 geometric diagram canvases)
ch3_slides = [
    {
        "id": 1,
        "slideNumber": 1,
        "title": "Kalidasa's Dvikshara & Ekakshara Mastery",
        "canvas": "assets/images/chap03/kalidas.jpg",
        "description": "Mastery of one-syllable and two-syllable verses in classical poetry."
    },
    {
        "id": 2,
        "slideNumber": 2,
        "title": "Sage Valmiki & The Birth of Shloka",
        "canvas": "assets/images/chap03/valmiki.jpg",
        "description": "The transformation of grief (śoka) into immortal verse (śloka)."
    },
    {
        "id": 3,
        "slideNumber": 3,
        "title": "Muraja-Bandha: The Double-Headed Drum Pattern",
        "canvas": "assets/images/chap03/drum.jpg",
        "description": "Geometric poem woven along the diagonal cords of the sacred drum."
    },
    {
        "id": 4,
        "slideNumber": 4,
        "title": "Turanga-Gati: The Knight's Tour on 8x8 Chessboard",
        "canvas": "assets/images/chap03/chess.jpg",
        "description": "Sanskrit verse traversing an 8x8 board through chess Knight moves."
    },
    {
        "id": 5,
        "slideNumber": 5,
        "title": "Gomutrika-Bandha: The Zigzag Cow's Path",
        "canvas": "assets/images/chap03/gau.jpg",
        "description": "Constrained verse alternating diagonally like the sacred path."
    },
    {
        "id": 6,
        "slideNumber": 6,
        "title": "Sarvatobhadra: The Omnidirectional Magic Square Grid",
        "canvas": "assets/images/chap03/diag04.jpg",
        "description": "A perfect phonetic matrix reading identically in all 8 directions."
    }
]

# Chapter 5 Slides (20 classical poetry canvases)
ch5_slides = []
for i in range(1, 20):
    ch5_slides.append({
        "id": i,
        "slideNumber": i,
        "title": f"Classical Poetry Manuscript Page {i}",
        "canvas": f"assets/images/chapter5/chap5page{i:02d}.jpg"
    })
ch5_slides.append({
    "id": 20,
    "slideNumber": 20,
    "title": "Sage Valmiki — Adi Kavi of Classical Kavya",
    "canvas": "assets/images/chapter5/valmiki.jpg"
})

# Chapter 6 Slides (12 wisdom canvases)
ch6_slides = []
for i in range(1, 10):
    ch6_slides.append({
        "id": i,
        "slideNumber": i,
        "title": f"Subhashita Wisdom Inscription Page {i}",
        "canvas": f"assets/images/chapter6/chapter6page{i:02d}.jpg"
    })
ch6_slides.extend([
    {"id": 10, "slideNumber": 10, "title": "Friedrich Engels on Ancient Indian Logic", "canvas": "assets/images/chapter6/engels.jpg"},
    {"id": 11, "slideNumber": 11, "title": "Mahatma Gandhi on Sanskrit Moral Education", "canvas": "assets/images/chapter6/gandhi.jpg"},
    {"id": 12, "slideNumber": 12, "title": "Karl Marx on Indian Heritage & Culture", "canvas": "assets/images/chapter6/marx.jpg"}
])

# Chapter 7 Slides (16 sacred Vedic canvases)
ch7_slides = []
for i in range(1, 16):
    ch7_slides.append({
        "id": i,
        "slideNumber": i,
        "title": f"Sacred Vedic & Upanishadic Revelation Page {i}",
        "canvas": f"assets/images/chapter7/chap7page{i:02d}.jpg"
    })
ch7_slides.append({
    "id": 16,
    "slideNumber": 16,
    "title": "Adi Shankaracharya — Master of Non-Dual Advaita",
    "canvas": "assets/images/chapter7/shankaracharya.jpg"
})

# 1. Chapters Specification
CHAPTERS_DATA = [
    {
        "id": 1,
        "slug": "chap1",
        "titleSanskrit": "भारतस्य भाषा",
        "titleIAST": "Bhāratasya Bhāṣā",
        "titleEnglish": "The Language of India",
        "subtitle": "Antiquity, Greatness and the Rediscovery of Sanskrit",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "totalSections": 6,
        "slides": [
            {"id": 1, "slideNumber": 1, "title": "Entering the Ancient Temple of Speech", "canvas": "assets/images/chapter1/chap1page01.jpg", "trackIndex": 0, "sectionIndex": 0},
            {"id": 2, "slideNumber": 2, "title": "Prof. Friedrich Schlegel — An Enthralling Discovery", "canvas": "assets/images/chapter1/chap1page02.jpg", "trackIndex": None, "sectionIndex": 1, "scholarImage": "assets/images/chapter1/schlegel-th.jpg"},
            {"id": 3, "slideNumber": 3, "title": "W.C. Taylor — Delicacy & Philosophy", "canvas": "assets/images/chapter1/chap1page03.jpg", "trackIndex": None, "sectionIndex": 2},
            {"id": 4, "slideNumber": 4, "title": "Will Durant — Mother of Languages", "canvas": "assets/images/chapter1/chap1page04.jpg", "trackIndex": None, "sectionIndex": 3},
            {"id": 5, "slideNumber": 5, "title": "Sri Aurobindo — The Living River of Antiquity", "canvas": "assets/images/chapter1/chap1page05.jpg", "trackIndex": None, "sectionIndex": 4},
            {"id": 6, "slideNumber": 6, "title": "Mahakavi Kalidasa — Awakening of Modern India", "canvas": "assets/images/chapter1/chap1page06.jpg", "trackIndex": None, "sectionIndex": 5}
        ],
        "audioTracks": [
            {
                "id": "chap1_01",
                "slideIndex": 0,
                "title": "Raghuvamsham Invocation — Kalidasa",
                "sanskrit": "वागर्थाविव सम्पृक्तौ वागर्थप्रतिपत्तये ।\nजगतः पितरौ वन्दे पार्वतीपरमेश्वरौ ॥",
                "iast": "vāgarthāviva sampṛktau vāgarthapratipattaye |\njagataḥ pitarau vande pārvatīparameśvarau ||",
                "translation": "For the mastery of word and sense, I bow to the Parents of the universe, the Mountain-Daughter Parvati and the Supreme Lord Shiva, who are united like word and meaning.",
                "m4a": "assets/audio/chap1/chap 1.m4a",
                "mp3": "assets/audio/chap1/chap 1.mp3",
                "duration": 34.2
            }
        ],
        "scholars": [
            {
                "name": "Prof. Friedrich Schlegel",
                "role": "German Philosopher & Indologist",
                "image": "assets/images/chapter1/schlegel-th.jpg",
                "quote": "Justly it is called Sanskrit, that is to say, perfected and refined. Sanskrit combines these various qualities possessed separately by other tongues: Grecian copiousness, deep-toned Roman force, and Celtic flexibility."
            },
            {
                "name": "W.C. Taylor",
                "role": "American Indologist",
                "image": "assets/images/chapter1/chap1page02.jpg",
                "quote": "It was an astounding discovery that Hindustan possessed, in spite of the changes of realms and time, a language of extraordinary structure and subtle delicacy, and a philosophy compared with which the lessons of Pythagoras are but of yesterday."
            },
            {
                "name": "Will Durant",
                "role": "Historian & Author of 'The Story of Civilization'",
                "image": "assets/images/chapter1/chap1page03.jpg",
                "quote": "India was the motherland of our race and Sanskrit the mother of Europe's languages; she was the mother of our philosophy, mother through the Arabs of much of our mathematics, mother through Buddha of ideals embodied in Christianity."
            },
            {
                "name": "Sri Aurobindo",
                "role": "Sage, Poet & Philosopher",
                "image": "assets/images/chapter1/chap1page04.jpg",
                "quote": "The ancient and classical creations of the Sanskrit tongue, both in quality and in body and abundance of excellence, in their potent originality and immense vigour of intellect, are equal to those of any other language."
            },
            {
                "name": "Dr. David Frawley",
                "role": "Vedic Scholar & Author",
                "image": "assets/images/chapter1/chap1page05.jpg",
                "quote": "Sanskrit is the oldest most continually used language in the world. It possesses a larger group of works on spirituality, metaphysics and mythology than any other language."
            },
            {
                "name": "Mahakavi Kalidasa",
                "role": "Kavikulaguru & Master Dramatist",
                "image": "assets/images/chapter1/chap1page06.jpg",
                "quote": "Vagarthaviva samprktau vagarthapratipattaye — Through the perfect union of sound, word and meaning, speech becomes divine."
            }
        ],
        "contentSections": [
            {
                "page": 1,
                "heading": "Entering the Ancient Temple of Speech",
                "body": "Let it be known right at the outset that this book is not written by a scholar and furthermore is not meant for scholars. In spite of never having studied Sanskrit in a systematic manner or in great depth, we surrendered to the stereotype of Sanskrit being a difficult language to learn.\n\nHowever, certain circumstances intervened. We took up a project called 'The Wonder that is Sanskrit', where our endeavour was to discover the greatest and highest achievements of India in every field. It was inevitable for one to turn to Sanskrit, one of the oldest and richest languages of the world."
            },
            {
                "page": 2,
                "heading": "An Enthralling Discovery",
                "body": "What resulted was an enthralling and fulfilling experience. The deeper we went into it, the more amazed we were by the beauty and perfection of this language. It was veritably the experience of entering an ancient Indian temple: huge, majestic and mighty, yet with each facet intricately carved and exquisitely polished.\n\nWe have all learnt our alphabets, our grammars and our languages from early childhood. But rarely does one bother to ask: What is language? What is its purpose? How does it communicate?"
            },
            {
                "page": 3,
                "heading": "The Greatest Language in the World",
                "body": "'Sanskrit is the greatest language in the world.' One would imagine such a statement to be mere sales talk. What it is, in actuality, is a very well researched and deliberate evaluation made by thinkers of diverse backgrounds across three centuries.\n\nA language derives its value not merely from its logical and grammatical structure, but from the manner in which it has been used, the treasures it enshrines, and the heights of human spirit to which it has given voice."
            },
            {
                "page": 4,
                "heading": "Colossal Literature & Phenomenal Diversity",
                "body": "It was not just a question of a phenomenal quantity and variety, but also of the highest quality. W.C. Taylor remarked that Hindustan possessed a philosophy compared with which the lessons of Pythagoras are but of yesterday, and in daring, Greece's boldest efforts were tame.\n\nWill Durant affirmed that India was the motherland of our race, and Sanskrit the mother of Europe's languages."
            },
            {
                "page": 5,
                "heading": "The Living River of Antiquity",
                "body": "By the most conservative accounts, Sanskrit has been used continuously since 1500 B.C.; by more liberal accounts, it was in use long before 3000 B.C. It is the sacred language of two of the world's greatest spiritual traditions: Hinduism and Buddhism.\n\nMuch like the sacred river Ganga, Sanskrit has flowed across India for millennia, embracing and nourishing all who approached her waters."
            },
            {
                "page": 6,
                "heading": "The Awakening of Modern India",
                "body": "It is an attempt to come into contact with the heart of Sanskrit and through it, the soul of India. Kalidasa begins his famous work Raghuvamsham by invoking the divine Parents of the universe, Shiva and Parvati, united as word and sense.\n\nMay this be also the beginning of our journey into the wonder that is Sanskrit."
            }
        ]
    },
    {
        "id": 2,
        "slug": "chap2",
        "titleSanskrit": "भाषाणाम् जननी",
        "titleIAST": "Bhāṣāṇāṁ Jananī",
        "titleEnglish": "The Mother of Languages",
        "subtitle": "The Science of Sound, Phonetics & Maheshvara Sutras",
        "canvas": "assets/images/chap2/01.jpg",
        "totalSections": 23,
        "slides": ch2_slides,
        "audioTracks": [
            {"id": "c2_alphabet", "slideIndex": 0, "title": "Sanskrit Alphabet (Varṇamālā)", "m4a": "assets/audio/chap2/Alphabet.m4a", "mp3": "assets/audio/chap2/Alphabet.mp3"},
            {"id": "c2_kavarga", "slideIndex": 1, "title": "Gutturals — Ka-Varga (क ख ग घ ङ)", "m4a": "assets/audio/chap2/Ka-varga.m4a", "mp3": "assets/audio/chap2/Ka-varga.mp3"},
            {"id": "c2_chavarga", "slideIndex": 2, "title": "Palatals — Cha-Varga (च छ ज झ ञ)", "m4a": "assets/audio/chap2/Cha-varga.m4a", "mp3": "assets/audio/chap2/Cha-varga.mp3"},
            {"id": "c2_ttavarga", "slideIndex": 3, "title": "Cerebrals / Retroflex — Ṭa-Varga (ट ठ ड ढ ण)", "m4a": "assets/audio/chap2/Tta-varga.m4a", "mp3": "assets/audio/chap2/Tta-varga.mp3"},
            {"id": "c2_tavarga", "slideIndex": 4, "title": "Dentals — Ta-Varga (त थ द ध न)", "m4a": "assets/audio/chap2/Ta-varga.m4a", "mp3": "assets/audio/chap2/Ta-varga.mp3"},
            {"id": "c2_pavarga", "slideIndex": 5, "title": "Labials — Pa-Varga (प फ ब भ म)", "m4a": "assets/audio/chap2/Pa-varga.m4a", "mp3": "assets/audio/chap2/Pa-varga.mp3"},
            {"id": "c2_ishat", "slideIndex": 6, "title": "Semi-Vowels — Antastha (य र ल व)", "m4a": "assets/audio/chap2/Ishatsparsha.m4a", "mp3": "assets/audio/chap2/Ishatsparsha.mp3"},
            {"id": "c2_ushman", "slideIndex": 7, "title": "Sibilants — Ūṣman (श ष स)", "m4a": "assets/audio/chap2/ushman.m4a", "mp3": "assets/audio/chap2/ushman.mp3"},
            {"id": "c2_h", "slideIndex": 8, "title": "Aspirate — Hakāra (ह)", "m4a": "assets/audio/chap2/H.m4a", "mp3": "assets/audio/chap2/H.mp3"},
            {"id": "c2_sandhi", "slideIndex": 9, "title": "Euphonic Combination (Sandhi Rules)", "m4a": "assets/audio/chap2/Sandhi.m4a", "mp3": "assets/audio/chap2/Sandhi.mp3"},
            {"id": "c2_s1", "slideIndex": 10, "title": "Shiva Sutra Chants (Part 1)", "m4a": "assets/audio/chap2/chapter2s1.m4a", "mp3": "assets/audio/chap2/chapter2s1.mp3"},
            {"id": "c2_s2", "slideIndex": 11, "title": "Anatomical Vocalization Resonance", "m4a": "assets/audio/chap2/chapter2s2.m4a", "mp3": "assets/audio/chap2/chapter2s2.mp3"},
            {"id": "c2_s3", "slideIndex": 12, "title": "Vedic Accentuation: Udātta, Anudātta, Svarita", "m4a": "assets/audio/chap2/chapter2s3.m4a", "mp3": "assets/audio/chap2/chapter2s3.mp3"},
            {"id": "c2_bhagavadgita", "slideIndex": 13, "title": "Bhagavadgītā Recitation & Metrics", "m4a": "assets/audio/chap2/Bhagavadgita.m4a", "mp3": "assets/audio/chap2/Bhagavadgita.mp3"}
        ],
        "contentSections": [
            {
                "page": 1,
                "heading": "The Scientific Architecture of the Sanskrit Alphabet",
                "body": "The Sanskrit alphabet (Varṇamālā) is not an arbitrary sequence of symbols, but a scientific classification based entirely on the human vocal tract. Sounds are ordered progressively from the deepest point of articulation at the throat (Guttural) forward to the lips (Labial)."
            },
            {
                "page": 2,
                "heading": "The Five Articulation Points (Sthānas)",
                "body": "1. Kaṇṭhya (Guttural): Throat resonance (क, ख, ग, घ, ङ)\n2. Tālavya (Palatal): Hard palate (च, छ, ज, झ, ञ)\n3. Mūrdhanya (Cerebral/Retroflex): Roof of the palate (ट, ठ, ड, ढ, ण)\n4. Dantya (Dental): Teeth contact (त, थ, द, ध, न)\n5. Oṣṭhya (Labial): Lips closure (प, फ, ब, भ, म)"
            },
            {
                "page": 3,
                "heading": "Maheshvara Sutras: The Foundation of Paninian Grammar",
                "body": "According to tradition, Panini received the 14 fundamental sound sequences from the beats of Lord Shiva's Damaru. These 14 Sutras compress all possible phonetic transformations into elegant, mathematical code formulas."
            }
        ]
    },
    {
        "id": 3,
        "slug": "chap3",
        "titleSanskrit": "चित्रकाव्यम्",
        "titleIAST": "Citrakāvyam",
        "titleEnglish": "Chitrakavya — Wonder of Visual Poetry",
        "subtitle": "Mathematical Verses, Constrained Patterns & Knight's Tour",
        "canvas": "assets/images/chap03/kalidas.jpg",
        "totalSections": 6,
        "slides": ch3_slides,
        "audioTracks": [
            {
                "id": f"c3_s{i:02d}",
                "slideIndex": min(i // 6, 5),
                "title": f"Chitrakavya Demonstration {i}",
                "m4a": f"assets/audio/chap3/chapter3s{i:02d}.m4a",
                "mp3": f"assets/audio/chap3/chapter3s{i:02d}.mp3"
            } for i in range(1, 34)
        ],
        "contentSections": [
            {
                "page": 1,
                "heading": "Chitrakavya: The Pinnacle of Poetic Ingenuity",
                "body": "Chitrakavya represents one of the most astonishing genres of Sanskrit literature. Poets constructed verses that simultaneously adhered to rigorous metrical rules while forming geometric diagrams (bandhas), palindromes, and chess knight moves."
            },
            {
                "page": 2,
                "heading": "Turanga-Gati: The Knight's Tour in Sanskrit Verse",
                "body": "In the Turanga-Pada-Bandha, a verse written on an 8x8 chessboard reveals an entirely new, meaningful stanza when read along the L-shaped moves of a chess Knight (Aśva)."
            },
            {
                "page": 3,
                "heading": "Muraja-Bandha: The Drum Constellation",
                "body": "In Muraja-Bandha, the syllables of the poem, when mapped onto the diagonal laces of a traditional double-headed drum (Mridangam), read identically whether traced along the strings or across the perimeter."
            }
        ]
    },
    {
        "id": 4,
        "slug": "chap4",
        "titleSanskrit": "विज्ञानस्य भाषा",
        "titleIAST": "Vijñānasya Bhāṣā",
        "titleEnglish": "The Language of Science",
        "subtitle": "Mathematics, Astronomy, Medicine & AI in Sanskrit",
        "canvas": "assets/images/chap03/diag04.jpg",
        "totalSections": 5,
        "slides": [
            {"id": 1, "slideNumber": 1, "title": "Baudhayana's Sulba Sutras & Ancient Geometry", "canvas": "assets/images/chap03/diag04.jpg", "trackIndex": 0},
            {"id": 2, "slideNumber": 2, "title": "Aryabhata's Astronomical Algorithms", "canvas": "assets/images/chap03/diag04.jpg", "trackIndex": 1},
            {"id": 3, "slideNumber": 3, "title": "Pingala's Binary System & Combinatorics (Chandas)", "canvas": "assets/images/chap03/diag04.jpg", "trackIndex": 2},
            {"id": 4, "slideNumber": 4, "title": "Sushruta & Charaka: The Foundations of Ayurveda", "canvas": "assets/images/chap03/diag04.jpg", "trackIndex": 3},
            {"id": 5, "slideNumber": 5, "title": "Rick Briggs & NASA: Sanskrit in Artificial Intelligence", "canvas": "assets/images/chap03/diag04.jpg", "trackIndex": 4}
        ],
        "audioTracks": [
            {"id": f"c4_s{i}", "slideIndex": i - 1, "title": f"Scientific Treatises & Shlokas {i}", "m4a": f"assets/audio/chap4/chapter4s{i}.m4a", "mp3": f"assets/audio/chap4/chapter4s{i}.mp3"} for i in range(1, 6)
        ],
        "contentSections": [
            {
                "page": 1,
                "heading": "Sanskrit: The Precise Medium of Exact Sciences",
                "body": "Far from being limited to liturgical chants, Sanskrit served as the scientific language of ancient India. From Baudhayana's Sulba Sutras (containing the earliest geometric formulations of the Pythagorean theorem) to Aryabhata's astronomical algorithms, Sanskrit delivered mathematical ideas with concise elegance."
            },
            {
                "page": 2,
                "heading": "Rick Briggs & NASA: Sanskrit in Artificial Intelligence",
                "body": "In 1985, NASA researcher Rick Briggs published his landmark paper 'Knowledge Representation in Sanskrit and Artificial Intelligence' in AI Magazine, demonstrating that ancient Paninian grammarians had constructed a semantic representation system that modern computer science was only beginning to rediscover."
            }
        ]
    },
    {
        "id": 5,
        "slug": "chap5",
        "titleSanskrit": "अक्षयं साहित्यम्",
        "titleIAST": "Akṣayaṁ Sāhityam",
        "titleEnglish": "An Inexhaustible Literature",
        "subtitle": "The Classical Kavya Trinity: Kalidasa, Bhavabhuti, Bharavi",
        "canvas": "assets/images/chapter5/chap5page01.jpg",
        "totalSections": 20,
        "slides": ch5_slides,
        "audioTracks": [
            {
                "id": f"c5_s{i:02d}",
                "slideIndex": min(int((i - 1) * 20 / 31), 19),
                "title": f"Classical Poetry Recitation {i}",
                "m4a": f"assets/audio/chap5/chapter5s{i}.m4a",
                "mp3": f"assets/audio/chap5/chapter5s{i}.mp3"
            } for i in range(1, 32)
        ],
        "contentSections": [
            {
                "page": 1,
                "heading": "The Grand Canvas of Classical Sanskrit Poetry",
                "body": "Classical Sanskrit literature is celebrated for its boundless imagination, delicate lyricism, and profound psychological insight. The trinity of poets—Kalidasa, Bhavabhuti, and Bharavi—elevated human emotion and natural beauty into timeless art."
            },
            {
                "page": 2,
                "heading": "Kalidasa: The Master of Similes (Upamā)",
                "body": "'Upamā Kālidāsasya'—the similes of Kalidasa are unequalled in world literature. In works like Meghadutam (The Cloud Messenger) and Abhijnanashakuntalam, every verse paints a vivid, evocative picture of nature and human longing."
            }
        ]
    },
    {
        "id": 6,
        "slug": "chap6",
        "titleSanskrit": "सुभाषितानि",
        "titleIAST": "Subhāṣitāni",
        "titleEnglish": "Subhashitas — Gems of Wisdom",
        "subtitle": "Epigrammatic Philosophy, Friendship, Learning & Ethics",
        "canvas": "assets/images/chapter6/chapter6page01.jpg",
        "totalSections": 12,
        "slides": ch6_slides,
        "audioTracks": [
            {
                "id": f"c6_s{i:02d}",
                "slideIndex": min(int((i - 1) * 12 / 22), 11),
                "title": f"Subhashita Wisdom Verse {i}",
                "m4a": f"assets/audio/chap6/chapter6s{i}.m4a",
                "mp3": f"assets/audio/chap6/chapter6s{i}.mp3"
            } for i in range(1, 23)
        ],
        "contentSections": [
            {
                "page": 1,
                "heading": "Subhashitas: Condensed Wisdom for Daily Living",
                "body": "Subhashitas ('well-spoken words') are epigrammatic Sanskrit verses that distill centuries of practical wisdom, social ethics, psychological discernment, and moral virtue into four concise lines."
            },
            {
                "page": 2,
                "heading": "Themes of Life: Knowledge, True Friendship and Character",
                "body": "Verses praise the indestructible wealth of knowledge (Vidyā), contrast the steadfast friend with the fair-weather companion, and celebrate nobility of character above royal birth or material wealth."
            }
        ]
    },
    {
        "id": 7,
        "slug": "chap7",
        "titleSanskrit": "आध्यात्मिकम् दायम्",
        "titleIAST": "Ādhyātmikaṁ Dāyam",
        "titleEnglish": "Sacred & Spiritual Heritage",
        "subtitle": "Vedas, Upanishads, Bhagavad Gita & Stotras",
        "canvas": "assets/images/chapter7/chap7page01.jpg",
        "totalSections": 16,
        "slides": ch7_slides,
        "audioTracks": [
            *(
                {
                    "id": f"c7_s{i:02d}",
                    "slideIndex": min(int((i - 1) * 16 / 40), 15),
                    "title": f"Sacred Vedic Recitation {i}",
                    "m4a": f"assets/audio/chap7/chapter7s{i}.m4a",
                    "mp3": f"assets/audio/chap7/chapter7s{i}.mp3"
                } for i in range(1, 40)
            ),
            {
                "id": "c7_s1b",
                "slideIndex": 0,
                "title": "Sacred Vedic Recitation 1b (Invocation Variant)",
                "m4a": "assets/audio/chap7/chapter7s1b.m4a",
                "mp3": "assets/audio/chap7/chapter7s1b.mp3"
            }
        ],
        "contentSections": [
            {
                "page": 1,
                "heading": "The Sacred Sounds of the Seers",
                "body": "Sanskrit is universally revered as the language of the soul. In the Rigveda, the Upanishads, and the Bhagavad Gita, words become luminous vehicles for transcendental consciousness and communion with the Divine."
            },
            {
                "page": 2,
                "heading": "Mantras: Vibration and Spiritual Awakening",
                "body": "Vedic mantras are not mere words to be intellectually analyzed; they are sonic patterns (Śabda-Brahman) whose precise cadence and intonation awaken spiritual centers within the human being."
            }
        ]
    },
    {
        "id": 8,
        "slug": "chap8",
        "titleSanskrit": "संस्कृतं भारतीयाः भाषाश्च",
        "titleIAST": "Saṁskṛtaṁ Bhāratīyāḥ Bhāṣāśca",
        "titleEnglish": "Sanskrit and Indian Languages",
        "subtitle": "Common Roots, Shared Vocabulary & Cultural Bonds",
        "canvas": "assets/images/chapter8/raman.jpg",
        "totalSections": 1,
        "slides": [
            {"id": 1, "slideNumber": 1, "title": "Sir C.V. Raman on Sanskrit & Indian Linguistics", "canvas": "assets/images/chapter8/raman.jpg"}
        ],
        "audioTracks": [],
        "contentSections": [
            {
                "page": 1,
                "heading": "The Unifying Thread of Indian Linguistics",
                "body": "Sanskrit has provided the foundation and enriched the vocabulary of nearly all Indian languages. Whether Hindi, Bengali, Marathi, Gujarati, Telugu, Kannada, or Malayalam, thousands of shared Sanskrit cognates bridge cultural and regional boundaries."
            },
            {
                "page": 2,
                "heading": "Indo-Aryan and Dravidian Harmony",
                "body": "Centuries of intimate coexistence created deep syntactical and philosophical bonds across the linguistic traditions of India. Sanskrit acted as the universal scholarly and artistic bridge."
            }
        ]
    },
    {
        "id": 9,
        "slug": "chap9",
        "titleSanskrit": "संशयनिवारणम्",
        "titleIAST": "Saṁśayanivāraṇam",
        "titleEnglish": "Doubts & Clarifications",
        "subtitle": "Dispelling Misconceptions: The Myth of the Dead Language",
        "canvas": "assets/images/chapter9/william jones.jpg",
        "totalSections": 2,
        "slides": [
            {"id": 1, "slideNumber": 1, "title": "Sir William Jones & The Discovery of Indo-European", "canvas": "assets/images/chapter9/william jones.jpg"},
            {"id": 2, "slideNumber": 2, "title": "Historical Clarifications Archive", "canvas": "assets/images/chapter9/popup1.jpg"}
        ],
        "audioTracks": [],
        "contentSections": [
            {
                "page": 1,
                "heading": "Is Sanskrit a 'Dead' Language?",
                "body": "One of the most widespread modern misconceptions is that Sanskrit is a dead language. A language is only dead when its thoughts, ideals, and words cease to influence the living. Sanskrit lives daily in Indian rituals, classical music, dance, philosophical inquiry, and modern conversational movements."
            },
            {
                "page": 2,
                "heading": "Is Sanskrit Too Difficult to Learn?",
                "body": "Because of its systematic regularity, Sanskrit has fewer irregularities than English or French. Once the core phonetic and grammatical rules are understood, vocabulary acquisition is remarkably logical and intuitive."
            }
        ]
    },
    {
        "id": 10,
        "slug": "chap10",
        "titleSanskrit": "भारतस्य आत्मा",
        "titleIAST": "Bhāratasya Ātmā",
        "titleEnglish": "The Soul of India",
        "subtitle": "National Mottos, Cultural Unity & the Vision of Great Leaders",
        "canvas": "assets/images/chapter10/tagore.jpg",
        "totalSections": 2,
        "slides": [
            {"id": 1, "slideNumber": 1, "title": "Rabindranath Tagore on the Soul of India", "canvas": "assets/images/chapter10/tagore.jpg", "trackIndex": 0},
            {"id": 2, "slideNumber": 2, "title": "Jawaharlal Nehru on the Great Heritage", "canvas": "assets/images/chapter10/nehru.jpg", "trackIndex": 2}
        ],
        "audioTracks": [
            {"id": "c10_s1", "slideIndex": 0, "title": "National Motto: Satyameva Jayate (सत्यमेव जयते)", "m4a": "assets/audio/chap10/chapter10s1.m4a", "mp3": "assets/audio/chap10/chapter10s1.mp3"},
            {"id": "c10_s2", "slideIndex": 0, "title": "Universal Brotherhood: Vasudhaiva Kutumbakam (वसुधैव कुटुम्बकम्)", "m4a": "assets/audio/chap10/chapter10s2.m4a", "mp3": "assets/audio/chap10/chapter10s2.mp3"},
            {"id": "c10_s3", "slideIndex": 1, "title": "Tagore & Nehru on the Living Heritage of Sanskrit", "m4a": "assets/audio/chap10/chapter10s3.m4a", "mp3": "assets/audio/chap10/chapter10s3.mp3"}
        ],
        "contentSections": [
            {
                "page": 1,
                "heading": "Sanskrit: The Living Soul of India",
                "body": "As Jawaharlal Nehru wrote in 'The Discovery of India': 'If I was asked what is the greatest treasure which India possesses and what is her greatest heritage, I would answer unhesitatingly that it is the Sanskrit language and literature, and all that it contains.'\n\nRabindranath Tagore similarly observed that Sanskrit connects India with her timeless inner essence."
            },
            {
                "page": 2,
                "heading": "National Mottos Inscribed in Sanskrit",
                "body": "India's highest national ideals are enshrined in immortal Sanskrit mottos:\n- Supreme Court of India: 'Yato Dharmas Tato Jayaḥ' (यतो धर्मस्ततो जयः — Where there is righteousness, there is victory)\n- Republic of India: 'Satyameva Jayate' (सत्यमेव जयते — Truth alone triumphs)\n- Lok Sabha: 'Dharma Cakra Pravartanāya' (धर्मचक्रप्रवर्तनाय — For the wheel of righteous law)\n- Indian Navy: 'Śaṁ No Varuṇaḥ' (शं नो वरुणः — May the waters be auspicious to us)"
            }
        ]
    }
]

# 2. Build Master Shlokas Concordance (all 149 tracks)
all_shlokas = []
for ch in CHAPTERS_DATA:
    for track in ch["audioTracks"]:
        all_shlokas.append({
            "id": track["id"],
            "chapterId": ch["id"],
            "chapterTitle": ch["titleEnglish"],
            "slideIndex": track.get("slideIndex", 0),
            "title": track["title"],
            "sanskrit": track.get("sanskrit", track["title"]),
            "iast": track.get("iast", track["title"]),
            "translation": track.get("translation", ""),
            "m4a": track["m4a"],
            "mp3": track["mp3"]
        })

# 3. Assemble Complete Database
database = {
    "metadata": {
        "title": "Devabhāṣā — The Language of the Gods",
        "edition": "1997 Multimedia CD-ROM Modernization (2026 Web Application)",
        "publisher": "Sri Aurobindo Society, Puducherry",
        "collaborator": "Department of Sanskrit, Pondicherry University",
        "totalChapters": 10,
        "totalAudioTracks": len(all_shlokas),
        "totalVideos": 1,
        "totalVisuals": 127
    },
    "opening": {
        "title": "Opening Sequence",
        "titleAnimation": [
            "assets/images/opening/S01.jpg",
            "assets/images/opening/S02.jpg",
            "assets/images/opening/S03.jpg",
            "assets/images/opening/S04.jpg",
            "assets/images/opening/S05.jpg",
            "assets/images/opening/S06.jpg"
        ],
        "mosaicCanvases": [
            "assets/images/opening/03.jpg",
            "assets/images/opening/02.jpg",
            "assets/images/opening/01.jpg"
        ],
        "montageVideo": "assets/video/montage.mp4",
        "durationSeconds": 177.47
    },
    "chapters": CHAPTERS_DATA,
    "shlokasConcordance": all_shlokas,
    "archival": {
        "acknowledgments": {
            "title": "Credits & Acknowledgments",
            "backdrop": "assets/images/acknowledge/back.jpg",
            "institutions": [
                "ICICI",
                "T.T. Devasthanam",
                "Department of Sanskrit, Ministry of H.R.D, Govt. of India"
            ],
            "creativeTeam": [
                "Arjita", "Chetan Sharma", "Debajyoti", "Gunheild", "Harinarayan",
                "Jagrat", "Krishna Chandra Das", "Krishnalal", "Kirti", "Luminaura",
                "Madhulita", "Maurice", "Pavitra", "Priti", "Prof. Ramakanta Shukla",
                "Radhikaranjan", "Rukshad", "Sampad", "Shonar", "Sumati",
                "Sushanto", "Sushil", "Swadhin", "Vijay", "Vishnu Lalit", "Vladimir"
            ],
            "music": [
                "Times Music (Shaswat, Himalayan Chants, Dhyana)",
                "Shruti (Shakti)"
            ],
            "technicalGroup": [
                "Ashok", "Sunshine Music, Auroville",
                "St. Xavier Studio Pondicherry",
                "Virtual Digital Media, New Delhi"
            ]
        },
        "institutionsDirectory": {
            "title": "Participating Sanskrit Institutions",
            "banner": "assets/images/institution/institution .jpg",
            "directory": [
                "Adyar Library and Research Institute, Madras",
                "Asiatic Society of Bengal, Calcutta",
                "B.L. Institute of Indology, New Delhi",
                "Bhandarkar Oriental Research Institute, Pune",
                "Bharatiya Vidya Bhavanam, Mumbai",
                "Bihar Rashtra Bhasha Parishad, Patna",
                "CASS, Pune University, Pune",
                "French Institute of Indology, Pondicherry",
                "Ganganath Jha Kendriya Sanskrit Vidyapeeth, Allahabad",
                "Indira Gandhi National Centre for the Arts, New Delhi",
                "Kalidasa Academy, Ujjain",
                "Kalpataru Research Academy, Bangalore",
                "Kendriya Sahitya Academy, New Delhi",
                "Kuppuswamy Sastri Research Institute, Madras",
                "L.D. Institute of Indology, Ahmedabad",
                "Maharshi Sandipani Kendriya Veda Vidya Pratishthan, Ujjain",
                "Oriental Research Institute, Tirupati",
                "Ramakrishna Mission Institute of Culture, Calcutta",
                "Rashtriya Sanskrit Sansthan, New Delhi",
                "Sampurnananda Sanskrit University, Varanasi",
                "Samskrita Bharati, Bangalore",
                "Vaidik Sanshodhan Mandal, Pune"
            ]
        },
        "sasMemorial": {
            "title": "Sri Aurobindo Society — Puducherry",
            "photo": "assets/images/sas/sas.jpg",
            "description": "The Sri Aurobindo Society is a non-profit, international, spiritual organisation recognised by the Govt. of India as a research institute and an institution of national importance. Sanskrit being the language of India's soul and the unifying link for centuries, the Society has taken up several major initiatives in research, multimedia publication, and audio-visual preservation."
        },
        "helpGuide": {
            "title": "Multimedia User Guide & Keyboard Controls",
            "shortcuts": [
                {"key": "Space", "action": "Play / Pause active audio recitation"},
                {"key": "← / →", "action": "Previous / Next section or chapter"},
                {"key": "Ctrl+K or /", "action": "Open Sanskrit & Devanagari live search"},
                {"key": "1 - 3", "action": "Switch view: 1=Devanagari, 2=Bilingual, 3=IAST"},
                {"key": "T", "action": "Toggle Smart TV 10-foot mode"},
                {"key": "Esc", "action": "Close any active modal overlay"}
            ]
        }
    }
}

with open(CONTENT_FILE, "w", encoding="utf-8") as f:
    json.dump(database, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {CONTENT_FILE} ({len(all_shlokas)} shlokas across 10 chapters).")
