import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_DIR = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern"
DATA_JSON_PATH = os.path.join(PROJECT_DIR, "content", "data.json")

with open(DATA_JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# Chapters structure
chapters = data["chapters"]

# Chapter 1: 6 pages (already authentic)
# Ensure slide indices on Track 1
ch1 = next(c for c in chapters if c["id"] == 1)
ch1["totalSections"] = 6
if ch1.get("audioTracks"):
    ch1["audioTracks"][0]["slideIndex"] = 5  # Culminates on Page 6

# Chapter 2: 23 pages (already authentic)
ch2 = next(c for c in chapters if c["id"] == 2)
ch2["totalSections"] = 23

# Chapter 3: Restore all 15 authentic pages
ch3 = next(c for c in chapters if c["id"] == 3)
ch3["totalSections"] = 15

ch3_slides = [
    {
        "id": 1,
        "slideNumber": 1,
        "title": "Introduction to Chitrakavya: The Realm of Adhama-Kavya",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "description": "Linguistic acrobatics, constrained compositions, and the playful genius of Sanskrit poets.",
        "trackIndices": []
    },
    {
        "id": 2,
        "slideNumber": 2,
        "title": "Varnachitra: All 33 Consonants in Exact Phonetic Order",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "description": "A coherent prayer to Vishnu utilizing all 33 consonants from ka to ha without interruption.",
        "trackIndices": [0]
    },
    {
        "id": 3,
        "slideNumber": 3,
        "title": "Tryakshara & Dvyakshara: Strict Three and Two Consonant Constraints",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "description": "Poetic verses restricted entirely to 3 consonants (n, d, v) or 2 consonants (bh, r).",
        "trackIndices": [1, 2]
    },
    {
        "id": 4,
        "slideNumber": 4,
        "title": "Ekakshara: Monoconsonantal Mastery (Only 'na' and Only 'da')",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "description": "Kiratarjuniya and Shishupalavadha verses composed of a single repeating consonant.",
        "trackIndices": [3, 4]
    },
    {
        "id": 5,
        "slideNumber": 5,
        "title": "Sthanachitras, Monovocalics & Bidirectional Hymns",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "description": "Verses restricted to single phonetic organs, single vowels, and reversible palindromes.",
        "trackIndices": list(range(5, 18))
    },
    {
        "id": 6,
        "slideNumber": 6,
        "title": "Gomutrika-Bandha: The Zigzag Cow's Path",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "diagram": "assets/images/chap03/gau.jpg",
        "diagramTitle": "Gomūtrikā-Bandha Diagram Plate",
        "description": "Diagonal alternating syllables tracing the sacred path of the wandering cow.",
        "trackIndices": [18]
    },
    {
        "id": 7,
        "slideNumber": 7,
        "title": "Muraja-Bandha: The Constellation of the Double-Headed Drum",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "diagram": "assets/images/chap03/drum.jpg",
        "diagramTitle": "Muraja-Bandha Mridanga Drum Diagram",
        "description": "Poetic verse woven across the crossing diagonal laces of the sacred drum.",
        "trackIndices": [19]
    },
    {
        "id": 8,
        "slideNumber": 8,
        "title": "Sarvatobhadra: The Omnidirectional 8x8 Magic Square",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "diagram": "assets/images/chap03/diag04.jpg",
        "diagramTitle": "Sarvatobhadra 8x8 Magic Square Matrix",
        "description": "An 8x8 matrix reading identically forwards, backwards, downwards, and upwards.",
        "trackIndices": [20]
    },
    {
        "id": 9,
        "slideNumber": 9,
        "title": "Turanga-Gati: The Knight's Tour on the 8x8 Chessboard",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "diagram": "assets/images/chap03/chess.jpg",
        "diagramTitle": "Turanga-Pada-Bandha Chessboard Knight Tour",
        "description": "Vedanta Desika's Paduka Sahasram verse revealing a second sacred verse via Knight's moves.",
        "trackIndices": [21, 22]
    },
    {
        "id": 10,
        "slideNumber": 10,
        "title": "Samasya-Purti: Riddle Verses and Metrical Challenges",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "description": "Spontaneous poetic composition completing paradoxical final lines.",
        "trackIndices": [23, 24]
    },
    {
        "id": 11,
        "slideNumber": 11,
        "title": "Kalidasa's Wit & Riddle Verses",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "diagram": "assets/images/chap03/kalidas.jpg",
        "diagramTitle": "Mahakavi Kalidasa Historical Portrait",
        "description": "The black-faced, two-tongued riddle solved as the sacred quill pen.",
        "trackIndices": [25]
    },
    {
        "id": 12,
        "slideNumber": 12,
        "title": "Vakrokti: The Art of Clever Verbal Evasion & Playful Dialogue",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "description": "Humorous exchanges between Krishna and Satyabhama playing on multiple word meanings.",
        "trackIndices": [26, 27, 28]
    },
    {
        "id": 13,
        "slideNumber": 13,
        "title": "The Court of King Bhoja: The Humble Weaver's Poem",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "description": "A poor weaver dazzles the royal assembly with 'Kavāmi, Vayāmi, Yāmi'.",
        "trackIndices": [29]
    },
    {
        "id": 14,
        "slideNumber": 14,
        "title": "Kalidasa's Eulogies: The Grief and Resurrection of King Bhoja",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "description": "From 'Adya Dhara Niradhara' to 'Adya Dhara Sadadhara' upon finding Bhoja alive.",
        "trackIndices": [30, 31]
    },
    {
        "id": 15,
        "slideNumber": 15,
        "title": "The Ocean of Chitrakavya: Boundless Mastery of Speech",
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "description": "Concluding synthesis on how Sanskrit becomes an instrument of infinite creative play.",
        "trackIndices": [32]
    }
]

ch3["slides"] = ch3_slides

# Update slideIndex on Chapter 3 audio tracks
for trk_idx, trk in enumerate(ch3["audioTracks"]):
    for s_idx, s in enumerate(ch3_slides):
        if trk_idx in s["trackIndices"]:
            trk["slideIndex"] = s_idx
            break

# Chapter 4: Restore all 17 authentic pages & remove cloned diag04.jpg!
ch4 = next(c for c in chapters if c["id"] == 4)
ch4["totalSections"] = 17

ch4_pages_meta = [
    ("Sanskrit in Arts, Sciences and Daily Life", "Comprehensive vision of Sanskrit as an exact scientific medium.", []),
    ("Sanskrit and Artificial Intelligence: Rick Briggs & NASA", "Bridging natural language processing and Paninian semantic graphs.", []),
    ("Semantic Networks & Knowledge Representation", "How 5th-century BCE grammarians solved modern computer language problems.", []),
    ("Baudhayana Sulba Sutras: Ancient Indian Geometry", "Earliest formulation of the diagonal theorem (Pythagoras).", [0]),
    ("Precision Approximation of the Square Root of 2", "Fractional expansion calculating √2 to 5 decimal places.", [1]),
    ("Aryabhata I: Exact Calculation of Pi (3.1416)", "Astronomical treatises and circumference-to-diameter ratio.", [2]),
    ("The True Learning: Para Vidya and Apara Vidya", "Spiritual foundation integrating outer sciences with inner wisdom.", []),
    ("The Vedas and Vedangas: The Six Auxiliary Sciences", "Phonetics, metrics, grammar, etymology, astronomy, and ritual.", []),
    ("Jyotisha: Ancient Astronomy and Time Measurement", "Planetary positions, cosmic cycles, and celestial mathematics.", []),
    ("Shatarudriya Hymns: Metallurgy, Flora, and Ecology", "Vedic enumeration of metals, crafts, and forest conservation.", []),
    ("The Itihasas & Puranas: Encyclopedias of Human Knowledge", "Ramayana and Mahabharata as repositories of geography and statecraft.", []),
    ("Sacred Geography & Pan-Indian Pilgrimage", "Confluence of holy rivers and mountains binding the subcontinent.", []),
    ("Katapayadi: The Alphanumeric Cipher System", "Encoding astronomical constants and mathematical tables into poetry.", [3, 4]),
    ("Kautilya's Arthashastra: Statecraft and Economics", "Meticulous treatise on public administration, law, and treasury.", []),
    ("Vatsyayana's Kamashastra and the 64 Traditional Arts", "Comprehensive curriculum of aesthetics, music, sculpting, and daily arts.", []),
    ("The Six Darshanas: Classical Systems of Philosophy", "Nyaya, Vaisheshika, Samkhya, Yoga, Mimamsa, and Vedanta.", []),
    ("Classical Drama and Living Traditions of Sanskrit", "Kalidasa, Bhasa, and Bhavabhuti reflecting vibrant social life.", [])
]

ch4_slides = []
for p_idx, (p_title, p_desc, p_tracks) in enumerate(ch4_pages_meta, 1):
    ch4_slides.append({
        "id": p_idx,
        "slideNumber": p_idx,
        "title": p_title,
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "description": p_desc,
        "trackIndices": p_tracks
    })

ch4["slides"] = ch4_slides
ch4["canvas"] = "assets/images/chapter1/chap1page01.jpg"

# Update slideIndex on Chapter 4 audio tracks
for trk_idx, trk in enumerate(ch4["audioTracks"]):
    for s_idx, s in enumerate(ch4_slides):
        if trk_idx in s["trackIndices"]:
            trk["slideIndex"] = s_idx
            break

# Chapter 5: 19 pages (chap5page01 to 19)
ch5 = next(c for c in chapters if c["id"] == 5)
ch5["totalSections"] = 19
ch5_slides = []
for i in range(1, 20):
    ch5_slides.append({
        "id": i,
        "slideNumber": i,
        "title": f"Classical Poetry Manuscript Page {i}",
        "canvas": f"assets/images/chapter5/chap5page{i:02d}.jpg",
        "description": f"Masterpieces of Kalidasa, Valmiki, Vyasa, Bharavi, and Magha.",
        "trackIndices": []
    })

# Assign 31 tracks across 19 pages authentically
ch5_track_page_map = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 4, 6: 5, 7: 5, 8: 6, 9: 7,
    10: 8, 11: 8, 12: 9, 13: 9, 14: 10, 15: 10, 16: 11, 17: 12, 18: 12, 19: 13,
    20: 13, 21: 14, 22: 14, 23: 15, 24: 15, 25: 16, 26: 16, 27: 17, 28: 17, 29: 18, 30: 18
}

