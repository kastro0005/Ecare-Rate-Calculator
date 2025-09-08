import requests
from typing import Optional, Tuple

def get_location_by_ip() -> Optional[Tuple[float, float]]:
    """
    Obtiene la latitud y longitud aproximada del usuario usando su IP pública.
    """
    try:
        response = requests.get("https://ipinfo.io/json", timeout=5)
        response.raise_for_status()
        data = response.json()
        if "loc" in data:
            lat, lon = map(float, data["loc"].split(","))
            return lat, lon
    except Exception:
        pass
    return None
