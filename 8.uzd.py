from flair.data import Sentence
from flair.models import SequenceTagger

# Ielādējam iepriekš apmācīto NER modeli
ner_tagger = SequenceTagger.load('ner-multi')  # Multivalodu modelis, tostarp latviešu

def extract_named_entities(text):
    sentence = Sentence(text)  # Izveidojam teikumu
    ner_tagger.predict(sentence)  # Prognozē entītijas

    entities = {
        "PERSON": [],
        "ORG": []
    }

    for entity in sentence.get_spans('ner'):
        if entity.tag == "PER":
            entities["PERSON"].append(entity.text)
        elif entity.tag == "ORG":
            entities["ORG"].append(entity.text)

    return entities

# Ievades teksts
text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

# Izgūstam nosauktās entītijas
named_entities = extract_named_entities(text)

# Izdrukājam rezultātus
print("Nosauktās entītijas:")
for entity_type, names in named_entities.items():
    print(f"{entity_type}: {', '.join(names)}")