for trk_idx, page_idx in ch5_track_page_map.items():
    if trk_idx < len(ch5["audioTracks"]):
        ch5["audioTracks"][trk_idx]["slideIndex"] = page_idx
        ch5_slides[page_idx]["trackIndices"].append(trk_idx)

ch5["slides"] = ch5_slides

# Chapter 6: 9 pages (chapter6page01 to 09)
ch6 = next(c for c in chapters if c["id"] == 6)
ch6["totalSections"] = 9
ch6_slides = []
for i in range(1, 10):
    ch6_slides.append({
        "id": i,
        "slideNumber": i,
        "title": f"Subhashita Wisdom Inscription Page {i}",
        "canvas": f"assets/images/chapter6/chapter6page{i:02d}.jpg",
        "description": f"Condensed ethical wisdom, contentment, friendship, and self-mastery.",
        "trackIndices": []
    })

# Assign 22 tracks across 9 pages authentically
ch6_track_page_map = {
    0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3, 9: 4,
    10: 4, 11: 4, 12: 5, 13: 5, 14: 5, 15: 6, 16: 6, 17: 7, 18: 7, 19: 7, 20: 8, 21: 8
}

for trk_idx, page_idx in ch6_track_page_map.items():
    if trk_idx < len(ch6["audioTracks"]):
        ch6["audioTracks"][trk_idx]["slideIndex"] = page_idx
        ch6_slides[page_idx]["trackIndices"].append(trk_idx)

