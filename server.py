import os
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from climaGlobal import pedirDatosClima
from conversionMonedas import pedirDatosMoneda
from convertYT import convertir_a_mp3, convertir_a_mp4, borrarArchivo
from database import guardarDatos, verificarCuentaDB, añadirCuentaDB, resetPasswordCorreoDB, resetPasswordDB
from enviarCorreo import enviarCorreo
from dotenv import load_dotenv
from generadorQR import generarQR_imagen, borrarImages
from traductorDeepL import traducirTexto

load_dotenv()
app = Flask(__name__)
DOWNLOAD_FOLDER = os.path.abspath(".")
CORS(app)


@app.route('/index.html')
def home():
    return render_template('index.html')


@app.route('/login.html')
def login():
    return render_template('login.html')


@app.route('/new-cuenta.html')
def new_cuenta():
    return render_template('new-cuenta.html')


@app.route('/reset-password.html')
def reset_password():
    return render_template('reset-password.html')


@app.route('/reset-password-2.html')
def reset_password_2():
    return render_template('reset-password-2.html')


@app.route('/convertYT.html')
def convert_YT():
    return render_template('convertYT.html')


@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)


@app.route('/generadorQR.html')
def generador_QR():
    return render_template('generadorQR.html')


@app.route('/climaGlobal.html')
def clima_global():
    return render_template('climaGlobal.html')


@app.route('/conversionMoneda.html')
def conversion_moneda():
    return render_template('conversionMoneda.html')


@app.route('/traductor.html')
def traductor_deepL():
    return render_template('traductor.html')


@app.route('/enviar', methods=['POST'])
def recibirDatos():
    datos = request.get_json()
    print("Datos recibidos")
    print(f"Nombre: {datos['nombre']}")
    print(f"Correo electronico: {datos['correo']}")
    print(f"Mensaje: {datos['mensaje']}")
    mensaje = guardarDatos(datos)
    print(enviarCorreo(datos))
    return jsonify({"mensaje": mensaje}), 200


@app.route('/verificarCuenta', methods=['POST'])
def verificarCuenta():
    datosVerificarUser = request.get_json()
    print("Datos recibidos")
    print(f"Correo: {datosVerificarUser['email']}")
    print(f"Contraseña: {datosVerificarUser['password']}")

    salida, resultado0, resultado1, resultado2 = verificarCuentaDB(datosVerificarUser)
    print(f"resultado0: {resultado0}")
    print(f"resultado1: {resultado1}")
    print(f"resultado2: {resultado2}")

    if not salida:
        return jsonify({'mensaje': resultado0}), 200
    elif resultado1 == None and resultado2 == None:
        return jsonify({"mensaje": "Contraseña incorrecta o usuario no registrado. ", 'resultado': False}), 200
    else:
        return jsonify({"mensaje": f"Contraseña correcta. Bienvenido {resultado0}", 'resultado': True}), 200


@app.route('/crearCuenta', methods=['POST'])
def crearCuenta():
    datosCuentaNueva = request.get_json()
    print("Datos recibidos")
    print(f"Nombre: {datosCuentaNueva['nombre']}")
    print(f"Correo: {datosCuentaNueva['email']}")
    print(f"Contraseña: {datosCuentaNueva['password']}")

    comprobar, resultado = añadirCuentaDB(datosCuentaNueva)
    if comprobar:
        return jsonify({"mensaje": resultado, 'resultado': True}), 200
    else:
        return jsonify({"mensaje": resultado, 'resultado': False}), 200


@app.route('/resetPasswordCorreo', methods=['POST'])
def resetPasswordCorreo():
    datosResetPasswordCorreo = request.get_json()
    print("Datos recibidos")
    print(f"Correo: {datosResetPasswordCorreo['email']}")

    comprobar, resultado = resetPasswordCorreoDB(datosResetPasswordCorreo)
    if comprobar:
        return jsonify({"mensaje": resultado, 'resultado': True}), 200
    else:
        return jsonify({"mensaje": resultado, 'resultado': False}), 200


@app.route('/resetPassword', methods=['POST'])
def resetPassword():
    datosResetPassword = request.get_json()
    print("Datos recibidos")
    print(f"Correo: {datosResetPassword['email']}")
    print(f"Contraseña: {datosResetPassword['password']}")

    comprobar, resultado = resetPasswordDB(datosResetPassword)
    if comprobar:
        return jsonify({"mensaje": resultado, 'resultado': True}), 200
    else:
        return jsonify({"mensaje": resultado, 'resultado': False}), 200


