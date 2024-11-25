from sentence_transformers import SentenceTransformer
import numpy as np
from deep_translator import GoogleTranslator

# Ielādējam iepriekš apmācīto daudzvalodu modeli
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def translate_array(array):
    # Funkcija, kas tulko vārdu sarakstu uz angļu valodu
    res = []
    for el in array:
        # Tulkojam katru vārdu, automātiski nosakot avota valodu
        res_el = GoogleTranslator(source='auto', target='en').translate(el)
        res.append(res_el)
    return res

def get_word_vectors(words, model):
    # Iegūstam katra vārda vektora reprezentāciju, izmantojot modeli
    embeddings = {word: model.encode(word) for word in words}
    return embeddings

def calculate_similarity(vector1, vector2):
    # Aprēķinām kosinusa līdzību starp diviem vektoriem
    similarity = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    return similarity

# Sākotnējie vārdi latviešu valodā
words = ["māja", "dzīvoklis", "jūra"]

# Tulkojam vārdus uz angļu valodu
words_translated = translate_array(words)  # Tulkojam vārdus angļu valodā

# Iegūstam vārdu vektorus, izmantojot iepriekš apmācīto modeli
word_vectors = get_word_vectors(words_translated, model)  # Iegūstam vektorus

# Aprēķinām līdzības starp vārdiem
similarities = {}
for i, word1 in enumerate(words_translated):
    for word2 in words_translated[i + 1:]:
        # Aprēķinām līdzību starp diviem vārdiem
        similarity = calculate_similarity(word_vectors[word1], word_vectors[word2])
        similarities[(word1, word2)] = similarity

# Izdrukājam vārdu vektorus
print("Word Vectors:")
for word, vector in word_vectors.items():
    print(f"{word}: {vector[:5]}... (truncated)")  # Parādām tikai pirmās 5 komponentes

print("\nWord Similarities:")
# Izdrukājam līdzības starp vārdu pāriem
for word_pair, similarity in similarities.items():
    print(f"Similarity between '{word_pair[0]}' and '{word_pair[1]}': {similarity:.4f}")