ch6["slides"] = ch6_slides

# Chapter 7: 15 pages (chap7page01 to 15)
ch7 = next(c for c in chapters if c["id"] == 7)
ch7["totalSections"] = 15
ch7_slides = []
for i in range(1, 16):
    ch7_slides.append({
        "id": i,
        "slideNumber": i,
        "title": f"Sacred Vedic & Upanishadic Revelation Page {i}",
        "canvas": f"assets/images/chapter7/chap7page{i:02d}.jpg",
        "description": f"Vedic hymns, Upanishads, and the Bhagavad Gita.",
        "trackIndices": []
    })

# Assign 40 tracks across 15 pages authentically
ch7_track_page_map = {
    0: 0, 1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 3, 9: 3,
    10: 3, 11: 4, 12: 4, 13: 4, 14: 5, 15: 5, 16: 5, 17: 6, 18: 6, 19: 6,
    20: 7, 21: 7, 22: 7, 23: 8, 24: 8, 25: 8, 26: 9, 27: 9, 28: 9, 29: 10,
    30: 10, 31: 10, 32: 11, 33: 11, 34: 12, 35: 12, 36: 13, 37: 13, 38: 14, 39: 14
}

for trk_idx, page_idx in ch7_track_page_map.items():
    if trk_idx < len(ch7["audioTracks"]):
        ch7["audioTracks"][trk_idx]["slideIndex"] = page_idx
        ch7_slides[page_idx]["trackIndices"].append(trk_idx)

