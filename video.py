import os
import moviepy.editor as mp
from tkinter import Tk, filedialog, Button, Label

def select_video():
    global video_path
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
    video_label.config(text=os.path.basename(video_path))

def select_audio():
    global audio_path
    audio_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav")])
    audio_label.config(text=os.path.basename(audio_path))

def replace_audio():
    if video_path and audio_path:
        video = mp.VideoFileClip(video_path)
        audio = mp.AudioFileClip(audio_path)
        video = video.set_audio(audio)
        output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("Video files", "*.mp4")])
        video.write_videofile(output_path, codec="libx264", audio_codec="aac", audio_fps=48000, audio_bitrate="320k", bitrate="7000k", fps=30)
        success_label.config(text=f"Video guardado como {os.path.basename(output_path)}")
    else:
        success_label.config(text="Por favor seleccione un video y un audio.")

root = Tk()
root.title("Reemplazar audio de video")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


root.geometry(f"{screen_width}x{screen_height}")

video_path = None
audio_path = None

video_button = Button(root, text="Seleccionar video", command=select_video, font=("Arial", 40))
video_button.pack()

video_label = Label(root, text="", font=("Arial", 20))
video_label.pack()

audio_button = Button(root, text="Seleccionar audio", command=select_audio, font=("Arial", 40))
audio_button.pack()

audio_label = Label(root, text="", font=("Arial", 20))
audio_label.pack()

replace_button = Button(root, text="Reemplazar audio", command=replace_audio, font=("Arial", 40))
replace_button.pack()

success_label = Label(root, text="", font=("Arial", 20))
success_label.pack()

diego_label = Label(root, text="DV TECHNOLOGY", font=("Arial", 16))
diego_label.pack()

root.mainloop()
