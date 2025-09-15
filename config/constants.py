#Seccion de los base rates de acuerdo a cada nivel de servicio de cada proveedor

# Lista de tarifas base por nivel de servicio estandard
LEVEL_OF_SERVICE_BASE_RATES = {
    "WCH": 100,   # Silla de ruedas
    "STR": 175,  # Camilla
    "BLS": 450,   # Soporte vital básico
    "BLS ER": 500, # Soporte vital básico con especialista
    "ALS NE": 550,   # Soporte vital avanzado
    "ALS ER": 600,   # Soporte vital avanzado con especialista
    "ALS2": 800,  # Soporte vital avanzado nivel 2
    "CCT": 950,   # Transporte de cuidado critico

    
}

# Lista de tarifas base por nivel de servicio de Baptist
LEVEL_OF_SERVICE_BASE_RATES_BAPTIST = {
    "WCH": 80,   # Silla de ruedas
    "STR": 100,  # Camilla
    "BLS": 450,   # Soporte vital básico
    "BLS ER": 500, # Soporte vital básico con especialista
    "ALS NE": 550,   # Soporte vital avanzado
    "ALS ER": 600,   # Soporte vital avanzado con especialista
    "ALS2": 800,  # Soporte vital avanzado nivel 2
    "CCT": 950,   # Transporte de cuidado critico
    
}

# Lista de tarifas base por nivel de servicio de HCA
LEVEL_OF_SERVICE_BASE_RATES_HCA = {
    "WCH": 70,   # Silla de ruedas
    "STR": 105,  # Camilla
    "BLS": 450,   # Soporte vital básico
    "BLS ER": 500, # Soporte vital básico con especialista
    "ALS NE": 550,   # Soporte vital avanzado
    "ALS ER": 600,   # Soporte vital avanzado con especialista
    "ALS2": 800,  # Soporte vital avanzado nivel 2
    "CCT": 950,   # Transporte de cuidado critico
    
}






# Incrementos por milla por nivel de servicio
LEVEL_OF_SERVICE_INCREMENTS = {
    "WCH": 5,
    "STR": 9,
    "BLS": 11.5,
    "BLS ER": 11.5, # Soporte vital básico con especialista
    "ALS NE": 11.5 ,
    "ALS ER": 11.5 ,  
    "ALS2": 11.5,  # Soporte vital avanzado nivel 2
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
    "BLS ER": 500, # Soporte vital básico con especialista
    "ALS NE": 150,
    "ALS ER": 600,
    "ALS2": 800,  # Soporte vital avanzado nivel 2
    "CCT": 200,
} 


"""Constantes para la parte de geolocalización y cálculo de rutas
   realmente no se usan demasiados y no son tan im[portantes pero quizas mada delnate si]"""


# Configuración de geolocalización
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
ROAD_DISTANCE_FACTOR = 1.3  # Factor para estimar distancia por carretera


