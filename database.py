import os
import mysql.connector

from enviarCorreo import enviarCorreoResetPassword

db_password=os.environ.get('DB_PASSWORD')
port=os.environ.get('PORT')
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': db_password,
    'database': 'datosWeb',
    'port': port
}

def guardarDatos(datos):
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        sql = """
                Insert into mensajesFormulario (nombre, correo, mensaje)
                values (%s, %s, %s)
        """
        valores = (datos['nombre'], datos['correo'], datos['mensaje'])

        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Datos guardados exitosamente")
        return "Datos recibidos correctamente"
    except mysql.connector.Error as e:
        return f"Ocurrio un error con la base de datos: {e}"


def verificarCuentaDB(datos):
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        sql = """
                select nombre, correo, contraseña from datosCuentas 
                where correo = %s and contraseña = %s
                """
        values= (datos['email'], datos['password'])
        cursor.execute(sql, values)
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        if resultado:
            return True,resultado[0], resultado[1], resultado[2]
        else:
            return True, None, None, None
    except mysql.connector.Error as e:
        return False, f"Ocurrio un error con la base de datos: {e}",None,None

def verificarCuentaExistenteDB(datos):
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        sql = """
                select correo from datosCuentas 
                where correo = %s
                """
        values= (str(datos['email']),)
        cursor.execute(sql, values)
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        if resultado:
            return resultado[0]
        else:
            return None
    except mysql.connector.Error as e:
        return f"Ocurrio un error con la base de datos: {e}"

def añadirCuentaDB(datos):
    try:
        resultado0 = verificarCuentaExistenteDB(datos)
        if str(resultado0) == str(datos['email']):
            return False, f"Ya existe una cuenta con ese email, intente con otro. "

        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        sql = """
                insert into datosCuentas (nombre, correo, contraseña)
                values (%s, %s, %s)
            """
        values = (datos['nombre'], datos['email'], datos['password'])
        cursor.execute(sql, values)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True, f"Cuenta creada exitosamente, bienvenido {datos['nombre']}"

    except mysql.connector.Error as e:
        return False, f"Ocurrio un error con la base de datos: {e}"

def resetPasswordCorreoDB(datos):
    resultado0 = verificarCuentaExistenteDB(datos)
    if str(resultado0) != str(datos['email']):
        return False, f"No existe una cuenta con ese email"

    statusCorreo= enviarCorreoResetPassword(datos)
    if not statusCorreo:
        return False, 'Ocurrio un error al enviar el correo.'
    else:
        return True, statusCorreo

def resetPasswordDB(datos):
    try:
        resultado0 = verificarCuentaExistenteDB(datos)
        if str(resultado0) != str(datos['email']):
            return False, f"No existe una cuenta con ese email"

        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        sql = """
                update datosCuentas set contraseña = %s where correo = %s
            """
        values= (datos['password'], datos['email'])
        cursor.execute(sql, values)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True, f"Contrseña actualizada exitosamente"
    except mysql.connector.Error as e:
        return False, f"Ocurrio un error con la base de datos: {e}"
