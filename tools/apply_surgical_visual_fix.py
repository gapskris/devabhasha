import json

def run_fix():
    with open('content/data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Update Chapter 1 slides
    ch1 = data['chapters'][0]
    scholar_data = [
        {
            'slideNumber': 1,
            'trackIndex': None,
            'trackIndices': [],
            'title': 'Entering the Ancient Temple of Speech',
            'titleSanskrit': 'पुरातन-संस्कृत-मन्दिर-प्रवेशः — वाग्देव्याः परिचयः',
            'proseTextSanskrit': 'वस्तुतो महतः प्राचीनस्य भारतीय-मन्दिरस्य गर्भगृह-प्रवेशानुभूतिरिवैषा। यत्र गम्भीरता, पवित्रता, युग-युगान्तर-व्यापिनी महिमा च युगपदेव हृदयावर्जकं प्रकाशन्ते। संस्कृतं हि नाम दैवी वाक्, सर्वासां भाषाणां जननी, मानवीय-प्रज्ञायाश्च चिरन्तनः आलोकः।',
            'proseText': 'It was veritably the experience of entering an ancient Indian temple, huge, majestic, solemn, serene, offering divine light to all seekers of wisdom. Sanskrit is not merely a language of communication, but the Divine Mother of all tongues, the sacred bridge connecting mortal thought with eternal truth.'
        },
        {
            'slideNumber': 2,
            'trackIndex': None,
            'trackIndices': [],
            'title': 'Prof. Friedrich Schlegel — An Enthralling Discovery',
            'titleSanskrit': 'फ्रेडरिख श्लेगेल — संस्कृत-भाषायाः प्रातिभ-माहात्म्यम्',
            'proseTextSanskrit': 'जर्मन-दार्शनिकः फ्रेडरिख श्लेगेलः आह: "यथार्थमेव संस्कृतं देववाणीत्युच्यते। अस्याः भाषायाः सुस्पष्टं व्याकरणं, समृद्धः शब्दनिधिः, अलौकिकी च अभिव्यक्ति-शक्तिः मानव-मनसो महत्तमा सृष्टिः।" भाषाविदां मते संस्कृतस्य संरचनायां सौन्दर्यस्य तत्त्वज्ञानस्य च अनुपमः सङ्गमः परिदृश्यते।',
            'proseText': 'Prof. Friedrich Schlegel, German philosopher and scholar: "Justly it is called Sanskrit, that is, perfect and cultivated. The clear grammatical structure, the philosophical richness, and the unparalleled phonetic precision make it one of the greatest masterpieces of the human intellect."'
        },
        {
            'slideNumber': 3,
            'trackIndex': None,
            'trackIndices': [],
            'title': 'W.C. Taylor — Delicacy & Philosophy',
            'titleSanskrit': 'डब्ल्यू. सी. टेलर — भाषायाः लालित्यं गाम्भीर्यं च',
            'proseTextSanskrit': 'ब्रिटिश-विपश्चित् डब्ल्यू. सी. टेलरः प्रतिपादयति: "संस्कृतस्य किमपि वाक्यं पठन् को वा जनः अस्याः भाषायाः अपूर्वेण माधुर्येण, सूक्ष्मतया, दार्शनिक-गाम्भीर्येण च विस्मितो न भवेत्। इयं भाषा केवलं सम्भाषणाय न, अपितु आत्माभिव्यक्तये एव देवैः निर्मितेव प्रतीयते।"',
            'proseText': 'W.C. Taylor, British Orientalist: "It is impossible to read a sentence of Sanskrit without being struck by its exquisite harmony, its delicate nuance, and its profound philosophical gravity."'
        },
        {
            'slideNumber': 4,
            'trackIndex': None,
            'trackIndices': [],
            'title': 'Will Durant — Mother of Languages',
            'titleSanskrit': 'विल ड्युरान्ट — सर्वासां भाषाणां माता भारतभूमिः',
            'proseTextSanskrit': 'इतिहासकारः विल ड्युरान्टः अवदत्: "भारतवर्षं हि अस्माकं जातेः मातृभूमिः, संस्कृतं च यूरोपीय-भाषाणां जननी। अस्माकं दर्शनस्य, गणितानां, विज्ञानस्य च मूलस्रोतांसि अत्रैव विभाव्यन्ते।"',
            'proseText': 'Will Durant, American historian and philosopher: "India was the motherland of our race and Sanskrit the mother of Europe\'s languages. She was the mother of our philosophy, our mathematics, and our deepest scientific traditions."'
        },
        {
            'slideNumber': 5,
            'trackIndex': None,
            'trackIndices': [],
            'title': 'Sri Aurobindo — The Living River of Antiquity',
            'titleSanskrit': 'श्रीअरविन्दः — संस्कृतस्य नित्या सजीवता',
            'proseTextSanskrit': 'श्रीअरविन्दानां दिव्य-वचनम्: "प्राचीना शास्त्रीया च संस्कृत-साहित्य-सम्पद् न केवलं समृद्धतमा, अपितु आध्यात्मिक-चेतनायाः परम-प्रकाशिका। अस्याः धारायाम् अनन्तस्य सत्यस्य, ऋतस्य, ब्रह्मणश्च सजीवं साक्षात्कारं लभते मानवता।"',
            'proseText': 'Sri Aurobindo, on the eternal vitality of Sanskrit: "The ancient and classical creations of Sanskrit literature are the expression of a magnificent culture, of a spirituality that touches both highest heaven and broadest earth."'
        },
        {
            'slideNumber': 6,
            'trackIndex': 0,
            'trackIndices': [0],
            'title': 'Mahakavi Kalidasa — Awakening of Modern India',
            'titleSanskrit': 'महाकवि-कालिदासः — रघुवंशस्य मङ्गलाचरणम्',
            'proseTextSanskrit': 'महाकवेः कालिदासस्य रघुवंश-महाकाव्यस्य मङ्गलाचरण-श्लोकः — वागर्थप्रतिपत्तये जगत्पितरौ वन्दे पार्वतीपरमेश्वरौ।',
            'proseText': 'Mahakavi Kalidasa, from the opening invocation of Raghuvamsham: "Vagarthaviva sampriktau vagartha-pratipattaye, Jagatah pitarau vande Parvati-Parameshvarau." Celebrating the divine unity of word and meaning through Lord Shiva and Goddess Parvati.'
        }
    ]

    for idx, sd in enumerate(scholar_data):
        ch1['slides'][idx].update(sd)

    # 2. Update Chapters 3, 8, 9, 10 canvas and slide canvases to back.jpg
    parchment_canvas = 'assets/images/acknowledge/back.jpg'

    for ch in data['chapters']:
        cid = ch['id']
        if cid in [3, 8, 9, 10]:
            ch['canvas'] = parchment_canvas
            for s in ch.get('slides', []):
                s['canvas'] = parchment_canvas

    # In Chapter 3 Slide 1, set diagram to kalidas.jpg
    ch3 = [c for c in data['chapters'] if c['id'] == 3][0]
    ch3['slides'][0]['diagram'] = 'assets/images/chap03/kalidas.jpg'
    ch3['slides'][0]['diagramTitle'] = 'Mahakavi Kalidasa Archival Portrait'
    ch3['slides'][0]['titleSanskrit'] = 'चित्रकाव्य-परिचयः — महाकवि-कालिदासः'
    ch3['slides'][0]['proseTextSanskrit'] = 'चित्रकाव्यं नाम संस्कृत-काव्यशास्त्रस्य सा विशिष्टा विधा यत्र कवेः अलौकिकं पाण्डित्यम्, आश्चर्यकरा चित्र-रचना, गूढं बन्ध-विधानं च परिदृश्यन्ते। कालिदासादयः महाकवयः शब्दार्थयोः परमां पराकाष्ठां साधयन्ति।'
    ch3['slides'][0]['proseText'] = 'Chitrakavya represents the pinnacle of Sanskrit poetic ingenuity, where verses form intricate geometric patterns and visual arrays while maintaining profound philosophical and aesthetic depth.'

    with open('content/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print('Successfully updated content/data.json')

if __name__ == '__main__':
    run_fix()
