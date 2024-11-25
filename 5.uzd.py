import re

# Neapstrādātais teksts
raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

# Noņem liekos simbolus
clean_text = re.sub(r'(@|#)\w+', '', raw_text)  # Noņem lietotājvārdus un heštagus
clean_text = re.sub(r'http\S+', '', clean_text)  # Noņem URL

clean_text = clean_text.encode('ascii', 'ignore').decode('ascii')  # Noņem emocijzīmes un ne-ASCII simbolus

clean_text = re.sub(r'[^\w\s]', '', clean_text)  # Noņem pieturzīmes un speciālos simbolus

clean_text = clean_text.lower()  # Pārveido uz mazajiem burtiem

clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # Noņem liekās atstarpes

# Izdrukā tīro tekstu
print("Tīrais teksts:")
print(clean_text)
