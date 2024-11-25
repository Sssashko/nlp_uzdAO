import nltk
from nltk.tokenize import RegexpTokenizer
from collections import Counter

text = """
Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas.
Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem.
"""

text = text.lower()  # Mazie burti

tokenizer = RegexpTokenizer(r'\w+')
names = tokenizer.tokenize(text)  # Tokenizē

name_ccounter = Counter(names)  # Vārdu biežums

# Izdrukā rezultātus
for count in name_ccounter.items():
    print(f"Vārds '{names}' atkārtojas {count} reizes.")
