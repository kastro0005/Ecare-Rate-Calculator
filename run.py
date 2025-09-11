import os
import flet as ft
from main import main

if __name__ == "__main__":
    # Para despliegue web
    port = int(os.environ.get("PORT", 8080))
    ft.app(
        target=main,
        view=ft.WEB_BROWSER,
        port=port,
        host="0.0.0.0"  # Importante para producción
    )