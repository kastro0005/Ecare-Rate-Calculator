from typing import Dict, Union
from config.constants import LEVEL_OF_SERVICE_BASE_RATES, LEVEL_OF_SERVICE_INCREMENTS
from utils.exceptions import RateCalculationError

class RateService:
    @staticmethod
    def calculate_rate(
        distance: float,
        service_level: str,
        after_hours: bool = False,
        deadheads: bool = False,
        o2: bool = False,
        liters_o2: int = 0,
        stc: bool = False,
        bariatric: bool = False
    ) -> Dict[str, Union[float, str]]:
        """
        Calcula la tarifa basada en la distancia y los parámetros seleccionados
        """
        try:
            base_rate = LEVEL_OF_SERVICE_BASE_RATES.get(service_level)
            if base_rate is None:
                raise RateCalculationError(f"Nivel de servicio no válido: {service_level}")

            # Cálculo de tarifa base
            increment = LEVEL_OF_SERVICE_INCREMENTS.get(service_level, 0)
            rate = base_rate + (increment * distance)

            # Aplicar modificadores
            if after_hours:
                rate += 150
            if deadheads:
                rate *= 2
            if o2:
                rate += (liters_o2 * 30) #  $30 por unidad de O2
            if stc:
                rate += 400 # tarifa extra para silla de escaleras
            if bariatric:
                rate += 300 # tarifa extra para bariátrico
            
            



            return {
                "distance": round(distance, 2),
                "base_rate": round(base_rate, 2),
                "total_rate": round(rate, 2)
            }

        except Exception as e:
            raise RateCalculationError(f"Error en el cálculo de la tarifa: {str(e)}")

    @staticmethod
    def update_rates(new_rates: Dict[str, float]) -> None:
        """
        Actualiza las tarifas base y los incrementos
        """
        try:
            for los, rate in new_rates.items():
                if rate <= 0:
                    raise ValueError(f"La tarifa para {los} debe ser mayor que 0")
                LEVEL_OF_SERVICE_BASE_RATES[los] = rate
                LEVEL_OF_SERVICE_INCREMENTS[los] = rate
        except Exception as e:
            raise RateCalculationError(f"Error al actualizar tarifas: {str(e)}")