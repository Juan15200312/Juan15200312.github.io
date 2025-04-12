import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def enviarCorreo(datos):
    try:
        mensaje = Mail(
            from_email='juanjoseortizolivares@gmail.com',
            to_emails=['juanjoseortizolivares@gmail.com'],
            subject=f"Nuevo mensaje de : {datos['nombre']}",
            html_content=f"<h4>Nombre: {datos['nombre']}</h4>"
                         f"<h4>Correo: {datos['correo']}</h4>"
                         f"<h4>Mensaje: {datos['mensaje']}</h4>"
        )
        api_key = os.environ.get('SENDGRID_API_KEY')
        sg = SendGridAPIClient(api_key)
        response = sg.send(mensaje)
        return f"Correo enviado exitosamente: {response.status_code}"
    except Exception as e:
        print(f"Ocurrio un error al enviar el correo: {e}")


def enviarCorreoResetPassword(datos):
    try:
        mensaje = Mail(
            from_email='juanjoseortizolivares@gmail.com',
            to_emails=[datos['email']],
            subject=f"CAMBIAR CONTRASEÑA",
            html_content=f"<h4>Ingrese al siguiente enlace para restablecer su contraseña:</h4>"
                         f"<h4>Link: http://192.168.1.25:7550/reset-password-2.html</h4>"
        )
        api_key = os.environ.get('SENDGRID_API_KEY')
        sg = SendGridAPIClient(api_key)
        response = sg.send(mensaje)
        print(response.status_code)
        return f"Correo enviado exitosamente"
    except Exception as e:
        print(f"Ocurrio un error al enviar el correo: {e}")
        return False