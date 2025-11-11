from flask import Flask, request, jsonify, send_file
import os
from utils.transcription import transcribe_audio
from utils.translation import translate_text
from utils.tts import generate_tts   # ✅ un seul import cohérent
from utils.sync import merge_audio_with_video

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return "✅ Voice Sync Backend is running!"

@app.route("/process", methods=["POST"])
def process_video():
    file = request.files.get("file")
    target_lang = request.form.get("lang", "en")

    if not file:
        return jsonify({"error": "Aucun fichier reçu"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # 🧠 Étapes du pipeline
    transcription = transcribe_audio(filepath)
    translated = translate_text(transcription, target_lang)
    tts_path = generate_tts(translated, OUTPUT_FOLDER)
    final_video = merge_audio_with_video(filepath, tts_path, OUTPUT_FOLDER)

    return send_file(final_video, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
