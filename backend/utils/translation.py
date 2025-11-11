from googletrans import Translator

def translate_text(text: str, target_lang: str = "en"):
    """
    Traduit le texte vers la langue cible.
    Exemples : 'fr', 'en', 'de', 'ar'...
    """
    translator = Translator()
    print(f"[Traduction] Traduction vers : {target_lang}")

    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        print(f"[Traduction] Erreur : {e}")
        return text  # on renvoie le texte original en cas d’échec
