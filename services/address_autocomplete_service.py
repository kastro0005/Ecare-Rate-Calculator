import requests
from typing import List


from utils.geolocate import get_location_by_ip

class AddressAutocompleteService:
    @staticmethod
    def get_suggestions(query: str, limit: int = 5) -> List[str]:
        """
        Busca sugerencias de direcciones usando Nominatim, priorizando la zona del usuario por IP
        """
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": query,
            "format": "json",
            "addressdetails": 1,
            "limit": limit,
        }
        # Intentar obtener la ubicación del usuario por IP
        loc = get_location_by_ip()
        if loc:
            lat, lon = loc
            # Definir un viewbox de ~20km alrededor del usuario
            delta = 0.1  # ~11km
            params["viewbox"] = f"{lon-delta},{lat-delta},{lon+delta},{lat+delta}"
            params["bounded"] = 1
        headers = {"User-Agent": "ecare-rate-calculator/1.0"}
        try:
            response = requests.get(url, params=params, headers=headers, timeout=5)
            response.raise_for_status()
            data = response.json()
            return [item["display_name"] for item in data]
        except Exception:
            return []
