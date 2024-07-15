from googletrans import Translator, LANGUAGES

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def print_supported_languages():
    print("Supported languages:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code}: {lang_name}")

if __name__ == "__main__":
    print("Welcome to the Python Language Translation Tool!")
    print_supported_languages()
    
    text_to_translate = input("Enter the text you want to translate: ")
    target_language = input("Enter the language code of the target language (e.g., 'es' for Spanish): ")
    
    try:
        translated_text = translate_text(text_to_translate, target_language)
        print(f"\nOriginal Text: {text_to_translate}")
        print(f"Translated Text ({LANGUAGES[target_language]}): {translated_text}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
