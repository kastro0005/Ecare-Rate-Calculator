import flet as ft
from typing import Dict, Callable
from config.constants import *

class RatesDialog:
    @staticmethod
    def create_dialog(save_callback: Callable, close_callback: Callable, provider="Default"):
        rates_inputs = {}

        # Selecciona el diccionario de rates según proveedor
        if provider == "Baptist":
            rates_dict = LEVEL_OF_SERVICE_BASE_RATES_BAPTIST
        elif provider == "HCA":
            rates_dict = LEVEL_OF_SERVICE_BASE_RATES_HCA
        else:
            rates_dict = LEVEL_OF_SERVICE_BASE_RATES

        content = ft.Column(
            [
                ft.TextField(
                    label=los,
                    value=str(rate),
                    width=200,
                    ref=lambda ref, los=los: rates_inputs.setdefault(los, ref)
                ) for los, rate in rates_dict.items()
            ],
            scroll=ft.ScrollMode.AUTO,
            height=300
        )
        dialog = ft.AlertDialog(
            title=ft.Text(f"Configurar Tarifas ({provider})"),
            content=content,
            actions=[
                ft.TextButton("Guardar", on_click=save_callback),
                ft.TextButton("Cancelar", on_click=close_callback),
            ]
        )
        return dialog, rates_inputs