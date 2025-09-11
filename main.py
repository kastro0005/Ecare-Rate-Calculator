"""
Project: ECARE Rate Calculator 
Creator: Adrian C. Sierra, Ariel Chacon
Date: 2025-9-03

"""

__author__ = "Adrian C. Sierra, Ariel Chacon "
__version__ = "1.0.2"
__email__ = "sierraesperanza.creations@gmail.com"


import os
import sys
import flet as ft
import logging
import services
import importlib


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)


from services.location_service import LocationService
from services.rate_service import RateService


# Configuración de rutas para desarrollo y producción
def get_base_path():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # Ejecutando como executable
        return sys._MEIPASS
    else:
        # Ejecutando en desarrollo
        return os.path.dirname(os.path.abspath(__file__))

# Añadir el directorio base al path
base_path = get_base_path()
if base_path not in sys.path:
    sys.path.insert(0, base_path)

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Importar después de configurar el path
try:
    from services.location_service import LocationService
    from services.rate_service import RateService
    from ui.components import RateCalculatorUI
    from ui.dialogs import RatesDialog
    from utils.exceptions import LocationError, ValidationError, RateCalculationError
    
    logger.info("Módulos importados correctamente")
except ImportError as e:
    logger.error(f"Error importando módulos: {e}")
    logger.debug(f"Path actual: {sys.path}")
    raise

def load_config_module(config_name):
    # Ejemplo: config_name = "constants_clientA"
    module = importlib.import_module(f"config.{config_name}")
    return module

def main(page: ft.Page):
    page.title = "Ecare Rate Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_icon = "assets/icon.ico"
    

    def calculate_rate(e):
        """Maneja el cálculo de tarifa"""
        ui.set_progress(True)
        ui.update_status("Calculating...")
        page.update()

        try:
            # Validacion para si no haz seleccionado un nivel de servicio salga una alerta
            if not ui.service_level.value:
                raise ValidationError("Please, select a Level Of Service")

            # Obtener distancia según el modo
            if ui.is_manual_mode():
                distance = ui.get_distance()
                ui.hide_map()  # Oculta el enlace en modo manual
                if distance <= 0:
                    raise ValidationError("Please, select a valid distance:")
            else:
                # Validar direcciones
                if not ui.address1.value or not ui.address2.value:
                    raise ValidationError("Please, put both addresses correctly")
                # Calcular distancia
                distance, _ = LocationService.calculate_distance(ui.address1.value, ui.address2.value)
                ui.show_route_on_map(ui.address1.value, ui.address2.value)  # Muestra el enlace

            # Cálculo de tarifa
            result = RateService.calculate_rate(
                distance,
                ui.service_level.value,
                ui.after_hours.value,
                ui.deadheads.value,
                ui.o2.value,
                ui.liters_o2.value,
                ui.stairchair.value,
                ui.bariatric.value,
                ui.wait.value,
                float(ui.waiting_time.value or 0),
                ui.config_selector.value  
            )
            
            ui.update_result(result)
            ui.update_status("Cálculo completado exitosamente")
            
        except (ValidationError, LocationError, RateCalculationError) as e:
            logger.error(f"Error de validación: {e}")
            ui.update_status(str(e), True)
        except Exception as e:
            logger.error(f"Error inesperado: {e}", exc_info=True)
            ui.update_status(f"Unexpected Error: {str(e)}", True)
        
        finally:
            ui.set_progress(False)
            page.update()

    def close_rates_dialog(e):
        """Cierra el diálogo de tarifas"""
        page.dialog.open = False
        page.update()

    def save_rates(e):
        """Guarda las nuevas tarifas"""
        try:
            rates_inputs = getattr(page, "dialog_rates_inputs", {})
            provider = getattr(page, "dialog_provider", "Default")
            new_rates = {
                los: float(input_field.value)
                for los, input_field in rates_inputs.items()
            }
            RateService.update_rates(new_rates, provider)  # <-- Pasa el proveedor
            RateService.save_rates_to_file(provider)        # <-- Guarda el proveedor
            ui.update_status("Tarifas actualizadas correctamente")
            close_rates_dialog(e)
        except Exception as e:
            logger.error(f"Error al guardar tarifas: {e}", exc_info=True)
            ui.update_status(f"Error al guardar tarifas: {str(e)}", True)

    def open_rates_dialog(e):
        """Abre el diálogo de configuración de tarifas"""
        try:
            provider = ui.config_selector.value or "Default"
            dialog, rates_inputs = RatesDialog.create_dialog(save_rates, close_rates_dialog, provider)
            page.dialog = dialog
            page.dialog_rates_inputs = rates_inputs
            page.dialog_provider = provider  # Guardar proveedor actual

            # Agrega el diálogo al overlay si no está
            if dialog not in page.overlay:
                page.overlay.append(dialog)
            dialog.open = True
            page.update()
        except Exception as e:
            logger.error(f"Error al abrir diálogo de tarifas: {e}", exc_info=True)
            ui.update_status(f"Error al abrir configuración: {str(e)}", True)

    # Inicialización de la UI
    try:
        ui = RateCalculatorUI(calculate_rate, open_rates_dialog)
        
        # Callback para cambiar el modo y actualizar la UI
        def on_mode_change(e):
            ui.on_mode_change(e)
            page.update()
        
        # Asigna el nuevo callback al cambio de pestaña
        ui.distance_mode.on_change = on_mode_change

        page.add(ui.get_layout())
    except Exception as e:
        logger.error(f"Error al inicializar UI: {e}", exc_info=True)
        page.add(ft.Text(f"Error al iniciar la aplicación: {str(e)}", color="red"))

if __name__ == "__main__":
    try:
        ft.app(target=main, view=ft.WEB_BROWSER)
    except Exception as e:
        logger.error(f"Error al iniciar la aplicación: {e}", exc_info=True)
        # Mostrar una ventana de error si falla el inicio
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", f"Error al iniciar la aplicación: {str(e)}")