import os
import requests

api_key = os.environ.get('API_CLIMA')

def pedirDatosClima(ciudad):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    response = requests.get(url)

    if response.status_code == 200:
        clima = response.json()
        nombre = clima["name"]
        pais = clima["sys"]["country"]
        icono = clima["weather"][0]["icon"]
        descripcion = clima["weather"][0]["description"]
        temperatura = clima["main"]["temp"]
        temperatura_min = clima["main"]["temp_min"]
        temperatura_max = clima["main"]["temp_max"]

        sensacion_termica = clima["main"]["feels_like"]
        viento = clima["wind"]["speed"]
        humedad = clima["main"]["humidity"]
        presion = clima["main"]["pressure"]
        visibilidad = clima["visibility"]
        amanecer = clima["sys"]["sunrise"]
        atardecer = clima["sys"]["sunset"]
        zona_horaria = clima["timezone"]

        datosClimaGlobal = {
            "nombre": nombre,
            "pais": pais,
            "icono": icono,
            "descripcion": descripcion,
            "temperatura": temperatura,
            "temperatura_min": temperatura_min,
            "temperatura_max": temperatura_max,
            "sensacion_termica": sensacion_termica,
            "viento": viento,
            "humedad": humedad,
            "presion": presion,
            "visibilidad": visibilidad,
            "amanecer": amanecer,
            "atardecer": atardecer,
            "zona_horaria": zona_horaria,

        }
        print(f"Datos recibidos correctamente de {nombre}")
        return True, datosClimaGlobal, f"Datos recibidos correctamente de {nombre}"

    else:
        print(f"Error al obtener datos de la API. Código de estado: {response.status_code}")
        return False, None, f"Error al obtener datos de la API: {response.status_code}"

