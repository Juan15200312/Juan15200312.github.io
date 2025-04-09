from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from database import guardarDatos
from enviarCorreo import enviarCorreo
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7550, debug=True)