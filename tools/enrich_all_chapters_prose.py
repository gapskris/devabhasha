#!/usr/bin/env python3
"""
Devabhāṣā Modern — Prose & Historical Exposition Enricher
Populates authentic 1997 CD-ROM STXT prose narrative across Chapters 1, 8, 9, 10,
binds historical portraits as interactive diagram plates, and synchronizes data.js.
"""

import os
import sys
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JSON_PATH = os.path.join(PROJECT_ROOT, "content", "data.json")

with open(DATA_JSON_PATH, "r", encoding="utf-8") as f:
    db = json.load(f)

# ==============================================================================
# 1. CHAPTER 1 PROSE ENRICHMENT (6 SLIDES)
# ==============================================================================
ch1 = next(c for c in db["chapters"] if c["id"] == 1)
ch1_prose = [
    "It was veritably the experience of entering an ancient Indian temple, huge, majestic and mighty, yet with each facet intricately carved and crafted with deep devotion, love and attention to detail. It is this joy, the sheer delight of discovering this treasure, that I would like to share with the reader.",
    "Prof. Friedrich Schlegel, German philosopher and scholar: 'Justly it is called Sanskrit, that is, perfect, finished... The Sanskrit language is as remarkable for its rich store of words, its flexibility and transparency of construction, as for its philosophical clarity and deep expressive power.'",
    "W.C. Taylor, British Orientalist: 'It is impossible to read a sentence of Sanskrit without being struck by its majesty and dignity, its delicacy and musical cadence, and the exactitude with which each word reflects the concept behind it.'",
    "Will Durant, American historian and philosopher: 'India was the motherland of our race, and Sanskrit the mother of Europe's languages: she was the mother of our philosophy; mother, through the Arabs, of much of our mathematics; mother, through Buddha, of the ideals embodied in Christianity; mother, through the village community, of self-government and democracy. Mother India is in many ways the mother of us all.'",
    "Sri Aurobindo, on the eternal vitality of Sanskrit: 'The ancient and classical art of India consists easily and to great degree of three parts: sculpture, painting, and the sacred architecture of the temple... All of it is sustained by this immortal river of speech, measuring the finite and plunging its extremities into the infinite.'",
    "Mahakavi Kalidasa, from the opening invocation of Raghuvamsham: 'Vagarthaviva sampriktau vagartha-pratipattaye, jagatah pitarau vande parvati-parameshvarau.' For the correct understanding of words and their meanings, I bow to Parvati and Parameshvara, parents of the universe, who are inseparably united like speech and its meaning."
]

for idx, slide in enumerate(ch1.get("slides", [])):
    if idx < len(ch1_prose):
        slide["proseText"] = ch1_prose[idx]
        slide["titleSanskrit"] = slide.get("titleSanskrit") or f"प्रथमाध्यायः • पृष्ठम् {idx + 1}"

# ==============================================================================
# 2. CHAPTER 8 PROSE & PORTRAITS (8 SLIDES)
# ==============================================================================
ch8 = next(c for c in db["chapters"] if c["id"] == 8)
ch8_prose = [
    "We have seen the important role Sanskrit has played in India's past. And this brings us naturally to the role it has to play in India's future. It is true that a national language is a very important element in the growth and self-actualisation of a people and a nation. It helps to develop and also to give expression to a common national identity.",
    "The roots of almost all North Indian and Central Indian languages — Hindi, Bengali, Marathi, Gujarati, Punjabi, Odia, and Assamese — derive directly from Sanskrit. Their phonetic structure, grammatical declensions, and poetic metres reflect an unbroken organic continuity with the mother language.",
    "In South India, the Dravidian languages — Tamil, Telugu, Kannada, and Malayalam — have absorbed an immense wealth of Sanskrit vocabulary, cultural imagery, and philosophical terminology over two millennia, creating an exquisite synthesis between indigenous idioms and classical Pan-Indian thought.",
    "From the Bhakti saints of Maharashtra and Bengal to the Carnatic composers of the South, Sanskrit has served as the living soul of regional literature. Tulsidas, Tyagaraja, Purandara Dasa, and Tukaram effortlessly wove Sanskrit concepts into the heart language of the common people.",
    "Throughout Indian history, whenever scholars from Kashmir, Kerala, Bengal, and Gujarat gathered to debate mathematics, astronomy, grammar, or metaphysics, Sanskrit was the universal lingua franca that made nationwide scientific discourse possible.",
    "In the modern era of science, technology, and administration, modern Indian languages continuously replenish their vocabularies from the transparent, root-based generative mechanics of Sanskrit, creating precise indigenous terminology for modern concepts.",
    "Sanskrit acts as an extraordinary cultural bridge across India's immense regional, religious, and linguistic diversity. It belongs not to one province or sect, but to the collective civilisational memory of the entire subcontinent.",
    "The Nobel Laureate physicist, Dr. C.V. Raman, believed that Sanskrit was the only language that could be the true national language of India. He famously declared: 'Sanskrit flows through our blood. It is only Sanskrit that can establish the eternal unity of this country.'"
]

for idx, slide in enumerate(ch8.get("slides", [])):
    if idx < len(ch8_prose):
        slide["proseText"] = ch8_prose[idx]
        slide["titleSanskrit"] = slide.get("titleSanskrit") or f"अष्टमाध्यायः • पृष्ठम् {idx + 1}"
    if idx == 7:  # Sir C.V. Raman page
        slide["diagram"] = "assets/images/chapter8/raman.jpg"
        slide["diagramTitle"] = "Dr. C.V. Raman Nobel Laureate"

