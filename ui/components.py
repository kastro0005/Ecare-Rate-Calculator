import flet as ft
from typing import Callable
from config.constants import LEVEL_OF_SERVICE_BASE_RATES


from services.address_autocomplete_service import AddressAutocompleteService
from threading import Thread

class RateCalculatorUI:
    def __init__(self, calculate_callback: Callable, open_rates_dialog_callback: Callable):
        self.calculate_callback = calculate_callback
        self.open_rates_dialog_callback = open_rates_dialog_callback

        self.suggestions1 = ft.ListView(visible=False, spacing=2, height=120, width=300)
        self.suggestions2 = ft.ListView(visible=False, spacing=2, height=120, width=300)

        self.address1 = ft.TextField(
            label="Dirección 1",
            hint_text="Ingrese la primera dirección",
            width=300,
            on_change=self.on_address1_change,
            on_blur=self.on_address1_blur
        )
        self.address2 = ft.TextField(
            label="Dirección 2",
            hint_text="Ingrese la segunda dirección",
            width=300,
            on_change=self.on_address2_change,
            on_blur=self.on_address2_blur
        )

        self.distance_mode = ft.Tabs(
            selected_index=0,
            on_change=self.on_mode_change,
            tabs=[
                ft.Tab(text="Calcular por direcciones"),
                ft.Tab(text="Ingresar millas manualmente")
            ]
        )

        self.manual_miles = ft.TextField(
            label="Millas",
            hint_text="Ingrese la distancia en millas",
            width=300,
            visible=False,
            keyboard_type=ft.KeyboardType.NUMBER
        )

        self.service_level = ft.Dropdown(
            label="Nivel de Servicio",
            hint_text="Elija el nivel de servicio",
            options=[ft.dropdown.Option(los) for los in LEVEL_OF_SERVICE_BASE_RATES.keys()],
            width=200
        )

        self.after_hours = ft.Checkbox(label="Viaje después de horas (después de 7pm)")
        self.deadheads = ft.Checkbox(label="Viaje Round Trip")
        self.roundtrip = ft.Checkbox(label="Viaje Roundtrip)")
        #intento de poner otros dos checkboxes
        self.o2 = ft.Checkbox(label="Oxígeno")
        self.isolation = ft.Checkbox(label="Aislamiento")
        self.covid = ft.Checkbox(label="Covid")
        self.stairchair = ft.Checkbox(label="Escalera")

        
        # Indicador de progreso y mensajes de estado
        self.progress = ft.ProgressBar(visible=False)
        self.status_text = ft.Text("")
        self.result = ft.Text(size=20, weight=ft.FontWeight.BOLD)

        self.calculate_button = ft.ElevatedButton(
            text="Calcular",
            on_click=self.calculate_callback,
            icon=ft.icons.CALCULATE
        )
        self.rates_button = ft.ElevatedButton(
            text="Configurar Tarifas",
            on_click=self.open_rates_dialog_callback,
            icon=ft.icons.SETTINGS
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

    #Metodo de organizar el layout
    def get_layout(self) -> ft.Column:
        """Retorna el layout completo de la UI"""
        return ft.Column(
            [
                ft.Row([self.distance_mode], alignment=ft.MainAxisAlignment.CENTER),
                self.address_container,
                self.manual_container,
                ft.Row([self.service_level], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.after_hours, self.deadheads], alignment=ft.MainAxisAlignment.CENTER),
                #Aki estoy intentando poner los otros dos checkboxes
                ft.Row([self.o2, self.isolation], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.covid, self.stairchair], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.calculate_button, self.rates_button], alignment=ft.MainAxisAlignment.CENTER),
                self.progress,
                self.status_text,
                self.result
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
            f"Distancia: {result_data['distance']} millas\n"
            f"Tarifa base: ${result_data['base_rate']}\n"
            f"Tarifa total: ${result_data['total_rate']}"
        )