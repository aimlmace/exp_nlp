from translate import Translator

def translate_text(text, source_language, target_language):

	translator = Translator(from_lang=source_language, to_lang=target_language)
	translation = translator.translate(text)
	return translation
    
if __name__ == "__main__":
    text_to_translate = input("Enter the text to translate: ")
    source_lang = input("Enter the source language code (e.g., en, es, fr): ")
    target_lang = input("Enter the target language code (e.g., en, es, fr): ")

    translated_text = translate_text(text_to_translate, source_lang, target_lang)

    if translated_text:
        print(f"Translated text: {translated_text}")
