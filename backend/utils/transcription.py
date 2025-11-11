import whisperx

def transcribe_audio(filepath):
    print("[Transcription] Chargement du modèle WhisperX sur CPU (float32)...")
    device = "cpu"
    
    # 👉 Forcer l'utilisation de float32 pour les CPU
    model = whisperx.load_model("small", device=device, compute_type="float32")

    result = model.transcribe(filepath)
    text = result["segments"][0]["text"] if result.get("segments") else ""
    
    print("[Transcription terminée ✅]")
    return text
