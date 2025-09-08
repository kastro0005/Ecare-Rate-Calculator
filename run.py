import sys
import os

# Añade el directorio del proyecto al PYTHONPATH
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

from main import main
import flet as ft

if __name__ == "__main__":
    ft.app(target=main)