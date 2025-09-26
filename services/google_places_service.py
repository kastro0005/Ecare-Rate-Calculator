from dotenv import load_dotenv
import os
import requests

load_dotenv()

def get_address_suggestions(input_text: str) -> list:
    try:
        api_key = os.getenv("GOOGLE_MAPS_API_KEY")
        if not api_key:
            print("No API KEY found")
            return []
        
        # URL de Google Places Autocomplete API
        url = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
        params = {
            "input": input_text,
            "key": api_key,
            "types": "address", # Solo direcciones
            "components": "country:us", # Restringir a EE.UU.
            "language": "en"  # Idioma de la respuesta
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if data.get("status") == "ZERO_RESULTS":
            print("No suggestions found  {input_text}")
            return []

        if data.get("status") != "OK":
            print(f"API Error: {data.get('status')}")
            return []
        
        suggestions = []
        for prediction in data.get("predictions", []):
            suggestions.append(prediction["description"])
        
        return suggestions[:5]  # Limitar a 5 sugerencias
    except Exception as e:
        print(f"Error getting suggestions: {e}")
        return []

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