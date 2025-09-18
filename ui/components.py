import flet as ft
from typing import Callable
from config.constants import *
import importlib

from services.address_autocomplete_service import AddressAutocompleteService
from threading import Thread

class RateCalculatorUI:
    def __init__(self, calculate_callback: Callable, open_rates_dialog_callback: Callable):
        self.calculate_callback = calculate_callback
        self.open_rates_dialog_callback = open_rates_dialog_callback

        self.suggestions1 = ft.ListView(visible=False, spacing=2, height=120, width=300)
        self.suggestions2 = ft.ListView(visible=False, spacing=2, height=120, width=300)

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
            selected_index=0,  # Esto selecciona "Enter distance manually" por defecto cambiar a 0 si quieres que sea por
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

        #Aki empiezan los checkboxes y campos de texto
        



        # Campo de texto de los litros de O2
        self.o2 = ft.TextField("", width=100, keyboard_type=ft.KeyboardType.NUMBER, disabled=True, on_change=self.validate_decimal  # <-- Valida el decimal
)

        #checkboxe del Oxygeno conexctada al campo de texto
        self.liters_o2 = ft.Checkbox(label="Liters of Oxygen", on_change=self.on_liters_o2_change )

        #Resto de checkboxes
        self.after_hours = ft.Checkbox(label="Afterhours (6pm-6am)")
        self.deadheads = ft.Checkbox(label="Round Trip")
        self.roundtrip = ft.Checkbox(label="Roundtrip)")     
        self.bariatric = ft.Checkbox(label="Bariatric")
        self.stairchair = ft.Checkbox(label="Stairchair")

        # Campo de texto de las horas de espera
        self.waiting_time = ft.TextField("", width=100, keyboard_type=ft.KeyboardType.NUMBER, disabled=True,on_change=self.validate_decimal)

        #checkboxe del Waiting time
        self.wait = ft.Checkbox(label="Waiting Time (Hours)", on_change=self.on_waiting_change)
        
        #Selector de configuracion de Condado
        self.county_selector = ft.Dropdown(
    label="County",
    options=[
        ft.dropdown.Option("Palm Beach"),
        ft.dropdown.Option("Broward"),
        ft.dropdown.Option("Monroe"),
        ft.dropdown.Option("Citrus"),
    ],
    value="Palm Beach",
    width=200,
    on_change=self.on_county_change  # <-- conecta el callback
)

        # Selector de configuración de Provider
        self.config_selector = ft.Dropdown(label="Source", options=[ft.dropdown.Option("Standard"),
                                                                           ft.dropdown.Option("Baptist"),
                                                                           ft.dropdown.Option("Jupiter Medical Center"),
                                                                            ft.dropdown.Option("Tenants (PBHN)"),
                                                                            ft.dropdown.Option("Arbor Trail Rehab and Skilled Nursing Center"),
                                                                            ft.dropdown.Option("Cedar Creek"),
                                                                            ft.dropdown.Option("Citrus Health and Rehab Center"),
                                                                            ft.dropdown.Option("Clearsky Rehab Hospital of Lecanto"),
                                                                            ft.dropdown.Option("Crystal River Health and Rehab Center"),
                                                                            ft.dropdown.Option("Diamond Ridge Health and Rehab Center"),
                                                                            ft.dropdown.Option("Sunflower Springs"),
                                                                            ft.dropdown.Option("Superior Residences of Lecanto"),
                                                                            ft.dropdown.Option("Tampa General Hospital Crystal River"),
                                                                            ft.dropdown.Option("TGH Crystal River Emergency Center"),
                                                                            ft.dropdown.Option("The Gardens Assisted Living and Memory Care"),
                                                                            ft.dropdown.Option("Vitas Inpatient Hospice"),
                                                                            ft.dropdown.Option("Amedysis Hospice"),
                                                                            ft.dropdown.Option("Baptist Miami"),
                                                                            ft.dropdown.Option("Oasis at the Keys Nursing and Rehab"),
                                                                            ft.dropdown.Option("Palm Vista Nursing and Rehab Center"),
                                                                            ft.dropdown.Option("Vitas Monroe"),
                             ],
                                                                           value="Standard",
                                                                           width=200,
                                                                           
                                            )


        # Indicador de progreso y mensajes de estado
        self.progress = ft.ProgressBar(visible=False)
        self.status_text = ft.Text("")
        self.result = ft.Text(size=20, weight=ft.FontWeight.BOLD)

        self.calculate_button = ft.ElevatedButton(
            text="Calculate Rate",
            on_click=self.calculate_callback,
            icon="calculate"  # <-- Usar el nombre del icono como string
        )
        self.rates_button = ft.ElevatedButton(
            text="Configurate Rates",
            on_click=self.open_rates_dialog_callback,
            icon="settings"   # <-- Usar el nombre del icono como string
        )

        self.map_link = ft.TextButton(
            text="Ver ruta en Google Maps",
            visible=False,
            url="",  # Se actualizará dinámicamente
            style=ft.ButtonStyle(color="blue")
        )

        self.address_container = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Column([self.address1, self.suggestions1])
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.Column([self.address2, self.suggestions2])
                ], alignment=ft.MainAxisAlignment.CENTER),
            ])
        )

        self.manual_container = ft.Container(
            content=ft.Column([
                ft.Row([self.manual_miles], alignment=ft.MainAxisAlignment.CENTER),
            ]),
            visible=False
        )

    def on_address1_change(self, e):
        query = self.address1.value.strip()
        if len(query) < 3:
            self.suggestions1.controls.clear()
            self.suggestions1.visible = False
            self.address1.update()
            self.suggestions1.update()
            return
        def fetch():
            suggestions = AddressAutocompleteService.get_suggestions(query)
            self.suggestions1.controls.clear()
            for suggestion in suggestions:
                self.suggestions1.controls.append(
                    ft.ListTile(
                        title=ft.Text(suggestion),
                        on_click=lambda e, s=suggestion: self.select_address1(s)
                    )
                )
            self.suggestions1.visible = bool(suggestions)
            self.suggestions1.update()
        Thread(target=fetch).start()

    def select_address1(self, suggestion):
        self.address1.value = suggestion
        self.suggestions1.visible = False
        self.address1.update()
        self.suggestions1.update()

    def on_address1_blur(self, e):
        self.suggestions1.visible = False
        self.suggestions1.update()

    def on_address2_change(self, e):
        query = self.address2.value.strip()
        if len(query) < 3:
            self.suggestions2.controls.clear()
            self.suggestions2.visible = False
            self.address2.update()
            self.suggestions2.update()
            return
        def fetch():
            suggestions = AddressAutocompleteService.get_suggestions(query)
            self.suggestions2.controls.clear()
            for suggestion in suggestions:
                self.suggestions2.controls.append(
                    ft.ListTile(
                        title=ft.Text(suggestion),
                        on_click=lambda e, s=suggestion: self.select_address2(s)
                    )
                )
            self.suggestions2.visible = bool(suggestions)
            self.suggestions2.update()
        Thread(target=fetch).start()

    def select_address2(self, suggestion):
        self.address2.value = suggestion
        self.suggestions2.visible = False
        self.address2.update()
        self.suggestions2.update()

    def on_address2_blur(self, e):
        self.suggestions2.visible = False
        self.suggestions2.update()

    def on_mode_change(self, e):
        """Maneja el cambio entre modos de entrada de distancia"""
        is_manual = self.distance_mode.selected_index == 1
        self.address_container.visible = not is_manual
        self.manual_container.visible = is_manual
        self.address1.visible = not is_manual
        self.address2.visible = not is_manual
        self.manual_miles.visible = is_manual
        self.update_status("")  # Limpiar mensajes de estado anteriores
        self.result.value = ""  # Limpiar resultados anteriores

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

    #Metodo de organizar el layout
    def get_layout(self) -> ft.Column:
        """Retorna el layout completo de la UI"""
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
                self.map_link,  # <-- Agrega el botón/enlace aquí
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )

    def is_manual_mode(self) -> bool:
        """Retorna True si está en modo manual de millas"""
        return self.distance_mode.selected_index == 1

    def get_distance(self) -> float:
        """Retorna la distancia ingresada manualmente"""
        try:
            return float(self.manual_miles.value or 0)
        except ValueError:
            raise ValueError("Por favor, ingrese un valor numérico válido para las millas")

    def update_status(self, message: str, is_error: bool = False) -> None:
        """Actualiza el mensaje de estado"""
        self.status_text.value = message
        self.status_text.color = "red" if is_error else "black"

    def set_progress(self, visible: bool) -> None:
        """Controla la visibilidad del indicador de progreso"""
        self.progress.visible = visible

    def update_result(self, result_data: dict) -> None:
        """Actualiza el texto de resultado"""
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

    #Metodo para asegurarnos que solo pongan numeros en el campo de texto de oxygeno y waiting time
    def validate_decimal(self, e):
        # Permite solo números con máximo un decimal
        import re
        value = e.control.value
        match = re.match(r"^\d+(\.\d{0,1})?$", value)
        if not match and value != "":
            # Elimina caracteres no válidos y limita a un decimal
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
        self.config_selector.value = providers[0]  # Selecciona el primero por defecto
        self.config_selector.update()



