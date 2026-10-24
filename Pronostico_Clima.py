
"""Módulo encargo de realizar las peticiones a la API del clima y procesar los datos."""

import requests
from typing import Dict, Any, Optional


def obtener_datos_clima(ciudad: str, api_key: str) -> Optional[Dict[str, Any]]:
    """Obtiene la información meteorológica actual de una ciudad mediante OpenWeatherMap.

    Args:
        ciudad (str): Nombre de la ciudad a consultar.
        api_key (str): Clave de acceso a la API de OpenWeatherMap.

    Returns:
        Optional[Dict[str, Any]]: Diccionario con los datos del clima si la consulta
        fue exitosa, o None si ocurrió un error de red o la ciudad no existe.
    """
    url: str = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    try:
        response: requests.Response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.RequestException:
        return None