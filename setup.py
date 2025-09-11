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
    
    # URL del proyecto
    url="https://github.com/usuario/ecare-rate-calculator",
    
    # Encontrar paquetes automáticamente
    packages=find_packages(exclude=['tests*', 'docs*', 'env*', 'build*', 'dist*']),
    
    # Incluir archivos no-Python
    package_data={
        '': [
            'assets/*',  # Incluir todos los archivos en la carpeta assets
            'config/*.py',  # Incluir archivos de configuración
            'ui/*.html',  # Incluir templates HTML
            '*.ico',  # Incluir iconos
            '*.png',  # Incluir imágenes
        ],
    },
    
    # Archivos adicionales que no son Python
    include_package_data=True,
    
    # Dependencias del proyecto
    install_requires=[
        'flet>=0.10.0',
        'geopy>=2.3.0',
        'requests>=2.32.0',
        'pydantic>=2.3.0',
        'python-dotenv>=1.0.0',
        'Pillow>=10.0.0',
        'aiohttp>=3.10.0',
        'httpx>=0.24.0',
    ],
    
    # Dependencias opcionales para desarrollo
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'flake8>=5.0.0',
            'black>=22.0.0',
            'mypy>=1.0.0',
        ],
        'build': [
            'pyinstaller>=5.13.0',
            'pyinstaller-hooks-contrib>=2023.8',
        ],
    },
    
    # Clasificadores del proyecto
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Environment :: X11 Applications",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
    ],
    
    # Requisitos de Python
    python_requires=">=3.8",
    
    # Puntos de entrada para scripts de consola
    entry_points={
        'console_scripts': [
            'ecare-calculator=main:main',
            'ecare-rate-calc=run:main',
        ],
    },
    
    # Palabras clave para búsqueda
    keywords='medical transport rate calculator emergency healthcare billing',
    
    # Información del proyecto
    project_urls={
        'Bug Reports': 'https://github.com/usuario/ecare-rate-calculator/issues',
        'Source': 'https://github.com/usuario/ecare-rate-calculator',
        'Documentation': 'https://github.com/usuario/ecare-rate-calculator#readme',
    },
)
