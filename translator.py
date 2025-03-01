from googletrans import Translator

def translate_text():
    translator = Translator()
    text_to_translate = input("Enter the sentences: ")
    target_language_code = input("Enter the language code: ")

    try:
        translated_text = translator.translate(text_to_translate, dest=target_language_code)
        print(f"Translated text in {target_language_code}: {translated_text.text}")
    except Exception as e:
        print(f"Translation failed: {e}")

#English - en,Tamil - ta,Hindi - hi,French - fr,Telugu - te,Punjabi - pa,Spanish - es,Arabic - ar,
#Korean - ko,Marathi - mr,Bengali - bn,Portuguese - pt,Turkish - tr,Chinese(Simplified) - zh-CN,
#Urdu - ur,Russian - ru,Japanese - ja,German - de,Danish - da,Norwegian - no,Vietnamese - vi,