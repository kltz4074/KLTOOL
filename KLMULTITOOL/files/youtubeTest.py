import yt_dlp

# Введите URL видео
url = input("Введите URL видео: ")

# Настройки для скачивания
ydl_opts = {
    'format': 'best',  # Скачивает лучшее доступное качество
    'outtmpl': '%(title)s.%(ext)s',  # Указывает имя файла (по названию видео)
}

# Скачиваем видео
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Видео скачано!")