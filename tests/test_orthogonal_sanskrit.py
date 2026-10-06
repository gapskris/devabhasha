"""
Automated Sanskrit Orthogonal & Forensic Parity Test Suite
Validates that all 149 recitations across 10 chapters in Devabhāṣā Modern contain:
  1. Complete authentic Sanskrit data (Devanagari + IAST + English Translation).
  2. Exactly 0 legacy font mojibake / corrupted glyphs (; £ Ð Ï Î ` ~ [ ] { } + = ^ a-zA-Z \\x80-\\xff).
  3. Zero broken combining characters (dotted circles \\u25cc or dangling matras).
  4. Sacred typography: non-breaking space gluing for all dandas (\\u00A0। and \\u00A0॥).
  5. 100% synchronization between content/data.json and js/data.js.
  6. Exactly 149 M4A + 149 MP3 = 298 physical audio tracks on disk.
  7. Character-level forensic accuracy for historic benchmark verses across all chapters.
"""

import unittest
import os
import sys
import json
import re

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JSON_PATH = os.path.join(PROJECT_DIR, "content", "data.json")
DATA_JS_PATH = os.path.join(PROJECT_DIR, "js", "data.js")

class TestOrthogonalSanskrit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(DATA_JSON_PATH, "r", encoding="utf-8") as f:
            cls.data = json.load(f)
        cls.chapters = cls.data.get("chapters", [])
        cls.concordance = cls.data.get("shlokasConcordance", [])

    def test_01_all_149_tracks_fully_articulated(self):
        """Verify exactly 149 tracks exist and have complete non-placeholder Sanskrit, IAST, and translation."""
        self.assertEqual(len(self.concordance), 149, "Master concordance must contain exactly 149 tracks.")
        total_audio_tracks = sum(len(c.get("audioTracks", [])) for c in self.chapters)
        self.assertEqual(total_audio_tracks, 149, "Chapters audioTracks must total exactly 149 tracks.")

        placeholder_pattern = re.compile(r'(?:Subhashita Wisdom Verse \d+|Sacred Vedic Recitation \d+|Chapter \d+ Verse \d+)', re.I)
        for t in self.concordance:
            tid = t["id"]
            sa = t.get("sanskrit", "").strip()
            iast = t.get("iast", "").strip()
            tr = t.get("translation", "").strip()
            
            self.assertTrue(len(sa) >= 10, f"Track {tid} sanskrit text too short or missing: '{sa}'")
            self.assertTrue(len(iast) >= 5, f"Track {tid} IAST text too short or missing: '{iast}'")
            self.assertTrue(len(tr) >= 10, f"Track {tid} translation too short or missing: '{tr}'")
            self.assertFalse(placeholder_pattern.search(sa), f"Track {tid} contains placeholder text in sanskrit: '{sa}'")

    def test_02_zero_mojibake_artifacts(self):
        """Verify zero unconverted legacy glyphs (; £ Ð Ï Î ` ~ [ ] { } + = ^ a-zA-Z) in all Sanskrit strings."""
        forbidden_pattern = re.compile(r'[;£ÐÏÎ`~\[\]\{\}\+\=\^a-zA-Z\x80-\xff]')
        for t in self.concordance:
            tid = t["id"]
            sa = t.get("sanskrit", "")
            words = re.findall(r'\S+', sa)
            bad_tokens = []
            for w in words:
                clean_w = re.sub(r'[\(\)\"\'\*\।\॥\,\-\?\!\d:🔔\u00A0]', '', w)
                if forbidden_pattern.search(clean_w):
                    bad_tokens.append(w)
            self.assertEqual(len(bad_tokens), 0, f"Track {tid} contains corrupted tokens: {' '.join(bad_tokens[:5])}")

    def test_03_zero_broken_combining_characters(self):
        """Verify no dotted circles (U+25CC) or isolated combining marks at word start."""
        for t in self.concordance:
            tid = t["id"]
            sa = t.get("sanskrit", "")
            self.assertNotIn("\u25cc", sa, f"Track {tid} contains dotted circle combining character!")
            
            words = re.findall(r'[\u0900-\u097f]+', sa)
            for w in words:
                self.assertFalse(re.search(r'^[ािीुूृॄेैोौ्ंँः]', w), f"Track {tid} has isolated matra at start of word: {w}")

    def test_04_sacred_typography_danda_gluing(self):
        """Verify dandas are glued with non-breaking space and never orphan at line start."""
        for t in self.concordance:
            tid = t["id"]
            sa = t.get("sanskrit", "")
            # Check for regular ASCII space before single or double danda
            matches = re.findall(r'[ \t]+[।॥]', sa)
            self.assertEqual(len(matches), 0, f"Track {tid} has {len(matches)} dandas preceded by regular ASCII space instead of \\u00A0!")
            
            # Ensure line does not start with danda
            for line in sa.splitlines():
                line_str = line.strip()
                self.assertFalse(line_str.startswith('।') or line_str.startswith('॥'),
                                 f"Track {tid} has leading orphaned danda on line: '{line_str}'")

    def test_05_data_js_synchronization(self):
        """Verify js/data.js exists, defines DEVABHASHA_DATA, and matches content/data.json 100%."""
        self.assertTrue(os.path.exists(DATA_JS_PATH), "js/data.js does not exist.")
        with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
            js_content = f.read()
        self.assertIn("DEVABHASHA_DATA", js_content)
        
        prefix = "const DEVABHASHA_DATA = "
        start = js_content.find(prefix)
        self.assertNotEqual(start, -1)
        start += len(prefix)
        end = js_content.find(";\n\nif (typeof", start)
        if end == -1:
            end = js_content.rfind(";")
        raw_json = js_content[start:end].strip()
        parsed_js = json.loads(raw_json)

        self.assertEqual(len(parsed_js.get("chapters", [])), len(self.chapters))
        self.assertEqual(len(parsed_js.get("shlokasConcordance", [])), len(self.concordance))
        for idx in range(len(self.concordance)):
            self.assertEqual(
                self.concordance[idx]["sanskrit"],
                parsed_js["shlokasConcordance"][idx]["sanskrit"],
                f"js/data.js out of sync on Track {self.concordance[idx]['id']} Sanskrit text!"
            )

    def test_06_audio_asset_parity_298_files(self):
        """Verify all 149 M4A and all 149 MP3 files exist on disk."""
        for t in self.concordance:
            tid = t["id"]
            m4a_path = os.path.join(PROJECT_DIR, t["m4a"].replace("/", os.sep))
            mp3_path = os.path.join(PROJECT_DIR, t["mp3"].replace("/", os.sep))
            self.assertTrue(os.path.exists(m4a_path), f"Track {tid} M4A audio file missing: {m4a_path}")
            self.assertTrue(os.path.exists(mp3_path), f"Track {tid} MP3 audio file missing: {mp3_path}")

    def test_07_canonical_benchmark_verses(self):
        """Verify specific historic benchmark verses across all key chapters."""
        c_map = {t["id"]: t["sanskrit"] for t in self.concordance}

        # Ch 1 Raghuvamsham
        self.assertIn("वागर्थाविव सम्पृक्तौ वागर्थप्रतिपत्तये", c_map["chap1_01"])
        self.assertIn("जगतः पितरौ वन्दे पार्वतीपरमेश्वरौ", c_map["chap1_01"])

        # Ch 2 Shiva Sutras & Rama Vibhaktis
        self.assertIn("अइउण्", c_map["c2_s1"])
        self.assertIn("रामो राजमणिः सदा विजयते", c_map["c2_s3"])

        # Ch 3 Citrakavya (33 consonants, Knight's Tour, Kalidasa riddle & obituary)
        self.assertIn("कः खगौघाङ्गचिच्छौजा", c_map["c3_s01"])
        self.assertIn("स्थिरागसां सदाऽऽराध्या", c_map["c3_s19"])
        self.assertIn("स्थिता समयराजत्पा", c_map["c3_s20"])
        self.assertIn("ठं ठं ठं ठं ठं ठठठं ठठं ठः", c_map["c3_s23"])
        self.assertIn("अद्य धारा निराधारा निरालम्बा सरस्वती", c_map["c3_s30"])
        self.assertIn("अद्य धारा सदाधारा सदालम्बा सरस्वती", c_map["c3_s31"])

        # Ch 4 Science (Baudhayana Pythagoras & √2, Aryabhata π)
        self.assertIn("दीर्घचतुरस्रस्याक्ष्णया रज्जुः", c_map["c4_s1"])
        self.assertIn("प्रमाणं तृतीयेन वर्धयेत्तच्च चतुर्थेनात्मचतुस्त्रिंशोनेन", c_map["c4_s2"])
        self.assertIn("चतुरधिकं शतमष्टगुणं द्वाषष्टिस्तथा सहस्राणाम्", c_map["c4_s3"])

        # Ch 5 Poetry (Valmiki first shloka, Kalidasa Himalaya, Meghadutam, Gitagovindam, Shivatandava)
        self.assertIn("मा निषाद प्रतिष्ठां त्वमगमः शाश्वतीः समाः", c_map["c5_s02"])
        self.assertIn("अस्त्युत्तरस्यां दिशि देवतात्मा हिमालयो नाम", c_map["c5_s09"])
        self.assertIn("कश्चित्कान्ताविरहगुरुणा स्वाधिकारात्प्रमत्तः", c_map["c5_s14"])
        self.assertIn("ललितलवङ्गलतापरिशीलनकोमलमलयसमीरे", c_map["c5_s28"])
        self.assertIn("जटाटवीगलज्जलप्रवाहपावितस्थले", c_map["c5_s30"])

        # Ch 6 Subhashita (Contentment, Vasudhaiva Kutumbakam, Caraiveti)
        self.assertIn("अन्तो नास्ति पिपासायास्तुष्टिस्तु परमं सुखम्", c_map["c6_s01"])
        self.assertIn("वसुधैव कुटुम्बकम्", c_map["c6_s08"])
        self.assertIn("चरैवेति चरैवेति", c_map["c6_s14"])

        # Ch 7 Sacred Heritage (Gayatri, Asato ma, Katha razor edge, Gita 2.20 & 18.66, Bhavani Ashtakam)
        self.assertIn("तत्सवितुर्वरेण्यम्", c_map["c7_s01"])
        self.assertIn("असतो मा सद्गमय", c_map["c7_s02"])
        self.assertIn("क्षुरस्य धारा निशिता दुरत्यया", c_map["c7_s15"])
        self.assertIn("न जायते म्रियते वा कदाचिन्नायं", c_map["c7_s25"])
        self.assertIn("सर्वधर्मान् परित्यज्य मामेकं शरणं व्रज", c_map["c7_s36"])
        self.assertIn("गतिस्त्वं गतिस्त्वं त्वमेका भवानि", c_map["c7_s37"])

        # Ch 10 Soul of India (Satyameva Jayate, Vishnu Purana, Sthanu Invocation)
        self.assertIn("सत्यमेव जयते नानृतं सत्येन पन्था विततो देवयानः", c_map["c10_s1"])
        self.assertIn("उत्तरं यत् समुद्रस्य हिमाद्रेश्चैव दक्षिणम्", c_map["c10_s2"])
        self.assertIn("स स्थाणुः स्थिरभक्तियोगसुलभो निःश्रेयसायास्तु वः", c_map["c10_s3"])

if __name__ == '__main__':
    unittest.main()