@app.route('/convertYT', methods=['POST'])
def convertYT():
    borrarArchivo()
    datosUrl = request.get_json()
    print("Datos recibidos: ")
    print(f"URL: {datosUrl['urlYT']}")
    print(f"Formato: {datosUrl['format']}")

    if datosUrl['format'] == 'mp3':
        title, mensaje = convertir_a_mp3(datosUrl['urlYT'])
        if title:
            enlace_descarga = f"http://192.168.1.25:7550/download/{title}"
            return jsonify({"mensaje": mensaje, "descargar": enlace_descarga}), 200
        else:
            return jsonify({"mensaje": mensaje, "descargar": None}), 200

    elif datosUrl['format'] == 'mp4':
        title, mensaje = convertir_a_mp4(datosUrl['urlYT'])
        if title:
            enlace_descarga = f"http://192.168.1.25:7550/download/{title}"
            return jsonify({"mensaje": mensaje, "descargar": enlace_descarga}), 200
        else:
            return jsonify({"mensaje": mensaje, "descargar": None}), 200


@app.route('/generadorQR', methods=['POST'])
def generadorQR():
    borrarArchivo()
    borrarImages()
    datosGenerador = request.get_json()
    print("Datos recibidos")
    print(f"URL: {datosGenerador['urlQR']}")

    ruta_final, mensaje = generarQR_imagen(datosGenerador['urlQR'])

    if ruta_final:
        enlace_ver = f"http://192.168.1.25:7550/{ruta_final}"
        enlace_descarga = f"http://192.168.1.25:7550/download/{ruta_final}"
        return jsonify({"mensaje": mensaje, "urlImagen": enlace_ver, "urlDescarga": enlace_descarga}), 200
    else:
        return jsonify({"mensaje": mensaje, "urlImagen": None, "urlDescarga": None}), 200


@app.route('/climaGlobal', methods=['POST'])
def climaGlobal():
    borrarArchivo()
    datosCiudad = request.get_json()
    print("Datos recibidos")
    print(f"Ciudad: {datosCiudad['ciudad']}")

    resultado, datosClimaGlobal, mensaje = pedirDatosClima(datosCiudad['ciudad'])

    if resultado:
        return jsonify({"resultado": True, "mensaje": mensaje, "datosClimaGlobal": datosClimaGlobal}), 200
    else:
        return jsonify({"resultado": False, "mensaje": mensaje, "datosClimaGlobal": None}), 200


@app.route('/conversionMoneda', methods=['POST'])
def conversionMoneda():
    datosMonedasHtml = request.get_json()
    print("Datos recibidos")
    print(f"Moneda 1: {datosMonedasHtml['moneda1']}")
    print(f"Moneda 2: {datosMonedasHtml['moneda2']}")
    print(f"Importe: {datosMonedasHtml['importe']}")

    resultado1, datosMoneda1, mensaje1 = pedirDatosMoneda(datosMonedasHtml['moneda1'])
    resultado2, datosMoneda2, mensaje2 = pedirDatosMoneda(datosMonedasHtml['moneda2'])

    if resultado1 and resultado2:
        return jsonify({"resultado": True, "mensaje": mensaje1 + mensaje2, "datosMoneda1": datosMoneda1,
                        "datosMoneda2": datosMoneda2}), 200
    else:
        return jsonify(
            {"resultado": False, "mensaje": mensaje1 + mensaje2, "datosMonedaCambio": None, "datosMoneda2": None}), 200


@app.route('/traductor', methods=['POST'])
def traductor():
    datosTraductor = request.get_json()
    print("Datos recibidos")
    print(f"Texto a traducir: {datosTraductor['texto']}")
    print(f"Idioma: {datosTraductor['idioma']}")

    resultado, nuevo_texto = traducirTexto(datosTraductor['texto'], datosTraductor['idioma'])

    if resultado:
        return jsonify({"resultadoText": True, "mensaje": nuevo_texto}), 200
    else:
        return jsonify({"resultadoText": False, "mensaje": nuevo_texto}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7550, debug=True)