ch7["slides"] = ch7_slides

# Chapter 8: 8 pages
ch8 = next(c for c in chapters if c["id"] == 8)
ch8["totalSections"] = 8
ch8_slides = []
ch8_pages_meta = [
    ("Sanskrit and Indian Languages: The Great Unifying Thread", "Linguistic relationship between Sanskrit and regional Indian tongues."),
    ("Phonetic Roots in Indo-Aryan Vernaculars", "Evolution from Prakrit to Hindi, Bengali, Marathi, and Gujarati."),
    ("Sanskrit and the Dravidian Languages: Cultural Synthesis", "Profuse vocabulary assimilation in Telugu, Kannada, Malayalam, and Tamil."),
    ("The Living Presence in Regional Literature", "Kavyas, devotional songs, and epics inspiring regional poets."),
    ("Sanskrit as the Medium of Pan-Indian Intellectual Life", "Scholarly debates across Kashmir, Kerala, Bengal, and Gujarat."),
    ("The Inflow of Technical and Philosophical Lexicon", "Scientific and medical vocabulary underlying all Indian languages."),
    ("Sanskrit as the Bridge Across Cultural Diversity", "Universal emotional resonance uniting distant regions of India."),
    ("Sir C.V. Raman on Sanskrit: The Scientific Soul of India", "Nobel laureate C.V. Raman on Sanskrit's phonetic and cultural precision.")
]
for p_idx, (p_title, p_desc) in enumerate(ch8_pages_meta, 1):
    slide_entry = {
        "id": p_idx,
        "slideNumber": p_idx,
        "title": p_title,
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "description": p_desc,
        "trackIndices": []
    }
    if p_idx == 8:
        slide_entry["diagram"] = "assets/images/chapter8/raman.jpg"
        slide_entry["diagramTitle"] = "Sir C.V. Raman Historical Portrait"
    ch8_slides.append(slide_entry)
ch8["slides"] = ch8_slides
ch8["canvas"] = "assets/images/chapter1/chap1page01.jpg"

