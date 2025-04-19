import os
import deepl

api_key = os.environ.get('API_TRADUCTOR')

def traducirTexto(texto, idioma):
    try:
        translator = deepl.Translator('acefa620-be20-4b89-b491-94ae016649ae:fx')
        result = translator.translate_text(texto, target_lang=idioma)
        print(result.text)
        return True, result.text
    except Exception as e:
        print(f"Ocurrio un error al traducir el texto: {e}")
        return False, f"Ocurrio un error al traducir el texto: {e}"

