from deep_translator import GoogleTranslator

def translate(input_text, lang="en"):
    return GoogleTranslator(source='auto', target=lang).translate(input_text)

texts = ["Labdien! Kā jums klājas?", "Es šodien lasīju interesantu grāmatu."]

for text in texts:
    translated = translate(text)  # Tulkojam tekstu
    print(f"Original Text: {text} \t Translated: {translated}")
