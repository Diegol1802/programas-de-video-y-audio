import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp

def extract_audio_and_convert():
    filepath = filedialog.askopenfilename(title="Seleccione un archivo de video",
                                           filetypes=(("Archivos de video", "*.mp4;*.avi;*.mkv"),
                                                      ("Todos los archivos", "*.*")))
    if not filepath:
        return

    destination = filedialog.asksaveasfilename(title="Guardar archivo de audio",
                                                defaultextension=".wav",
                                                filetypes=(("Archivos WAV", "*.wav"),
                                                           ("Todos los archivos", "*.*")))
    if not destination:
        return

    try:
        video_clip = mp.VideoFileClip(filepath)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(destination, codec='pcm_s24le', fps=48000)
        audio_clip.close()
        video_clip.close()
        tk.messagebox.showinfo("Éxito", "Extracción y conversión completadas correctamente.")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Se produjo un error: {str(e)}")

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Extractor de audio de video")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")

# Botón para iniciar el proceso de extracción y conversión
button = tk.Button(root, text="Seleccionar video y convertir audio", command=extract_audio_and_convert,font=("Arial", 40))
button.pack(pady=20)

diego_label = Label(root, text="DV TECHNOLOGY", font=("Arial", 16))
diego_label.pack()

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
