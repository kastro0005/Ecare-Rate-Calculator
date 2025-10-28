import flet as ft
from typing import Callable
from config.constants import *

from services.google_places_service import get_google_maps_distance

class RateCalculatorUI:
    def __init__(self, page, calculate_callback: Callable, open_rates_dialog_callback: Callable):
        self.page = page
        self.calculate_callback = calculate_callback
        self.open_rates_dialog_callback = open_rates_dialog_callback

        # Listas de sugerencias
        self.suggestions1 = ft.ListView(visible=False, spacing=2, height=150, width=300)
        self.suggestions2 = ft.ListView(visible=False, spacing=2, height=150, width=300)

        # Campos de texto con eventos de autocompletado
        self.address1 = ft.TextField(
            label="First Address",
            hint_text="Enter the first address",
            width=300,
            on_change=self.on_address1_change,
            on_blur=self.on_address1_blur
        )
        
        self.address2 = ft.TextField(
            label="Second Address",
            hint_text="Enter the second address",
            width=300,
            on_change=self.on_address2_change,
            on_blur=self.on_address2_blur
        )
        self.distance_mode = ft.Tabs(
            selected_index=0,
            on_change=self.on_mode_change,
            tabs=[
                ft.Tab(text="Calculate from addresses"),
                ft.Tab(text="Enter distance manually")
            ]
        )
        self.manual_miles = ft.TextField(
            label="Miles",
            hint_text="Enter the Miles",
            width=300,
            visible=False,
            keyboard_type=ft.KeyboardType.NUMBER
        )
        self.service_level = ft.Dropdown(
            label="Level of Service",
            hint_text="Choose Level of Service",
            options=[ft.dropdown.Option(los) for los in LEVEL_OF_SERVICE_BASE_RATES.keys()],
            width=200
        )
        self.o2 = ft.TextField("", width=100, keyboard_type=ft.KeyboardType.NUMBER, disabled=True, on_change=self.validate_decimal)
        self.liters_o2 = ft.Checkbox(label="Liters of Oxygen", on_change=self.on_liters_o2_change )
        self.after_hours = ft.Checkbox(label="Afterhours (6pm-6am)")
        self.deadheads = ft.Checkbox(label="Round Trip")
        self.roundtrip = ft.Checkbox(label="Roundtrip)")     
        self.bariatric = ft.Checkbox(label="Bariatric")
        self.stairchair = ft.Checkbox(label="Stairchair")
        self.waiting_time = ft.TextField("", width=100, keyboard_type=ft.KeyboardType.NUMBER, disabled=True,on_change=self.validate_decimal)
        self.wait = ft.Checkbox(label="Waiting Time (Hours)", on_change=self.on_waiting_change)
        self.county_selector = ft.Dropdown(
            label="County",
            options=[ft.dropdown.Option(c) for c in COUNTY_PROVIDERS.keys()],
            value="Palm Beach",
            width=200,
            on_change=self.on_county_change
        )
        self.config_selector = ft.Dropdown(
            label="Source",
            options=[ft.dropdown.Option(p) for p in COUNTY_PROVIDERS["Palm Beach"]],
            value=COUNTY_PROVIDERS["Palm Beach"][0],
            width=200,
        )
        self.progress = ft.ProgressBar(visible=False)
        self.status_text = ft.Text("")
        self.result = ft.Text(size=20, weight=ft.FontWeight.BOLD)

        self.calculate_button = ft.ElevatedButton(
            text="Calculate Rate",
            on_click=self.calculate_callback,
            icon="calculate"
        )
        self.rates_button = ft.ElevatedButton(
            text="Configurate Rates",
            on_click=self.open_rates_dialog_callback,
            icon="settings",
            disabled=True
        )

        self.clear_button = ft.ElevatedButton(
            text="Clear",
            on_click=self.clear_all_fields,
            icon="clear",
            color="red"
        )

        self.map_link = ft.TextButton(
            text="Show route on Google Maps",
            visible=False,
            url="",
            style=ft.ButtonStyle(color="blue")
        )
        self.address_container = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Column([
                        self.address1,
                        self.suggestions1,  # Lista de sugerencias para address1
                    ])
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.Column([
                        self.address2,
                        self.suggestions2,  # Lista de sugerencias para address2
                    ])
                ], alignment=ft.MainAxisAlignment.CENTER),
            ])
        )

        self.manual_container = ft.Container(
            content=ft.Column([
                ft.Row([self.manual_miles], alignment=ft.MainAxisAlignment.CENTER),
            ]),
            visible=False
        )

    def on_mode_change(self, e):
        is_manual = self.distance_mode.selected_index == 1
        self.address_container.visible = not is_manual
        self.manual_container.visible = is_manual
        self.address1.visible = not is_manual
        self.address2.visible = not is_manual
        self.manual_miles.visible = is_manual
        self.update_status("")
        self.result.value = ""

    def show_route_on_map(self, origin: str, destination: str):
        origin_url = origin.replace(" ", "+")
        destination_url = destination.replace(" ", "+")
        url = f"https://www.google.com/maps/dir/{origin_url}/{destination_url}/"
        self.map_link.url = url
        self.map_link.visible = True
        self.map_link.update()

    def hide_map(self):
        self.map_link.visible = False
        self.map_link.update()

    #mETODO DE PRIEBA
    def show_result_dialog(self, result_data: dict):
        dialog = ft.AlertDialog( modal=True,
                title=ft.Text("Calculation Results"),
                content=ft.Column([
                    ft.Text(f"Distance: {result_data['distance']} miles"),
                    ft.Text(f"Rate Base: ${result_data['base_rate']}"),
                    ft.Text(f"Total Rate: ${result_data['total_rate']}")
                ], tight=True, spacing=5),
                actions=[
                    ft.TextButton("Close", on_click=lambda e: self.close_dialog())
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    #End Prueba

    def get_layout(self) -> ft.Column:
        return ft.Column(
            [
                ft.Row([self.distance_mode], alignment=ft.MainAxisAlignment.CENTER),  # Tabs arriba
                self.address_container,  # Direcciones pegadas justo debajo de los tabs
                self.manual_container,
                ft.Row([self.county_selector], alignment=ft.MainAxisAlignment.END),
                ft.Row([self.config_selector], alignment=ft.MainAxisAlignment.END),
                ft.Row([self.service_level], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.after_hours, self.deadheads], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.liters_o2, self.o2], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.bariatric, self.stairchair], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.wait, self.waiting_time], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.calculate_button, self.rates_button, self.clear_button], alignment=ft.MainAxisAlignment.CENTER),
                #self.progress,
                #self.status_text,
                self.result,
                self.map_link,
                ft.Row([
                    ft.TextButton(
                        text="Developed by Sierra-Esperanza Creations ©",
                        url="https://www.sierraesperanzac.com",
                        style=ft.ButtonStyle(color="white")
                    )
                ], alignment=ft.MainAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8
        )

    def is_manual_mode(self) -> bool:
        return self.distance_mode.selected_index == 1

    def get_distance(self) -> float:
        try:
            return float(self.manual_miles.value or 0)
        except ValueError:
            raise ValueError("PLEASE ENTER A VALID NUMBER FOR MILES")

    def update_status(self, message: str, is_error: bool = False) -> None:
        self.status_text.value = message
        self.status_text.color = "red" if is_error else "black"

    def set_progress(self, visible: bool) -> None:
        self.progress.visible = visible

    def update_result(self, result_data: dict) -> None:
        self.result.value = (
             f"Rate Base: ${result_data['base_rate']}\n"
            f"Distance: {result_data['distance']} miles\n"
            f"Total Rate: ${result_data['total_rate']}"
        )
        self.show_result_dialog(result_data)

    def on_liters_o2_change(self, e):
        self.o2.disabled = not self.liters_o2.value
        self.o2.update()

    def on_waiting_change(self, e):
        self.waiting_time.disabled = not self.wait.value
        self.waiting_time.update()

    def validate_decimal(self, e):
        import re
        value = e.control.value
        match = re.match(r"^\d+(\.\d{0,1})?$", value)
        if not match and value != "":
            parts = value.split(".")
            if len(parts) == 2:
                value = parts[0] + "." + parts[1][:1]
            else:
                value = ''.join(filter(str.isdigit, value))
            e.control.value = value
            e.control.update()

    def on_county_change(self, e):
        county = self.county_selector.value
        providers = COUNTY_PROVIDERS.get(county, ["Standard"])
        self.config_selector.options = [ft.dropdown.Option(p) for p in providers]
        self.config_selector.value = providers[0]
        self.config_selector.update()

    def calculate_rate(self):
        try:
            if not self.address1.value or not self.address2.value:
                self.update_status("Please enter both addresses", is_error=True)
                return
            distance = get_google_maps_distance(self.address1.value, self.address2.value)
            base_rate = LEVEL_OF_SERVICE_BASE_RATES[self.service_level.value]
            total_rate = base_rate * distance
            self.update_result({
                "distance": distance,
                "base_rate": base_rate,
                "total_rate": total_rate
            })
            
        except Exception as e:
            self.update_status(f"Error Calculating Rate: {str(e)}", is_error=True)
    
    def close_dialog(self):
        self.page.dialog.open = False
        self.page.update()

    def on_address1_change(self, e):
        query = self.address1.value.strip()
        self.suggestions1.controls.clear()
        
        if query and len(query) >= 3:
            from services.google_places_service import get_address_suggestions
            suggestions = get_address_suggestions(query)
            
            if suggestions:
                for suggestion in suggestions:
                    self.suggestions1.controls.append(
                        ft.ListTile(
                            title=ft.Text(suggestion),
                            data=suggestion,
                            on_click=self.on_address1_suggestion_click
                        )
                    )
                self.suggestions1.visible = True
            else:
                self.suggestions1.visible = False
        else:
            self.suggestions1.visible = False
        
        self.page.update()

    def on_address1_suggestion_click(self, e):
        selected_address = e.control.data
        print(f"Dirección seleccionada: {selected_address}")  # Debug
        
        # Actualiza el campo
        self.address1.value = selected_address
        
        # Oculta las sugerencias
        self.suggestions1.visible = False
        self.suggestions1.controls.clear()
        
        # Actualiza explícitamente el campo y la página
        self.address1.update()
        self.suggestions1.update()
        self.page.update()

    def on_address1_blur(self, e):
        # Sin hilos, solo ocultar después de un delay
        pass  # O simplemente no hagas nada aquí

    def on_address2_change(self, e):
        query = self.address2.value.strip()
        self.suggestions2.controls.clear()
        
        if query and len(query) >= 3:
            from services.google_places_service import get_address_suggestions
            suggestions = get_address_suggestions(query)
            
            if suggestions:
                for suggestion in suggestions:
                    self.suggestions2.controls.append(
                        ft.ListTile(
                            title=ft.Text(suggestion),
                            data=suggestion,
                            on_click=self.on_address2_suggestion_click
                        )
                    )
                self.suggestions2.visible = True
            else:
                self.suggestions2.visible = False
        else:
            self.suggestions2.visible = False
        
        self.page.update()

    def on_address2_suggestion_click(self, e):
        selected_address = e.control.data
        print(f"Dirección seleccionada: {selected_address}")  # Debug
        
        # Actualiza el campo
        self.address2.value = selected_address
        
        # Oculta las sugerencias
        self.suggestions2.visible = False
        self.suggestions2.controls.clear()
        
        # Actualiza explícitamente el campo y la página
        self.address2.update()
        self.suggestions2.update()
        self.page.update()

    def on_address2_blur(self, e):
        # Sin hilos, solo ocultar después de un delay  
        pass  # O simplemente no hagas nada aquí

    def clear_all_fields(self, e):
        """Reinicia todos los campos del programa"""
        # Limpiar campos de dirección
        self.address1.value = ""
        self.address2.value = ""
        
        # Limpiar campo manual
        self.manual_miles.value = ""
        
        # Resetear dropdown de nivel de servicio
        self.service_level.value = None
        
        # Limpiar campos numéricos
        self.o2.value = ""
        self.waiting_time.value = ""
        
        # Resetear checkboxes
        self.liters_o2.value = False
        self.after_hours.value = False
        self.deadheads.value = False
        self.roundtrip.value = False
        self.bariatric.value = False
        self.stairchair.value = False
        self.wait.value = False
        
        # Deshabilitar campos dependientes
        self.o2.disabled = True
        self.waiting_time.disabled = True
        
        # Resetear selectors de condado y proveedor
        self.county_selector.value = "Palm Beach"
        self.config_selector.value = COUNTY_PROVIDERS["Palm Beach"][0]
        
        # Resetear modo de distancia a "Calculate from addresses"
        self.distance_mode.selected_index = 0
        self.on_mode_change(None)  # Aplicar cambio de modo
        
        # Limpiar resultados y estado
        self.result.value = ""
        self.status_text.value = ""
        
        # Ocultar mapa
        self.hide_map()
        
        # Ocultar sugerencias
        self.suggestions1.visible = False
        self.suggestions1.controls.clear()
        self.suggestions2.visible = False
        self.suggestions2.controls.clear()
        
        # Actualizar toda la página
        self.page.update()



