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