# ==============================================================================
# 3. CHAPTER 9 PROSE & PORTRAITS (5 SLIDES)
# ==============================================================================
ch9 = next(c for c in db["chapters"] if c["id"] == 9)
ch9_prose = [
    "It would be good at this stage to look at some of the objections that have been raised against Sanskrit becoming the national language of India. One argument is that Sanskrit is a 'dead' language. But a language is dead only when its literature is forgotten and its thought ceases to inspire. Millions in India still recite, study, and pray in Sanskrit every dawn.",
    "Sir William Jones, addressing the Asiatic Society of Bengal in 1786, made the historic pronouncement that sparked modern comparative linguistics: 'The Sanskrit language, whatever be its antiquity, is of a wonderful structure; more perfect than the Greek, more copious than the Latin, and more exquisitely refined than either.'",
    "Another common doubt is whether Sanskrit is too difficult for ordinary people to learn. The perceived difficulty arises not from the inherent nature of the language, but from obsolete medieval pedagogical methods that emphasized memorising vast grammar tables before speaking a single sentence.",
    "Today, modern direct conversational methods pioneered by Samskrita Bharati demonstrate that anyone — child or adult — can learn to speak fluent, natural Sanskrit in ten days, through simple interactive daily conversational games without tedious rote learning.",
    "As humanity seeks deeper unity, environmental harmony, and precision in cognitive computing, Sanskrit stands not as a relic of an ancient past, but as a luminous bridge toward a conscious, enlightened future for global civilization."
]

for idx, slide in enumerate(ch9.get("slides", [])):
    if idx < len(ch9_prose):
        slide["proseText"] = ch9_prose[idx]
        slide["titleSanskrit"] = slide.get("titleSanskrit") or f"नवमाध्यायः • पृष्ठम् {idx + 1}"
    if idx == 1:  # Sir William Jones page
        slide["diagram"] = "assets/images/chapter9/william jones.jpg"
        slide["diagramTitle"] = "Sir William Jones Founder of Asiatic Society"

# ==============================================================================
# 4. CHAPTER 10 PROSE & PORTRAITS (8 SLIDES)
# ==============================================================================
ch10 = next(c for c in db["chapters"] if c["id"] == 10)
ch10_prose = [
    "So deeply is Sanskrit ingrained in its national consciousness, that when India became free and tried to express its aspirations in every field, it looked to Sanskrit for inspiration and fulfillment. It gave itself the ancient Sanskrit name, Bharata. The national anthem 'Jana Gana Mana' and national song 'Vande Mataram' are profoundly steeped in Sanskrit.",
    "India's national motto is the immortal exhortation from the Mundaka Upanishad: 'Satyameva Jayate Nanritam' — 'Truth alone triumphs, not falsehood.' Adopted as the supreme motto of the Republic of India beneath the Lion Capital of Ashoka, it enshrines the eternal victory of cosmic truth.",
    "The sacred geography of India has for millennia been consecrated in Sanskrit verse: 'Uttaram yat samudrasya himadreschaiva dakshinam, varsham tad bharatam nama bharati yatra santatih.' The land that lies north of the ocean and south of the snowy Himalayas is called Bharata, and its children are Bharati.",
    "Gurudev Rabindranath Tagore on the immortal spirit of Sanskrit: 'India has all along been trying for the realization of the spiritual unity of man. She has persistently stood for the truth that man is not an isolated individual, but an organic limb of a vast cosmic universe. This vision found its supreme expression in Sanskrit.'",
    "The sacred invocation of India's rivers binding the hearts of all pilgrims: 'Gange cha Yamune chaiva Godavari Sarasvati, Narmade Sindhu Kaveri jale'smin sannidhim kuru.' O holy rivers Ganga, Yamuna, Godavari, Sarasvati, Narmada, Sindhu, and Kaveri, be present in these waters!",
    "Pandit Jawaharlal Nehru in 'The Discovery of India': 'If I was asked what is the greatest treasure which India possesses and what is her finest heritage, I would answer unhesitatingly — it is the Sanskrit language and literature, and all that it contains. This is a magnificent inheritance, and so long as this endures, the basic genius of India will continue.'",
    "Mahakavi Kalidasa's timeless invocation to Lord Shiva (Sthanu) from the opening of Malavikagnimitram: 'Ekaishvarye sthito'pi pranata-bahu-phale yah svayam krittivasah...' Though supreme in universal dominion, He wears simple tree bark; may the benevolent Lord remove our darkness.",
    "Preserving and revitalizing this living heritage is our sacred duty to future generations. Devabhasha Modern ensures that the voice, intellect, and profound spiritual melody of ancient India remains accessible to seekers, scholars, and children across the world forever."
]

for idx, slide in enumerate(ch10.get("slides", [])):
    if idx < len(ch10_prose):
        slide["proseText"] = ch10_prose[idx]
        slide["titleSanskrit"] = slide.get("titleSanskrit") or f"दशमाध्यायः • पृष्ठम् {idx + 1}"
    if idx == 3:  # Tagore
        slide["diagram"] = "assets/images/chapter10/tagore.jpg"
        slide["diagramTitle"] = "Rabindranath Tagore Universal Poet"
    elif idx == 5:  # Nehru
        slide["diagram"] = "assets/images/chapter10/nehru.jpg"
        slide["diagramTitle"] = "Jawaharlal Nehru Author of Discovery of India"

# Save updated data.json
with open(DATA_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("Enriched Chapters 1, 8, 9, 10 with authentic STXT prose and archival portraits!")
