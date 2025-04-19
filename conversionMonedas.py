import requests

def pedirDatosMoneda(moneda):
    url = f'https://api.appnexus.com/currency?code={moneda}&show_rate=true'
    response = requests.get(url)

    if response.status_code == 200:
        moneda = response.json()

        datosMoneda = {
            "estado": moneda["response"]["status"],
            "codigo": moneda["response"]["currency"]["code"],
            "simbolo": moneda["response"]["currency"]["symbol"],
            "nombre": moneda["response"]["currency"]["name"],
            "posicion": moneda["response"]["currency"]["position"],
            "cambio_dolar": moneda["response"]["currency"]["rate_per_usd"],
            "ultimo_cambio": moneda["response"]["currency"]["as_of"]
        }
        return True, datosMoneda, f"Datos recibidos correctamente de {datosMoneda['nombre']}"
    else:
        return False, None, f"Error al obtener datos de la API: {response.status_code}"
