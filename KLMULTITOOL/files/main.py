import os
from pystyle import Write, Colors
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import SbannerRU
import SbannerENG
import webbrowser
import random
import string
import time
import moviepy
import yt_dlp
rdn = random.randint(5000000, 10000000000000000)
current_directory = os.path.dirname(os.path.abspath(__file__))

folder_path = os.path.join(current_directory, 'images')
os.makedirs(folder_path, exist_ok=True)
with open(os.path.join(folder_path, 'none.txt'), 'w', encoding='utf-8') as file:
    file.write(str(rdn))

# FUNCTIONS -----------------------------------------------------------------------------------------------------------------------

def exxut():
    if lng == "2":
        time.sleep(1)
        print(" ")
        print(" ")
        btdprint("continue? 1 - yes 2 - no", 0.025)
        print(" ")
        btdprint("1 - yes")
        print(" ")
        btdprint("2 - no")
        print(" ")
        choose = Write.Input(">>", Colors.yellow_to_green, interval=0.025)
        if choose == "1":
            os.system("python files/main.py")
        
        if choose == "2":
            btdprint("closing...")
            print(" ")
            exit()
        
        
    if lng == "1":
        time.sleep(1)
        print(" ")
        print(" ")
        btdprint("продолжить?")
        print(" ")
        btdprint("1 - да")
        print(" ")
        btdprint("2 - нет")
        print(" ")
        choose1 = Write.Input(">>", Colors.yellow_to_green, interval=0.025)
        if choose1 == "2":
            btdprint("закрываюсь...")
            print(" ")
            exit()
            
        if choose1 == "1":
            os.system("python files/main.py")

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

def btdprint(text, interval = 0.025):
    Write.Print(text, Colors.yellow_to_green, interval)

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
    if lng == "1":
        btdprint("видео успешно скачано!")
        btdprint("видео сохранено в: " + save_path)
# FUNCTIONS -----------------------------------------------------------------------------------------------------------------------

btdprint("Выберите язык / Choose language", 0.025)
print(" ")
btdprint("1 - RU")
print(" ")
btdprint("2 - ENG")
print(" ")
lng = Write.Input(">>", Colors.yellow_to_green, interval=0.025)
#-----------------------------------------------ENGLISH--------------------------------------------------------
if lng == "2":
    btdprint(SbannerENG.Banner, 0.00025)
    btdprint(SbannerENG.textq, 0.025)
    inputi = Write.Input(SbannerENG.textu, Colors.yellow_to_green, interval=0.025)

    if int(inputi) == rdn:
        Write.Input(SbannerENG.scrbn, Colors.red, interval=0.00025)
        btdprint(SbannerENG.scrbn, 0.00025)
        
    if inputi == "1":
        Write.Print(SbannerENG.telegram, Colors.yellow_to_green, interval=0.025)
        inputg = Write.Input(">>", Colors.yellow_to_green, interval=0.25)

        if inputg == "1":
            btdprint(SbannerENG.tgks, 0.025)
            inputgk = Write.Input(">>", Colors.yellow_to_green, interval=0.25)

            if inputgk == "1":
                webbrowser.open('https://t.me/kltzyoutube_pon')

    
    if inputi == "2":
        smalgnrt = int(Write.Input("number from - ", Colors.yellow_to_green, interval=0.025))
        biggnrt = int(Write.Input("to - ", Colors.yellow_to_green, interval=0.025))
        btdprint(str(random.randint(smalgnrt, biggnrt)), 0.025)
        print(" ")
    
    if inputi == "3":
        Write.Print("Password length", Colors.yellow_to_green, interval=0.025)
        length = int(Write.Input(">>", Colors.yellow_to_green, interval=0.025))
        Write.Print("Use digits? 1 - yes, 2 - no", Colors.yellow_to_green, interval=0.025)
        use_digits = Write.Input(">>", Colors.yellow_to_green, interval=0.025) == "1"
        Write.Print("Use uppercase? 1 - yes, 2 - no", Colors.yellow_to_green, interval=0.025)
        use_uppercase = Write.Input(">>", Colors.yellow_to_green, interval=0.025) == "1"
        Write.Print(generatePassword(int(length), use_digits, use_uppercase), Colors.yellow_to_green, interval=0.025)
        
    if inputi == "4":
        btdprint(SbannerENG.whatdecompilate, 0.025)
        inputpg = Write.Input(">>", Colors.yellow_to_green, interval=0.25)
        if inputpg == "1":
            root = tk.Tk()
            file_path = filedialog.askopenfilename(title="Choose PNG file")
            btdprint("path - " + file_path)
            convert_jpg_to_png(file_path, file_path.rsplit(".", 1)[0] + ".png")
            print(" ")
            print(" ")
            btdprint("File saved as: " + file_path.rsplit(".", 1)[0] + ".png", 0.025)
            
        if inputi == "5":
            btdprint(SbannerENG.youtube)
            print(" ")
            ythose = Write.Input(">>", Colors.yellow_to_green, interval=0.025)
            if ythose == "1":
                btdprint("write video link")
                print(" ")
                url = Write.Input(">>", Colors.yellow_to_green, interval=0.025)
                btdprint("choose where to save the video")
                print(" ")
                root = tk.Tk()
                save_path = filedialog.askdirectory(title="select path to save")
                Download_youtube_video(url, save_path)
                print(" ")
                btdprint(": " + save_path)
    exxut()
