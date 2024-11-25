from deep_translator import GoogleTranslator
from lingua import LanguageDetectorBuilder

from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

import nltk
# Lejupielādējam nepieciešamos NLTK resursus
nltk.download('stopwords')
nltk.download('punkt')

# Inicializējam valodas detektoru
detector = LanguageDetectorBuilder.from_all_languages().with_preloaded_language_models().build()

def summarize_text(article):
    # Nosakām raksta valodu
    input_language = detector.detect_language_of(article).iso_code_639_1.name.lower()
    # Tulkojam rakstu uz angļu valodu
    input_translation = GoogleTranslator(source=input_language, target='en').translate(article)
    
    # Sadalām tulkoto tekstu teikumos
    sentences = sent_tokenize(input_translation)
    # Sadalām vārdus un pārveidojam uz mazajiem burtiem
    words = word_tokenize(input_translation.lower())
    # Noņemam stopvārdus un atstājam tikai alfabētiskos vārdus
    words = [word for word in words if word.isalnum() and word not in stopwords.words()]
    
    # Aprēķinām vārdu frekvenču sadalījumu
    freq_dist = FreqDist(words)
    
    # Vērtējam katra teikuma nozīmīgumu
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist:
                # Summējam vārdu frekvences teikumā
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq_dist[word]
    
    # Kārtojam teikumus pēc to vērtējuma
    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    
    # Izvēlamies noteiktu skaitu (piemēram, 2) svarīgākos teikumus
    summary = " ".join(ranked_sentences[:2])
    
    # Tulkojam kopsavilkumu atpakaļ uz sākotnējo valodu
    output_translate = GoogleTranslator(source='en', target=input_language).translate(summary)
    
    return output_translate

# Raksts rezumēšanai
article = (
    "Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm."
)

# Izsaucam funkciju un izdrukājam kopsavilkumu
summary = summarize_text(article)
print("Kopsavilkums:", summary)
