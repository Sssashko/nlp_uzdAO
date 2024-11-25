from langdetect import detect

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day.",
    "Сегодня солнечный день."
]

for textss in texts:
    language = detect(textss)  # Nosaka teksta valodu
    print(f"Teksts: '{textss}' - Valoda: {language}")
