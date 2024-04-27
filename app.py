import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os
import subprocess
import re


def download_video():
    url = entry_url.get()
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        output_path = audio_stream.download(output_path="downloads")
        output_file_path = os.path.join("downloads", f"{yt.title}.mp3")

        convert(output_path, output_file_path)

    except Exception as e:
        print(f"Download Failed: {e}")

def convert(input_file, output_file):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",  # No video.
        "-acodec", "libmp3lame",  # MP3 codec
        "-ab", "192k",  # Bit rate
        "-ar", "44100",  # Audio sampling rate
        "-y",  # Overwrite output file if it exists
        output_file
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Conversion successful.")
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed: {e}")

root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root.title("Youtube to MP3")

root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

url_label = ctk.CTkLabel(content_frame, text="Enter Youtube URL")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=("10p", "5p"))
entry_url.pack(pady=("10p", "5p"))

download_button = ctk.CTkButton(content_frame, text="Download", command=download_video())
download_button.pack(pady=("10p", "5p"))




root.mainloop()
