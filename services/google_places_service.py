import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_address_suggestions(input_text: str) -> list:
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    url = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
    params = {
        "input": input_text,
        "key": api_key,
        "types": "address",
        "components": "country:us"
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data["status"] != "OK":
        return []
    return [item["description"] for item in data["predictions"]]


def get_google_maps_distance(origin: str, destination: str) -> float:
    """
    Calcula la distancia en millas entre dos direcciones usando Google Maps Directions API.
    """
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise Exception("No se encontró la API Key de Google Maps.")

    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": origin,
        "destination": destination,
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] != "OK":
        raise Exception(f"Error en la respuesta de Google Maps: {data['status']}")

    # Obtiene la distancia en metros del primer tramo de la primera ruta
    distance_meters = data["routes"][0]["legs"][0]["distance"]["value"]
    distance_miles = distance_meters / 1609.344  # 1 milla = 1609.344 metros
    return distance_miles