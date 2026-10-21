import requests

def obtener_datos():
    respuesta = requests.get(
    #"https://mindicador.cl/api/dolar",
    "https://open.er-api.com/v6/latest/USD",
        timeout=(3, 5),
    )
    print("Estado HTTP:", respuesta.status_code)
    respuesta.raise_for_status()
    return respuesta.json()

import math
import math
import requests

def obtener_datos():
    """Realiza la petición HTTP para obtener los datos del indicador."""
    respuesta = requests.get(
        "https://mindicador.cl/api/dolar",  # URL de mindicador
        timeout=(3, 5),
    )
    print("Estado HTTP:", respuesta.status_code)
    respuesta.raise_for_status()
    return respuesta.json()

def extraer_primero(datos):
    """
    Comprueba que la serie tenga datos, valida que el valor sea numérico,
    finito y positivo, y muestra la fecha del registro utilizado.
    """
    # 1. Comprobar que la respuesta sea un diccionario
    if not isinstance(datos, dict):
        raise ValueError("Respuesta inesperada: se esperaba un diccionario.")

    # 2. Obtener la lista de registros del indicador ("serie")
    serie = datos.get("serie")
    
    # Comprobar que la serie sea una lista y contenga datos
    if not isinstance(serie, list) or not serie:
        raise ValueError("No hay valores disponibles en la serie.")

    # 3. Seleccionar el primer registro y validar su estructura
    registro = serie[0]
    if not isinstance(registro, dict):
        raise ValueError("El formato del registro es inválido.")

    # Verificar que el registro contenga las claves requeridas
    if "valor" not in registro or "fecha" not in registro:
        raise ValueError("El registro no contiene las claves 'valor' o 'fecha'.")

    valor = registro["valor"]
    fecha = registro["fecha"]

    # 4. Validar que el valor sea numérico (excluyendo booleanos), finito y positivo
    if not isinstance(valor, (int, float)) or isinstance(valor, bool):
        raise ValueError("El valor del indicador debe ser de tipo numérico.")
    
    if not math.isfinite(valor) or valor <= 0:
        raise ValueError("El valor del indicador debe ser un número finito y mayor que cero.")

    # 5. Mostrar la fecha del registro utilizado junto con el valor
    print(f"Registro utilizado - Fecha: {fecha} | Valor: {valor}")

    # Devolver la fecha y el valor como una tupla
    return fecha, valor


# Ejemplo de uso:
if __name__ == "__main__":
    try:
        datos_api = obtener_datos()
        fecha_utilizada, valor_utilizado = extraer_primero(datos_api)
    except Exception as e:
        print(f"Ocurrió un error: {e}")

try:
    # Consultar la API y obtener los datos.
    datos = obtener_datos()
    
    # Extraer y validar la fecha y el valor del primer registro.
    fecha, valor = extraer_primero(datos)
    
    # Mostrar el valor con dos decimales y su unidad.
    print(f"Dólar observado: {valor:.2f} CLP por USD")
    
    # Mostrar la fecha a la que corresponde el dato.
    print(f"Fecha del registro: {fecha}")
except requests.exceptions.RequestException:
    # Controlar fallos de conexión, espera, HTTP o decodificación JSON.
    print("No pudimos consultar el servicio. Reintente.")

except (ValueError, KeyError, TypeError):
    # Controlar valores inválidos, claves ausentes o tipos incorrectos.
    print("La respuesta no contiene un indicador válido.")