#-----------------------------------------------RUSSIAN--------------------------------------------------------
if lng == "1":
    btdprint(SbannerRU.Banner, 0.00025)
    btdprint(SbannerRU.textq, 0.025)
    inputi = Write.Input(SbannerRU.textu, Colors.yellow_to_green, interval=0.025)

    if int(inputi) == rdn:
        Write.Input(SbannerRU.scrbn, Colors.red, interval=0.00025)
        btdprint(SbannerRU.scrbn, 0.00025)
        
    if inputi == "1":
        Write.Print(SbannerRU.telegram, Colors.yellow_to_green, interval=0.025)
        inputg = Write.Input(">>", Colors.yellow_to_green, interval=0.25)

        if inputg == "1":
            btdprint(SbannerRU.tgks, 0.025)
            inputgk = Write.Input(">>", Colors.yellow_to_green, interval=0.25)

            if inputgk == "1":
                webbrowser.open('https://t.me/kltzyoutube_pon')
                
    if inputi == "2":
        smalgnrt = int(Write.Input("число от - ", Colors.yellow_to_green, interval=0.025))
        biggnrt = int(Write.Input("до - ", Colors.yellow_to_green, interval=0.025))
        btdprint(str(random.randint(smalgnrt, biggnrt)), 0.025)
        print(" ")
    
    if inputi == "3":
        Write.Print("длина пароля", Colors.yellow_to_green, interval=0.025)
        length = int(Write.Input(">>", Colors.yellow_to_green, interval=0.025))
        Write.Print("использовать цифры? 1 - да, 2 - нет", Colors.yellow_to_green, interval=0.025)
        use_digits = Write.Input(">>", Colors.yellow_to_green, interval=0.025) == "1"
        Write.Print("Использовать заглавные буквы.? 1 - да, 2 - нет", Colors.yellow_to_green, interval=0.025)
        use_uppercase = Write.Input(">>", Colors.yellow_to_green, interval=0.025) == "1"
        Write.Print(generatePassword(int(length), use_digits, use_uppercase), Colors.yellow_to_green, interval=0.025)
        
    if inputi == "4":
        btdprint(SbannerRU.whatdecompilate, 0.025)
        inputpg = Write.Input(">>", Colors.yellow_to_green, interval=0.25)
        if inputpg == "1":
            root = tk.Tk()
            file_path = filedialog.askopenfilename(title="выберите файл PNG")
            btdprint("путь - " + file_path)
            convert_jpg_to_png(file_path, file_path.rsplit(".", 1)[0] + ".png")
            btdprint("File saved as: " + file_path.rsplit(".", 1)[0] + ".png", 0.025)
        
        if inputpg == "2":
            root = tk.Tk()
            mp4_path = filedialog.askopenfilename(title="выберите файл MP4")
            mp3_path = mp4_path.rsplit(".", 1)[0] + ".mp3"
            convert_mp4_to_mp3(mp4_path, mp3_path)
            print(" ")
            print(f"файл сохранён в: {mp3_path}")
        
    if inputi == "5":
        btdprint(SbannerRU.youtube)
        print(" ")
        ythose = Write.Input(">>", Colors.yellow_to_green, interval=0.025)
        if ythose == "1":
            btdprint("введите сыллку на видео")
            print(" ")
            url = Write.Input(">>", Colors.yellow_to_green, interval=0.025)
            btdprint("where to save the video")
            print(" ")
            root = tk.Tk()
            save_path = filedialog.askdirectory(title="выберите путь для сохранения")
            Download_youtube_video(url, save_path)
            
    exxut()

# END -----------------------------------------------------------------------------------------------------------------------