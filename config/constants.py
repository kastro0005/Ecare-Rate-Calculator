#Seccion de los base rates de acuerdo a cada nivel de servicio de cada proveedor

# Lista de tarifas base por nivel de servicio estandard
LEVEL_OF_SERVICE_BASE_RATES = {
    "WCH": 100,   # Silla de ruedas
    "STR": 175,  # Camilla
    "BLS": 450,   # Soporte vital básico
    "ALS": 550,   # Soporte vital avanzado
    "CCT": 950,   # Transporte de cuidado critico
    
}

# Lista de tarifas base por nivel de servicio de Baptist
LEVEL_OF_SERVICE_BASE_RATES_BAPTIST = {
    "WCH": 80,   # Silla de ruedas
    "STR": 100,  # Camilla
    "BLS": 450,   # Soporte vital básico
    "ALS": 550,   # Soporte vital avanzado
    "CCT": 950,   # Transporte de cuidado critico
    
}

# Lista de tarifas base por nivel de servicio de HCA
LEVEL_OF_SERVICE_BASE_RATES_HCA = {
    "WCH": 70,   # Silla de ruedas
    "STR": 105,  # Camilla
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
    
    
}

# tarifa por hora de tiempo de espera
WAITING_TIME_RATE = {
    "WCH": 50,
    "STR": 75,
    "BLS": 100,
    "ALS": 150,
    "CCT": 200,
} 

# Configuración de geolocalización
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
ROAD_DISTANCE_FACTOR = 1.3  # Factor para estimar distancia por carretera


