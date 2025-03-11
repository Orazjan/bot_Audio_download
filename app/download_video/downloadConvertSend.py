from yt_dlp import YoutubeDL
import os
from pathlib import Path


PATH = os.path.abspath('./downloaded/')
file_name = ''


def download(video_url):
    downloaded_dir = PATH
    # downloaded_dir.mkdir(exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',  # Скачивать лучшее аудио
        'outtmpl': os.path.join(downloaded_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{  # Постобработка для преобразования в MP3
            'key': 'FFmpegExtractAudio',  # Использовать FFmpeg для извлечения аудио
            'preferredcodec': 'mp3',  # Выбрать формат MP3
            'preferredquality': '192',  # Качество аудио (192 kbps)
        }],
        'extract_audio': True,  # Извлечь аудио
    }

# Скачивание и преобразование в MP3
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            global full_path
            full_path = ydl.prepare_filename(info_dict).replace(
                '.webm', '.mp3')
            global file_name
            file_name = os.path.basename(full_path)
        message = file_name
    except Exception as e:
        message = "Произошла ошибка: {e}"
    return message
