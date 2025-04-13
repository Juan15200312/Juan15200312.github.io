import os
from os import listdir

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
        print("Descargando solo el audio...")
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'audio').strip()
        print(f"Descarga completada: {title}.mp3")
        print("¡El proceso ha finalizado!")
        return f"{title}.mp3", f"Descarga completada: {title}.mp3"
    except Exception as e:
        print("Ocurrió un error:", e)
        return None, f"Ocurrio un error al intentar descargar: {url}"

def convertir_a_mp4(url):
    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': '%(title)s.%(ext)s',
        }
        print("Descargando el mejor video y audio en MP4...")
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'video').strip()
        print(f"Descarga completada: {title}.mp4")
        print("¡El proceso ha finalizado!")
        return f"{title}.mp4", f"Descarga completada: {title}.mp4"
    except Exception as e:
        print("Ocurrió un error:", e)
        return None, f"Ocurrio un error al intentar descargar: {url}"

def borrarArchivo():
    lista=listdir('.')
    extenciones=['.mp3','.mp4','.webm']
    try:
        for archivo in lista:
            for extencion in extenciones:
                if extencion in archivo:
                    os.remove(archivo)
                    print(f"Archivo eliminado: {archivo}")
    except Exception as e:
        print(f"Error al eliminar el archivo: {e}")

