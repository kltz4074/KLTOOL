from pystyle import Write, Colors

def convert_jpg_to_png(png_path, jpg_path):
    # Открываем изображение PNG
    with Image.open(png_path) as img:
        # Конвертируем изображение в RGB (JPG не поддерживает альфа-канал)
        rgb_img = img.convert('RGB')
        # Сохраняем изображение в формате JPG
        rgb_img.save(jpg_path, 'JPEG')

def generatePassword(length=12, use_digits=True, use_uppercase=True):
    chars = string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_uppercase:
        chars += string.ascii_uppercase
    return ''.join(random.choice(chars) for _ in range(length))

def btdprint(text, interval = 0.0001, color = Colors.yellow_to_green):
    Write.Print(text, color, interval)
    print("")

def convert_mp4_to_mp3(mp4_path, mp3_path):
    video = moviepy.editor.VideoFileClip(mp4_path)
    audio = video.audio
    audio.write_audiofile(mp3_path)
    audio.close()
    video.close()

def Download_youtube_video(url, save_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl':  os.path.join(save_path, '%(title)s.%(ext)s'),  # Сохранение в указанной папке
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        
    if lng == "2":
        btdprint("Video downloaded successfully!")
        btdprint("video saved in: " + save_path)

def btdinput(text = ">>", colorin = Colors.yellow_to_green):
    Write.Input(str(text), colorin)