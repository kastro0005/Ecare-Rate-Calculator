from setuptools import setup, find_packages
import os

# Leer el contenido del README.md si existe
def read_readme():
    if os.path.exists('README.md'):
        with open('README.md', 'r', encoding='utf-8') as f:
            return f.read()
    return ''

# Leer requirements.txt si existe
def read_requirements():
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    # Información básica del proyecto
    name="URBIS Rate Calculator",
    version="1.0.2",
    author="Adrian C Sierra DBA Sierra-Esperanza Creations LLC",
    author_email="sierraesperanza.creations@gmail.com",
    description="Rate calculator ",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    
    # URL del proyecto (si tienes repositorio)
    url="https://github.com/usuario/proyecto",
    
    # Encontrar paquetes automáticamente
    packages=find_packages(exclude=['tests*', 'docs*']),
    
    # Incluir archivos no-Python
    package_data={
        'mi_aplicacion': [
            'assets/*',  # Incluir todos los archivos en la carpeta assets
            'modulos/*.py',  # Incluir archivos Python en modulos
            'config/*.json',  # Incluir archivos de configuración
        ],
    },
    
    # Archivos adicionales que no son Python
    include_package_data=True,
    
    # Dependencias del proyecto
    install_requires=[
        'flet',
        'pygeo',
        # Agrega aquí tus otras dependencias
        # O usa la función read_requirements()
    ] + read_requirements(),
    
    # Dependencias opcionales
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'flake8',
            'black',
            'mypy',
        ],
    },
    
    # Metadata para PyPI
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    
    # Requisitos de Python
    python_requires=">=3.8",
    
    # Punto de entrada para la aplicación
    entry_points={
        'console_scripts': [
            'mi_aplicacion=mi_aplicacion.main:main',
        ],
    },
)
