from transformers import AutoTokenizer, AutoModelForCausalLM
from deep_translator import GoogleTranslator
from lingua import LanguageDetectorBuilder

# Inicializējam valodas detektoru
detector = LanguageDetectorBuilder.from_all_languages().with_preloaded_language_models().build()

# Norādam modeļa nosaukumu un ielādējam to
model_name = "Qwen/Qwen2.5-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def complete_text(input_text, max_length=50):
    # Nosakām teksta valodu
    detected_language = detector.detect_language_of(input_text).iso_code_639_1.name.lower()
    # Tulkojam ievades tekstu uz angļu valodu
    translation = GoogleTranslator(source=detected_language, target='en').translate(input_text)

    # Kodējam tekstu un ģenerējam turpinājumu
    input_ids = tokenizer.encode(translation, return_tensors="pt")
    output_ids = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id
    )

    # Dekodējam ģenerēto tekstu
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    # Tulkojam ģenerēto tekstu atpakaļ uz sākotnējo valodu
    translated_generated_text = GoogleTranslator(source='en', target=detected_language).translate(generated_text)

    return translated_generated_text

if __name__ == "__main__":
    text = "Reiz kādā tālā zemē..."
    completed_text = complete_text(text)
    print("Pabeigtais teksts:")
    print(completed_text)
