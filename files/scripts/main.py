import os
import random
import string
import time
import webbrowser
import tkinter as tk
from tkinter import filedialog
from pystyle import Write, Colors
from PIL import Image
from moviepy import VideoFileClip
import yt_dlp
import functions
import SbannerENG

def exxut():
    # Placeholder for exit or loop logic, you can implement as needed
    pass

def main():
    # Set language
    lng = "1"

    if lng == "1":
        functions.btdprint(SbannerENG.Banner, 0.00025)
        functions.btdprint(SbannerENG.menu, 0.025)
        inputi = Write.Input(SbannerENG.textu, Colors.yellow_to_green, interval=0.025)

        if inputi == "1":
            Write.Print(SbannerENG.telegram, Colors.yellow_to_green, interval=0.025)
            inputg = Write.Input(">>", Colors.yellow_to_green, interval=0.25)
            if inputg == "1":
                functions.btdprint(SbannerENG.tgks, 0.025)
                inputgk = Write.Input(">>", Colors.yellow_to_green, interval=0.25)
                if inputgk == "1":
                    webbrowser.open('https://t.me/kltzyoutube_pon')

        elif inputi == "2":
            try:
                smalgnrt = int(Write.Input("number from - ", Colors.yellow_to_green, interval=0.025))
                biggnrt = int(Write.Input("to - ", Colors.yellow_to_green, interval=0.025))
                if smalgnrt > biggnrt:
                    functions.btdprint("Error: Start number must be less than end number.", 0.025)
                else:
                    functions.btdprint(str(random.randint(smalgnrt, biggnrt)), 0.025)
                    print(" ")
            except ValueError:
                functions.btdprint("Invalid input. Please enter valid numbers.", 0.025)

        elif inputi == "3":
            try:
                Write.Print("Password length", Colors.yellow_to_green, interval=0.025)
                length = int(Write.Input(">>", Colors.yellow_to_green, interval=0.025))
                Write.Print("Use digits? 1 - yes, 2 - no", Colors.yellow_to_green, interval=0.025)
                use_digits = Write.Input(">>", Colors.yellow_to_green, interval=0.025) == "1"
                Write.Print("Use uppercase? 1 - yes, 2 - no", Colors.yellow_to_green, interval=0.025)
                use_uppercase = Write.Input(">>", Colors.yellow_to_green, interval=0.025) == "1"
                password = functions.generatePassword(length, use_digits, use_uppercase)
                Write.Print(password, Colors.yellow_to_green, interval=0.025)
            except ValueError:
                functions.btdprint("Invalid input for password length.", 0.025)

        elif inputi == "4":
            functions.btdprint(SbannerENG.whatdecompilate, 0.025)
            inputpg = Write.Input(">>", Colors.yellow_to_green, interval=0.25)
            if inputpg == "1":
                root = tk.Tk()
                root.withdraw()  # Hide the main window
                file_path = filedialog.askopenfilename(title="Choose JPG file", filetypes=[("JPG files", "*.jpg"), ("All files", "*.*")])
                if file_path:
                    functions.btdprint("Selected file path: " + file_path)
                    png_path = file_path.rsplit(".", 1)[0] + ".png"
                    try:
                        functions.convert_jpg_to_png(file_path, png_path)
                        functions.btdprint("File saved as: " + png_path, 0.025)
                    except Exception as e:
                        functions.btdprint(f"Error converting file: {e}", 0.025)
                else:
                    functions.btdprint("No file selected.", 0.025)

        elif inputi == "5":
            functions.btdprint(SbannerENG.youtube, 0.025)
            ythose = Write.Input(">>", Colors.yellow_to_green, interval=0.025)
            if ythose == "1":
                functions.btdprint("Write video link:", 0.025)
                url = Write.Input(">>", Colors.yellow_to_green, interval=0.025)
                functions.btdprint("Choose where to save the video", 0.025)
                root = tk.Tk()
                root.withdraw()
                save_path = filedialog.askdirectory(title="Select path to save")
                if save_path:
                    try:
                        functions.Download_youtube_video(url, save_path)
                        functions.btdprint("Video saved in: " + save_path)
                    except Exception as e:
                        functions.btdprint(f"Error downloading video: {e}", 0.025)
                else:
                    functions.btdprint("No path selected.", 0.025)
            elif ythose == "2":
                functions.btdprint("Write video link:", 0.025)
                url = Write.Input(">>", Colors.yellow_to_green, interval=0.025)
                functions.btdprint("Choose where to save the audio", 0.025)
                root = tk.Tk()
                root.withdraw()
                save_path = filedialog.askdirectory(title="Select path to save")
                if save_path:
                    try:
                        # Download video first, then convert to mp3
                        functions.Download_youtube_video(url, save_path)
                        # Find the downloaded video file
                        # Assumes yt_dlp saves with .mp4 extension
                        for fname in os.listdir(save_path):
                            if fname.endswith(".mp4"):
                                mp4_path = os.path.join(save_path, fname)
                                mp3_path = mp4_path.rsplit(".", 1)[0] + ".mp3"
                                functions.convert_mp4_to_mp3(mp4_path, mp3_path)
                                functions.btdprint("Audio saved as: " + mp3_path)
                                break
                        else:
                            functions.btdprint("MP4 file not found for conversion.", 0.025)
                    except Exception as e:
                        functions.btdprint(f"Error downloading or converting video: {e}", 0.025)
                else:
                    functions.btdprint("No path selected.", 0.025)

        else:
            functions.btdprint("Invalid menu selection.", 0.025)

        exxut()

if __name__ == '__main__':
    main()