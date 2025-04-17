import glob
import os
import time
import qrcode
from PIL import Image

def generarQR_imagen(url):
    try:
        qr = qrcode.QRCode(version=4 , error_correction=qrcode.constants.ERROR_CORRECT_L ,box_size=10, border=2)
        qr.add_data(url)
        qr.make(fit=True)
        fill_color=(0,0,0)
        back_color=(255,255,255)
        img_logo = 'static/images/logoQR.png'
        qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)
        logo = Image.open(img_logo)
        posicion = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
        timestamp = str(int(time.time()))
        ruta_final = f'static/images/images-qr/imagenQRgenerada_{timestamp}.png'
        qr_img.paste(logo, posicion)
        qr_img.save(ruta_final)
        return ruta_final, f'Imagen generada con exito. '
    except Exception as error:
        print("Ops, ocurrio un error: ", error)
        return None, f'Ocurrio un error al generar la imagen. '

def borrarImages():
    files = glob.glob('static/images/images-qr/imagenQRgenerada_*.png')
    for f in files:
        try:
            os.remove(f)
        except Exception as e:
            print(f"Error borrando {f}: {e}")