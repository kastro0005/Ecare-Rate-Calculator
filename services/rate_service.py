from typing import Dict, Union
from config.constants import *
from utils.exceptions import RateCalculationError
import os

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
        bariatric: bool = False,
        wait: bool = False,
        waiting_time: int = 0,
        provider: str = "Standard"
    ) -> Dict[str, Union[float, str]]:
        """
        Calcula la tarifa basada en la distancia y los parámetros seleccionados
        """
        try:
            # Vamos a intentar iterar por los diferentes proveedores
            #Provider va a guardar el nombre del proveedor seleccionado el el menu desplegable
            #Logica de seleccion del proveedor
            if provider == "Baptist":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_BAPTIST.get(service_level) 
                provider = provider
            elif provider == "HCA":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_JUPITER_MEDICAL_CENTER.get(service_level) 
            elif provider == "Tenants (PBHN)":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_TENANTS.get(service_level)
            elif provider == "Arbor Trail Rehab and Skilled Nursing Center":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_ARBOR_TRAIL_REHAB_AND_SKILLED_NURSING_CENTER.get(service_level)
            elif provider == "Jupiter Medical Center":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_JUPITER_MEDICAL_CENTER.get(service_level)
            elif provider == "Cedar Creek":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_CEDAR_CREEK.get(service_level)
            elif provider == "Citrus Health and Rehab Center":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_CITRUS_HEALTH_AND_REHAB_CENTER.get(service_level)
            elif provider == "Clearsky Rehab Hospital of Lecanto":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_CLEARSKY_REHAB_HOSPITAL_OF_LECANTO.get(service_level)
            elif provider == "Crystal River Health and Rehab Center":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_CRYSTAL_RIVER_HEALTH_AND_REHAB_CENTER.get(service_level)
            elif provider == "Diamond Ridge Health and Rehab Center":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_DIAMOND_RIDGE_HEALTH_AND_REHAB_CENTER.get(service_level)
            elif provider == "Sunflower Springs":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_SUNFLOWER_SPRINGS.get(service_level)
            elif provider == "Superior Residences of Lecanto":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_SUPERIOR_RESIDENCES_OF_LECANTO.get(service_level)
            elif provider == "Tampa General Hospital Crystal River":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_TAMPA_GENERAL_HOSPITAL_CRYSTAL_RIVER.get(service_level)
            elif provider == "TGH Crystal River Emergency Center":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_TGH_CRYSTAL_RIVER_EMERGENCY_CENTER.get(service_level)
            elif provider == "The Gardens Assisted Living and Memory Care":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_THE_GARDENS_ASSISTED_LIVING_AND_MEMORY_CARE.get(service_level)
            elif provider == "Vitas Inpatient Hospice":
                base_rate = LEVEL_OF_SERVICE_BASE_RATES_VITAS_INPATIENT_HOSPICE.get(service_level)
            else:
                base_rate = LEVEL_OF_SERVICE_BASE_RATES.get(service_level)



            #Caso de que no se halla elegido proveedor
            if base_rate is None:
                raise RateCalculationError(f"Nivel de servicio no válido: {service_level}")

            # Cálculo de tarifa de incremento por milla
            #Aki voy a intentar hacer que el incremento por milla sea diferente segun el proveedor
            if provider == "Baptist":
                increment = LEVEL_OF_SERVICE_INCREMENTS_BAPTIST.get(service_level, 0)
            elif provider == "Jupiter Medical Center":
                increment = LEVEL_OF_SERVICE_INCREMENTS_JUPITER_MEDICAL_CENTER.get(service_level, 0)
            elif provider == "Tenants (PBHN)":
                increment = LEVEL_OF_SERVICE_INCREMENTS_TENANTS.get(service_level, 0)
            elif provider == "Arbor Trail Rehab and Skilled Nursing Center":
                increment = LEVEL_OF_SERVICE_INCREMENTS_ARBOR_TRAIL_REHAB_AND_SKILLED_NURSING_CENTER.get(service_level, 0)
            elif provider == "HCA":
                increment = LEVEL_OF_SERVICE_INCREMENTS_JUPITER_MEDICAL_CENTER.get(service_level, 0)
            elif provider == "Cedar Creek":
                increment = LEVEL_OF_SERVICE_INCREMENTS_CEDAR_CREEK.get(service_level, 0)
            elif provider == "Citrus Health and Rehab Center":
                increment = LEVEL_OF_SERVICE_INCREMENTS_CITRUS_HEALTH_AND_REHAB_CENTER.get(service_level, 0)
            elif provider == "Clearsky Rehab Hospital of Lecanto":
                increment = LEVEL_OF_SERVICE_INCREMENTS_CLEARSKY_REHAB_HOSPITAL_OF_LECANTO.get(service_level, 0)
            elif provider == "Crystal River Health and Rehab Center":
                increment = LEVEL_OF_SERVICE_INCREMENTS_CRYSTAL_RIVER_HEALTH_AND_REHAB_CENTER.get(service_level, 0)
            elif provider == "Diamond Ridge Health and Rehab Center":
                increment = LEVEL_OF_SERVICE_INCREMENTS_CRYSTAL_RIVER_HEALTH_AND_REHAB_CENTER.get(service_level, 0)
            elif provider == "Sunflower Springs":
                increment = LEVEL_OF_SERVICE_INCREMENTS_SUNFLOWER_SPRINGS.get(service_level, 0)
            elif provider == "Superior Residences of Lecanto":
                increment = LEVEL_OF_SERVICE_INCREMENTS_SUPERIOR_RESIDENCES_OF_LECANTO.get(service_level, 0)
            elif provider == "Tampa General Hospital Crystal River":
                increment = LEVEL_OF_SERVICE_INCREMENTS_TAMPA_GENERAL_HOSPITAL_CRYSTAL_RIVER.get(service_level, 0)
            elif provider == "TGH Crystal River Emergency Center":
                increment = LEVEL_OF_SERVICE_INCREMENTS_TGH_CRYSTAL_RIVER_EMERGENCY_CENTER.get(service_level, 0)
            elif provider == "The Gardens Assisted Living and Memory Care":
                increment = LEVEL_OF_SERVICE_INCREMENTS_THE_GARDENS_ASSISTED_LIVING_AND_MEMORY_CARE.get(service_level, 0)
            elif provider == "Vitas Inpatient Hospice":
                increment = LEVEL_OF_SERVICE_INCREMENTS_VITAS_INPATIENT_HOSPICE.get(service_level, 0)
            else:
                increment = LEVEL_OF_SERVICE_INCREMENTS.get(service_level, 0)
            rate = base_rate + (increment * distance)

            # Aplicar modificadores
            if after_hours:
                rate += EXTRAS.get("AfterHours") # tarifa extra por viaje después de horas          
            if o2:
                rate += (liters_o2 * EXTRAS.get("O2")) #  rate por unidad de O2
            if stc:
                rate += EXTRAS.get("STC") # tarifa extra para silla de escaleras
            if bariatric:
                rate += EXTRAS.get("Bariatric") # tarifa extra para bariátrico
            if wait:
                medias_horas = int(waiting_time * 2)  # Ej: 1.5 horas = 3 medias horas
                rate += medias_horas * WAITING_TIME_RATE.get(service_level, 0) # tarifa extra por tiempo de espera
            if deadheads:
                rate *= 2
            



            return {
                "distance": round(distance, 2),
                "base_rate": round(base_rate, 2),
                "total_rate": round(rate, 2)
            }

        except Exception as e:
            raise RateCalculationError(f"Error en el cálculo de la tarifa: {str(e)}")

    @staticmethod
    def update_rates(new_rates: Dict[str, float], provider: str = "Default") -> None:
        """
        Actualiza las tarifas base según el proveedor
        """
        try:
            if provider == "Baptist":
                LEVEL_OF_SERVICE_BASE_RATES_BAPTIST.update(new_rates)
            elif provider == "Jupiter Medical Center":
                LEVEL_OF_SERVICE_BASE_RATES_JUPITER_MEDICAL_CENTER.update(new_rates)
            elif provider == "Tenants (PBHN)":
                LEVEL_OF_SERVICE_BASE_RATES_TENANTS.update(new_rates)
            elif provider == "Arbor Trail Rehab and Skilled Nursing Center":
                LEVEL_OF_SERVICE_BASE_RATES_ARBOR_TRAIL_REHAB_AND_SKILLED_NURSING_CENTER.update(new_rates)
            elif provider == "Cedar Creek":
                LEVEL_OF_SERVICE_BASE_RATES_CEDAR_CREEK.update(new_rates)
            elif provider == "Citrus Health and Rehab Center":
                LEVEL_OF_SERVICE_BASE_RATES_CITRUS_HEALTH_AND_REHAB_CENTER.update(new_rates)
            elif provider == "Clearsky Rehab Hospital of Lecanto":
                LEVEL_OF_SERVICE_BASE_RATES_CLEARSKY_REHAB_HOSPITAL_OF_LECANTO.update(new_rates)
            elif provider == "Crystal River Health and Rehab Center":
                LEVEL_OF_SERVICE_BASE_RATES_CRYSTAL_RIVER_HEALTH_AND_REHAB_CENTER.update(new_rates)
            elif provider == "Diamond Ridge Health and Rehab Center":
                LEVEL_OF_SERVICE_BASE_RATES_DIAMOND_RIDGE_HEALTH_AND_REHAB_CENTER.update(new_rates)
            elif provider == "Sunflower Springs":
                LEVEL_OF_SERVICE_BASE_RATES_SUNFLOWER_SPRINGS.update(new_rates)
            elif provider == "Superior Residences of Lecanto":
                LEVEL_OF_SERVICE_BASE_RATES_SUPERIOR_RESIDENCES_OF_LECANTO.update(new_rates)
            elif provider == "Tampa General Hospital Crystal River":
                LEVEL_OF_SERVICE_BASE_RATES_TAMPA_GENERAL_HOSPITAL_CRYSTAL_RIVER.update(new_rates)
            elif provider == "TGH Crystal River Emergency Center":
                LEVEL_OF_SERVICE_BASE_RATES_TGH_CRYSTAL_RIVER_EMERGENCY_CENTER.update(new_rates)
            elif provider == "The Gardens Assisted Living and Memory Care":
                LEVEL_OF_SERVICE_BASE_RATES_THE_GARDENS_ASSISTED_LIVING_AND_MEMORY_CARE.update(new_rates)
            elif provider == "Vitas Inpatient Hospice":
                LEVEL_OF_SERVICE_BASE_RATES_VITAS_INPATIENT_HOSPICE.update(new_rates)
            else:
                LEVEL_OF_SERVICE_BASE_RATES.update(new_rates)
        except Exception as e:
            raise RateCalculationError(f"Error al actualizar tarifas: {str(e)}")

    @staticmethod
    def save_rates_to_file(provider: str = "Default", filepath: str = None):
        """
        Guarda los rates actuales en el archivo constants.py según el proveedor
        """
        try:
            if not filepath:
                filepath = os.path.join(os.path.dirname(__file__), "../config/constants.py")
                filepath = os.path.abspath(filepath)

            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()

            def dict_to_str(name, d):
                items = ",\n    ".join([f'"{k}": {v}' for k, v in d.items()])
                return f'{name} = {{\n    {items}\n}}\n'

            import re
            def replace_dict(name, d, text):
                pattern = rf'{name}\s*=\s*\{{.*?\}}'
                return re.sub(pattern, dict_to_str(name, d), text, flags=re.DOTALL)

            text = "".join(lines)
            # Solo actualiza el diccionario del proveedor seleccionado
            if provider == "Baptist":
                text = replace_dict("LEVEL_OF_SERVICE_BASE_RATES_BAPTIST", LEVEL_OF_SERVICE_BASE_RATES_BAPTIST, text)
            else:
                text = replace_dict("LEVEL_OF_SERVICE_BASE_RATES", LEVEL_OF_SERVICE_BASE_RATES, text)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(text)

        except Exception as e:
            raise RateCalculationError(f"Error al guardar tarifas en archivo: {str(e)}")