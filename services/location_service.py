from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time
import logging
from typing import Tuple

from config.constants import MAX_RETRIES, RETRY_DELAY, ROAD_DISTANCE_FACTOR
from utils.exceptions import LocationError

logger = logging.getLogger(__name__)

class LocationService:
    @staticmethod
    def get_coordinates_with_retry(address: str) -> Tuple[float, float]:
        """
        Obtiene las coordenadas de una dirección con reintentos
        """
        errors = []
        for attempt in range(MAX_RETRIES):
            try:
                geolocator = Nominatim(user_agent=f"distance_calculator_{attempt}")
                location = geolocator.geocode(address)
                
                if location is None:
                    raise LocationError(f"No se encontró la ubicación para: {address}")
                    
                return location.latitude, location.longitude
                
            except Exception as e:
                errors.append(f"Intento {attempt + 1}: {str(e)}")
                if attempt < MAX_RETRIES - 1:
                    time.sleep(RETRY_DELAY)
                continue
                
        raise LocationError(f"No se pudo obtener las coordenadas después de {MAX_RETRIES} intentos. "
                           f"Errores: {'; '.join(errors)}")

    @staticmethod
    def calculate_distance(origin: str, destination: str) -> Tuple[float, str]:
        """
        Calcula la distancia entre dos direcciones
        """
        try:
            origin_coords = LocationService.get_coordinates_with_retry(origin)
            dest_coords = LocationService.get_coordinates_with_retry(destination)
            
            distance = geodesic(origin_coords, dest_coords).miles
            adjusted_distance = distance * ROAD_DISTANCE_FACTOR
            
            return adjusted_distance, "road_estimate"
            
        except Exception as e:
            logger.error(f"Error en el cálculo de distancia: {str(e)}")
            raise