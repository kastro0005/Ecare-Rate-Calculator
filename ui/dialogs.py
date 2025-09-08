import flet as ft
from typing import Dict, Callable
from config.constants import LEVEL_OF_SERVICE_BASE_RATES

class RatesDialog:
    @staticmethod
    def create_dialog(save_callback: Callable, close_callback: Callable) -> ft.AlertDialog:
        rates_inputs = {}
        
        content = ft.Column(
            [
                ft.TextField(
                    label=los,
                    value=str(rate),
                    width=200
                ) for los, rate in LEVEL_OF_SERVICE_BASE_RATES.items()
            ],
            scroll=ft.ScrollMode.AUTO,
            height=300
        )

        return ft.AlertDialog(
            title=ft.Text("Configurar Tarifas"),
            content=content,
            actions=[
                ft.TextButton("Guardar", on_click=save_callback),
                ft.TextButton("Cancelar", on_click=close_callback),
            ]
        )