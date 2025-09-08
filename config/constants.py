# Lista de tarifas base por nivel de servicio
LEVEL_OF_SERVICE_BASE_RATES = {
    "WCH": 100,   # Silla de ruedas
    "STR": 175,  # Camilla
    "BLS": 450,   # Soporte vital básico
    "ALS": 550,   # Soporte vital avanzado
    "CCT": 950,   # Transporte de cuidado critico
    
}

# Incrementos por milla por nivel de servicio
LEVEL_OF_SERVICE_INCREMENTS = {
    "WCH": 5,
    "STR": 9,
    "BLS": 11.5,
    "ALS": 11.5 ,  
    "CCT": 11.5 , 
}

#Incrementos Extras

EXTRAS = {
    "O2": 30,  # por litro
    "AfterHours": 150,  #plus for after hours
    "STC": 400,
    "Bariatric": 300,
    "WaitinfTime": 0, # por cada 30 minutos
    
}

# Configuración de geolocalización
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
ROAD_DISTANCE_FACTOR = 1.3  # Factor para estimar distancia por carretera