# Chapter 9: 5 pages
ch9 = next(c for c in chapters if c["id"] == 9)
ch9["totalSections"] = 5
ch9_pages_meta = [
    ("Is Sanskrit a 'Dead' Language? The Living Reality", "Challenging modern misconceptions about the vitality of Sanskrit."),
    ("Sir William Jones & The Global Discovery of Indo-European", "The 1786 Asiatic Society discourse on the structure of Sanskrit."),
    ("Is Sanskrit Difficult? Natural Learning Approaches", "How simplified Sanskrit teaching revitalizes natural fluency."),
    ("Daily Expressions and Spoken Sanskrit Revival", "Modern movements demonstrating Sanskrit as a spoken tongue for conversation."),
    ("The Future of Sanskrit in Global Culture", "Its enduring relevance in linguistics, psychology, computer science, and spirituality.")
]
ch9_slides = []
for p_idx, (p_title, p_desc) in enumerate(ch9_pages_meta, 1):
    slide_entry = {
        "id": p_idx,
        "slideNumber": p_idx,
        "title": p_title,
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "description": p_desc,
        "trackIndices": []
    }
    if p_idx == 2:
        slide_entry["diagram"] = "assets/images/chapter9/william jones.jpg"
        slide_entry["diagramTitle"] = "Sir William Jones Historical Portrait"
    elif p_idx == 4:
        slide_entry["diagram"] = "assets/images/chapter9/popup1.jpg"
        slide_entry["diagramTitle"] = "Historical Clarifications Archive"
    ch9_slides.append(slide_entry)
ch9["slides"] = ch9_slides
ch9["canvas"] = "assets/images/chapter1/chap1page01.jpg"

# Chapter 10: 8 pages
ch10 = next(c for c in chapters if c["id"] == 10)
ch10["totalSections"] = 8
ch10_pages_meta = [
    ("Sanskrit: The Eternal Soul of India", "Introduction to Sanskrit as the spiritual and cultural identity of India.", []),
    ("National Motto: Satyameva Jayate (Truth Alone Triumphs)", "Mundaka Upanishad 3.1.6 adopted as India's supreme national seal.", [0]),
    ("The Sacred Geography of Bharata: North to the Snowy Himalayas", "Vishnu Purana description of the sacred land between the mountains and the sea.", [1]),
    ("Rabindranath Tagore on the Universal Spirit of Sanskrit", "Tagore's reflection on Sanskrit literature as India's gift to the world.", []),
    ("The Holy Rivers of India: The Sacred Invocation", "Ganga, Yamuna, Godavari, Saraswati, Narmada, Sindhu, and Kaveri.", []),
    ("Jawaharlal Nehru on the Living Heritage of Sanskrit", "Nehru's testament in The Discovery of India on the genius of Sanskrit.", []),
    ("Invocation to Sthanu: Mahakavi Kalidasa's Opening Prayer", "Vikramorvashiyam 1.1 invocation to the eternal Lord Shiva.", [2]),
    ("The Eternal Dawn: Preserving the Heritage for Future Generations", "Concluding celebration of Devabhasha across millennia.", [])
]
ch10_slides = []
for p_idx, (p_title, p_desc, p_tracks) in enumerate(ch10_pages_meta, 1):
    slide_entry = {
        "id": p_idx,
        "slideNumber": p_idx,
        "title": p_title,
        "canvas": "assets/images/chapter1/chap1page01.jpg",
        "description": p_desc,
        "trackIndices": p_tracks
    }
    if p_idx == 4:
        slide_entry["diagram"] = "assets/images/chapter10/tagore.jpg"
        slide_entry["diagramTitle"] = "Rabindranath Tagore Historical Portrait"
    elif p_idx == 6:
        slide_entry["diagram"] = "assets/images/chapter10/nehru.jpg"
        slide_entry["diagramTitle"] = "Jawaharlal Nehru Historical Portrait"
    ch10_slides.append(slide_entry)
ch10["slides"] = ch10_slides
ch10["canvas"] = "assets/images/chapter1/chap1page01.jpg"

# Update slideIndex on Chapter 10 audio tracks
for trk_idx, trk in enumerate(ch10["audioTracks"]):
    for s_idx, s in enumerate(ch10_slides):
        if trk_idx in s["trackIndices"]:
            trk["slideIndex"] = s_idx
            break

# Save updated canonical database
with open(DATA_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully updated content/data.json to authentic 125-page baseline!")
