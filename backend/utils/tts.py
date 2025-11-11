from gtts import gTTS
import os
import uuid

def generate_tts(text: str, output_folder: str, lang: str = "en"):
    """
    Génère un fichier audio à partir du texte traduit.
    """
    filename = f"tts_{uuid.uuid4().hex}.mp3"
    output_path = os.path.join(output_folder, filename)
    print(f"[TTS] Génération de la voix en {lang}...")

    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(output_path)
        print(f"[TTS] Fichier audio généré : {output_path}")
        return output_path
    except Exception as e:
        print(f"[TTS] Erreur : {e}")
        return None
