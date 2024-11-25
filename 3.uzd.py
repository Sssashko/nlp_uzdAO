import string

# Dotie teksti
text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

def process_text(text):
    text = text.lower()  # Mazie burti
    text = text.translate(str.maketrans('', '', string.punctuation))  # Noņem pieturzīmes
    words = text.split()  # Sadalām vārdos
    return words

words1 = process_text(text1)
words2 = process_text(text2)

set1 = set(words1)  # Unikālie vārdi pirmajā tekstā
set2 = set(words2)  # Unikālie vārdi otrajā tekstā

common_words = set1.intersection(set2)  # Kopīgie vārdi

unique_words = set1.union(set2)  # Visi unikālie vārdi

similarity_percentage = (len(common_words) / len(unique_words)) * 100  # Sakritības procents

# Izdrukājam rezultātus
print("Kopīgie vārdi starp abiem tekstiem:")
print(common_words)
print(f"Sakritības līmenis: {similarity_percentage:.2f}%")
