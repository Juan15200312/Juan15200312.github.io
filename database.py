import os
import mysql.connector

db_password=os.environ.get('DB_PASSWORD')
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': db_password,
    'database': 'formulario_contacto',
    'port': 3306
}

def guardarDatos(datos):
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        sql = """
                Insert into mensajes (nombre, correo, mensaje)
                values (%s, %s, %s)
        """
        valores = (datos['nombre'], datos['correo'], datos['mensaje'])

        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        return "Datos guardados exitosamente"
    except mysql.connector.Error as e:
        return f"Ocurrio un error con la base de datos: {e}"

