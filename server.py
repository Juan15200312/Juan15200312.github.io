from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from database import guardarDatos, verificarCuentaDB, añadirCuentaDB, resetPasswordCorreoDB, resetPasswordDB
from enviarCorreo import enviarCorreo
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
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

@app.route('/enviar', methods=['POST'])
def recibirDatos():

    datos = request.get_json()
    print("Datos recibidos")
    print(f"Nombre: {datos['nombre']}")
    print(f"Correo electronico: {datos['correo']}")
    print(f"Mensaje: {datos['mensaje']}")
    print(guardarDatos(datos))
    print(enviarCorreo(datos))
    return jsonify({"mensaje": "Datos recibidos correctamente"}),200

@app.route('/verificarCuenta', methods=['POST'])
def verificarCuenta():
    datosVerificarUser = request.get_json()
    print("Datos recibidos")
    print(f"Correo: {datosVerificarUser['email']}")
    print(f"Contraseña: {datosVerificarUser['password']}")

    resultado0,resultado1,resultado2=verificarCuentaDB(datosVerificarUser)
    print(f"resultado0: {resultado0}")
    print(f"resultado1: {resultado1}")
    print(f"resultado2: {resultado2}")

    if resultado1==None and resultado2==None:
        return jsonify({"mensaje": "Contraseña incorrecta o usuario no registrado. ", 'resultado': False}),200
    else:
        return jsonify({"mensaje": f"Contraseña correcta. Bienvenido {resultado0}", 'resultado': True}),200

@app.route('/crearCuenta', methods=['POST'])
def crearCuenta():
    datosCuentaNueva = request.get_json()
    print("Datos recibidos")
    print(f"Nombre: {datosCuentaNueva['nombre']}")
    print(f"Correo: {datosCuentaNueva['email']}")
    print(f"Contraseña: {datosCuentaNueva['password']}")

    comprobar,resultado = añadirCuentaDB(datosCuentaNueva)
    if comprobar:
        return jsonify({"mensaje": resultado, 'resultado': True}), 200
    else:
        return jsonify({"mensaje": resultado, 'resultado': False}), 200

@app.route('/resetPasswordCorreo', methods=['POST'])
def resetPasswordCorreo():
    datosResetPasswordCorreo = request.get_json()
    print("Datos recibidos")
    print(f"Correo: {datosResetPasswordCorreo['email']}")

    comprobar,resultado = resetPasswordCorreoDB(datosResetPasswordCorreo)
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7550, debug=True)