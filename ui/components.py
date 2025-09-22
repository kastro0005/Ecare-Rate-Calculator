import flet as ft
from typing import Callable
from config.constants import *

from services.google_places_service import get_google_maps_distance

class RateCalculatorUI:
    def __init__(self, page, calculate_callback: Callable, open_rates_dialog_callback: Callable):
        self.page = page
        self.calculate_callback = calculate_callback
        self.open_rates_dialog_callback = open_rates_dialog_callback

        # Campos de texto para la direccion 1
        self.address1 = ft.TextField(
            label="First Address",
            hint_text="Enter the first address",
            width=300,
        )
       # Campos de texto para la direccion 2
        self.address2 = ft.TextField(
            label="Second Address",
            hint_text="Enter the second address",
            width=300,
        )
        # Modo de distancia: Direcciones o manual
        self.distance_mode = ft.Tabs(
            selected_index=0,
            on_change=self.on_mode_change,
            tabs=[
                ft.Tab(text="Calculate from addresses"),
                ft.Tab(text="Enter distance manually")
            ]
        )
        # Campo de texto para ingresar millas manualmente
        self.manual_miles = ft.TextField(
            label="Miles",
            hint_text="Enter the Miles",
            width=300,
            visible=False,
            keyboard_type=ft.KeyboardType.NUMBER
        )
        # Dropdown para seleccionar el nivel de servicio
        self.service_level = ft.Dropdown(
            label="Level of Service",
            hint_text="Choose Level of Service",
            options=[ft.dropdown.Option(los) for los in LEVEL_OF_SERVICE_BASE_RATES.keys()],
            width=200
        )
        # Otros campos y checkboxes
        self.o2 = ft.TextField("", width=100, keyboard_type=ft.KeyboardType.NUMBER, disabled=True, on_change=self.validate_decimal)
        self.liters_o2 = ft.Checkbox(label="Liters of Oxygen", on_change=self.on_liters_o2_change )
        self.after_hours = ft.Checkbox(label="Afterhours (6pm-6am)")
        self.deadheads = ft.Checkbox(label="Round Trip")
        self.roundtrip = ft.Checkbox(label="Roundtrip)")     
        self.bariatric = ft.Checkbox(label="Bariatric")
        self.stairchair = ft.Checkbox(label="Stairchair")
        self.waiting_time = ft.TextField("", width=100, keyboard_type=ft.KeyboardType.NUMBER, disabled=True,on_change=self.validate_decimal)
        self.wait = ft.Checkbox(label="Waiting Time (Hours)", on_change=self.on_waiting_change)
        # Dropdowns para seleccionar el condado y la configuracion con Palm beach como default
        self.county_selector = ft.Dropdown(
            label="County",
            options=[ft.dropdown.Option(c) for c in COUNTY_PROVIDERS.keys()],
            value="Palm Beach",
            width=200,
            on_change=self.on_county_change
        )
        # Configuracion de proveedores segun el condado
        self.config_selector = ft.Dropdown(
            label="Source",
            options=[ft.dropdown.Option(p) for p in COUNTY_PROVIDERS["Palm Beach"]],
            value=COUNTY_PROVIDERS["Palm Beach"][0],
            width=200,
        )
        # Barra de progreso y textos para estado y resultado
        self.progress = ft.ProgressBar(visible=False)
        self.status_text = ft.Text("")
        self.result = ft.Text(size=20, weight=ft.FontWeight.BOLD)

        #Boton de calcular 
        self.calculate_button = ft.ElevatedButton(
            text="Calculate Rate",
            on_click=self.calculate_callback,
            icon="calculate"
        )
        #Boton para abrir dialogo de configuracion de tarifas
        self.rates_button = ft.ElevatedButton(
            text="Configurate Rates",
            on_click=self.open_rates_dialog_callback,
            icon="settings"
        )

        self.map_link = ft.TextButton(
            text="Show route on Google Maps",
            visible=False,
            url="",
            style=ft.ButtonStyle(color="blue")
        )
        # Contenedores para organizar la interfaz
        self.address_container = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Column([
                        self.address1,
                    ])
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.Column([
                        self.address2,
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

    def get_layout(self) -> ft.Column:
        return ft.Column(
            [   
                ft.Row([self.county_selector], alignment=ft.MainAxisAlignment.END),
                ft.Row([self.config_selector], alignment=ft.MainAxisAlignment.END),
                ft.Row([self.distance_mode], alignment=ft.MainAxisAlignment.CENTER),
                self.address_container,
                self.manual_container,
                ft.Row([self.service_level], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.after_hours, self.deadheads], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.liters_o2,self.o2], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.bariatric, self.stairchair], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.wait, self.waiting_time], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.calculate_button, self.rates_button], alignment=ft.MainAxisAlignment.CENTER),
                self.progress,
                self.status_text,
                self.result,
                self.map_link,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )

    def is_manual_mode(self) -> bool:
        return self.distance_mode.selected_index == 1

    def get_distance(self) -> float:
        try:
            return float(self.manual_miles.value or 0)
        except ValueError:
            raise ValueError("Por favor, ingrese un valor numérico válido para las millas")

    def update_status(self, message: str, is_error: bool = False) -> None:
        self.status_text.value = message
        self.status_text.color = "red" if is_error else "black"

    def set_progress(self, visible: bool) -> None:
        self.progress.visible = visible

    def update_result(self, result_data: dict) -> None:
        self.result.value = (
            f"Distance: {result_data['distance']} miles\n"
            f"Rate Base: ${result_data['base_rate']}\n"
            f"Total Rate: ${result_data['total_rate']}"
        )

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
                self.update_status("Por favor, ingrese ambas direcciones", is_error=True)
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
            self.update_status(f"Error al calcular la tarifa: {str(e)}", is_error=True)



