import os
from os import listdir
import re
from unicodedata import normalize
from yt_dlp import YoutubeDL

def convertir_a_mp3(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  #
                'preferredquality': '192',
            }],
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        mp3_files = [f for f in os.listdir('.') if f.endswith('.mp3')]
        if not mp3_files:
            raise FileNotFoundError("No se encontró el archivo MP3")
        original_filename = mp3_files[0]

        print(f"Archivo descargado: {original_filename}")
        clean_title = renombrarArchivo(original_filename)
        print(f"Descarga completada: {clean_title}")
        return clean_title, f"Descarga completada: {clean_title}"
    except Exception as e:
        print("Ocurrió un error:", e)
        return None, f"Error al descargar: {url}"

def convertir_a_mp4(url):
    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': '%(title)s.%(ext)s',
        }
        print("Descargando el mejor video y audio en MP4...")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        mp4_files = [f for f in os.listdir('.') if f.endswith('.mp4')]
        if not mp4_files:
            raise FileNotFoundError("No se encontró el archivo MP4")
        original_filename = mp4_files[0]

        print(f"Archivo descargado: {original_filename}")
        clean_title = renombrarArchivo(original_filename)
        print(f"Descarga completada: {clean_title}")
        return clean_title, f"Conversion exitosa: {clean_title}"
    except Exception as e:
        print("Ocurrió un error:", e)
        return None, f"Error al descargar: {url}"

def borrarArchivo():
    lista=listdir('.')
    extenciones=['.mp3','.mp4','.webm','png', 'jpg']
    try:
        for archivo in lista:
            for extencion in extenciones:
                if extencion in archivo:
                    os.remove(archivo)
                    print(f"Archivo eliminado: {archivo}")
    except Exception as e:
        print(f"Error al eliminar el archivo: {e}")

def renombrarArchivo(nombre):
    target_name = normalize('NFKC', nombre)
    target_name = re.sub(r'[\\/*?#:"<>|｜]', "_", target_name)
    os.rename(nombre, target_name)
    return target_name

