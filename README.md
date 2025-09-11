# ECARE Rate Calculator

![Version](https://img.shields.io/badge/version-1.0.2-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## 📋 Descripción

ECARE Rate Calculator es una aplicación de escritorio desarrollada con **Flet** que permite calcular tarifas de transporte médico de emergencia basadas en diferentes parámetros como distancia, nivel de servicio, horarios, y servicios adicionales. La aplicación está diseñada para proveedores de servicios médicos de emergencia y permite calcular tarifas para diferentes proveedores (Baptist, HCA, y tarifas estándar).

## ✨ Características Principales

- **Cálculo de Tarifas Dinámico**: Calcula tarifas basadas en distancia y nivel de servicio
- **Múltiples Proveedores**: Soporte para Baptist, HCA y tarifas estándar
- **Servicios Adicionales**: 
  - Oxígeno (O2) con cálculo por litros
  - Servicios fuera de horario (After Hours)
  - Transporte de ida y vuelta (Deadheads)
  - Servicios de cuidado especial (STC)
  - Transporte bariátrico
  - Tiempo de espera
- **Niveles de Servicio**:
  - WCH (Wheelchair - Silla de ruedas)
  - STR (Stretcher - Camilla)
  - BLS (Basic Life Support - Soporte vital básico)
  - ALS (Advanced Life Support - Soporte vital avanzado)
  - CCT (Critical Care Transport - Transporte de cuidado crítico)
- **Interfaz Gráfica Moderna**: Desarrollada con Flet para una experiencia de usuario intuitiva
- **Geolocalización**: Integración con servicios de ubicación para cálculo automático de distancias
- **Autocompletado de Direcciones**: Funcionalidad de autocompletado para direcciones

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **Flet**: Framework para aplicaciones de escritorio multiplataforma
- **GeoPy**: Para servicios de geolocalización
- **Requests**: Para llamadas a APIs
- **PyInstaller**: Para crear ejecutables

## 📦 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación desde el código fuente

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/usuario/ecare-rate-calculator.git
   cd ecare-rate-calculator
   ```

2. **Crear un entorno virtual** (recomendado):
   ```bash
   python -m venv env
   ```

3. **Activar el entorno virtual**:
   - Windows:
     ```bash
     env\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

### Instalación usando setup.py

```bash
pip install -e .
```

## 🚀 Uso

### Ejecutar la aplicación

#### Modo desarrollo:
```bash
python main.py
```

#### Usando el script de ejecución:
```bash
python run.py
```

### Crear ejecutable

Para crear un ejecutable independiente:

```bash
pyinstaller main.spec
```

O usar el script de construcción en Windows:
```bash
build.bat
```

## 📖 Guía de Uso

1. **Seleccionar Proveedor**: Elige entre Baptist, HCA o tarifas estándar
2. **Ingresar Ubicaciones**: 
   - Dirección de origen
   - Dirección de destino
   - La aplicación calculará automáticamente la distancia
3. **Seleccionar Nivel de Servicio**: WCH, STR, BLS, ALS, o CCT
4. **Configurar Servicios Adicionales**:
   - Marcar casillas según los servicios requeridos
   - Especificar litros de oxígeno si es necesario
   - Indicar tiempo de espera si aplica
5. **Calcular Tarifa**: La aplicación mostrará el costo total desglosado

## 📁 Estructura del Proyecto

```
ecare-rate-calculator/
├── main.py                 # Archivo principal de la aplicación
├── run.py                  # Script alternativo de ejecución
├── setup.py               # Configuración de instalación
├── requirements.txt       # Dependencias del proyecto
├── main.spec             # Configuración de PyInstaller
├── build.bat             # Script de construcción para Windows
├── README.md             # Documentación del proyecto
├── .gitignore            # Archivos ignorados por Git
├── assets/               # Recursos estáticos
│   └── icon.ico         # Icono de la aplicación
├── config/              # Configuraciones
│   ├── __init__.py
│   └── constants.py     # Constantes y tarifas
├── services/            # Servicios de la aplicación
│   ├── __init__.py
│   ├── rate_service.py          # Lógica de cálculo de tarifas
│   ├── location_service.py      # Servicios de geolocalización
│   └── address_autocomplete_service.py  # Autocompletado de direcciones
├── ui/                  # Interfaz de usuario
│   ├── __init__.py
│   ├── components.py    # Componentes de la UI
│   ├── dialogs.py       # Diálogos y ventanas modales
│   └── map_template.html # Template para mapas
└── utils/               # Utilidades
    ├── __init__.py
    ├── exceptions.py    # Excepciones personalizadas
    └── geolocate.py     # Utilidades de geolocalización
```

## ⚙️ Configuración

### Tarifas y Constantes

Las tarifas se configuran en `config/constants.py`:

- `LEVEL_OF_SERVICE_BASE_RATES`: Tarifas base estándar
- `LEVEL_OF_SERVICE_BASE_RATES_BAPTIST`: Tarifas específicas de Baptist
- `LEVEL_OF_SERVICE_BASE_RATES_HCA`: Tarifas específicas de HCA
- `LEVEL_OF_SERVICE_INCREMENTS`: Incrementos por milla
- `EXTRAS`: Costos de servicios adicionales
- `WAITING_TIME_RATE`: Tarifas por tiempo de espera

### Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto para configurar:

```env
# APIs de geolocalización (si es necesario)
GEOCODING_API_KEY=tu_api_key_aqui

# Configuración de logging
LOG_LEVEL=INFO

# Configuración de la aplicación
APP_DEBUG=False
```

## 🧪 Testing

Para ejecutar las pruebas (cuando estén disponibles):

```bash
pytest tests/
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Changelog

### v1.0.2
- Mejoras en la interfaz de usuario
- Corrección de bugs en el cálculo de tarifas
- Optimización del rendimiento

### v1.0.1
- Implementación de múltiples proveedores
- Adición de servicios adicionales

### v1.0.0
- Lanzamiento inicial
- Funcionalidad básica de cálculo de tarifas

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- **Adrian C. Sierra** - *Desarrollo Principal* - [Sierra-Esperanza Creations LLC](mailto:sierraesperanza.creations@gmail.com)
- **Ariel Chacon** - *Desarrollo Principal*

## 📞 Soporte

Para soporte técnico o preguntas:
- Email: sierraesperanza.creations@gmail.com
- Crear un issue en GitHub

## 🙏 Agradecimientos

- Equipo de Flet por el excelente framework
- Comunidad de Python por las librerías utilizadas
- Proveedores de servicios médicos por los requerimientos y feedback

---

**Nota**: Esta aplicación está diseñada específicamente para el cálculo de tarifas de transporte médico de emergencia y debe ser utilizada por profesionales del sector.