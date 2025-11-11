from moviepy.editor import VideoFileClip, AudioFileClip
import os
import uuid

def merge_audio_with_video(video_path: str, audio_path: str, output_folder: str):
    """
    Fusionne l'audio généré (TTS) avec la vidéo originale.
    Retourne le chemin du fichier final.
    """
    output_filename = f"final_{uuid.uuid4().hex}.mp4"
    output_path = os.path.join(output_folder, output_filename)

    print("[Fusion] Chargement de la vidéo et de l’audio...")

    try:
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)

        # Ajuste la durée audio si elle dépasse la vidéo
        if audio.duration > video.duration:
            audio = audio.subclip(0, video.duration)

        final = video.set_audio(audio)
        final.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"[Fusion] Vidéo finale sauvegardée : {output_path}")
        return output_path
    except Exception as e:
        print(f"[Fusion] Erreur : {e}")
        return None
