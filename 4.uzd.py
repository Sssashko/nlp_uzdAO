# Pozitīvo un negatīvo vārdu saraksti
positive_words = ['lielisks', 'apmierināts', 'patīk', 'labs', 'brīnišķīgs', 'pozitīvs']
negative_words = ['vīlies', 'neapmierināts', 'slikts', 'negatīvs', 'nepatīk']

# Dotie teikumi
sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

def sentiment_analysis(sentence):
    sentence_lower = sentence.lower()
    positive_count = sum(word in sentence_lower for word in positive_words)
    negative_count = sum(word in sentence_lower for word in negative_words)
    if positive_count > negative_count:
        return 'Pozitīvs'
    elif negative_count > positive_count:
        return 'Negatīvs'
    else:
        return 'Neitrāls'

# Izdrukājam noskaņojumu katram teikumam
for sentence in sentences:
    result = sentiment_analysis(sentence)
    print(f"Teikums: '{sentence}'")
    print(f"Noskaņojums: {result}\n")
