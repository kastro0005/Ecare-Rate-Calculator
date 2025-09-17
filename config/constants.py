#Seccion de los base rates de acuerdo a cada nivel de servicio de cada proveedor

# Lista de tarifas base por nivel de servicio estandard
LEVEL_OF_SERVICE_BASE_RATES = {
    "WCH": 100,   # Silla de ruedas
    "STR": 175,  # Camilla
    "BLS NE": 450,   # Soporte vital básico
    "BLS ER": 500, # Soporte vital básico con especialista
    "ALS NE": 550,   # Soporte vital avanzado
    "ALS ER": 600,   # Soporte vital avanzado con especialista
    "ALS2": 800,  # Soporte vital avanzado nivel 2
    "CCT": 950,   # Transporte de cuidado critico

    
}

# Incrementos por milla por nivel de servicio Standard
LEVEL_OF_SERVICE_INCREMENTS = {
    "WCH": 5,
    "STR": 9,
    "BLS NE": 13,
    "BLS ER": 13, # Soporte vital básico con especialista
    "ALS NE": 13 ,
    "ALS ER": 13 ,  
    "ALS2": 13,  # Soporte vital avanzado nivel 2
    "CCT": 13 , 
}

#Incrementos Extras

EXTRAS = {
    "O2": 30,  # por litro
    "AfterHours": 150,  #plus for after hours
    "STC": 250,
    "Bariatric": 350,
    
}

# tarifa por hora de tiempo de espera
WAITING_TIME_RATE = {
    "WCH": 50,
    "STR": 75,
    "BLS NE": 100,
    "BLS ER": 500, # Soporte vital básico con especialista
    "ALS NE": 150,
    "ALS ER": 600,
    "ALS2": 800,  # Soporte vital avanzado nivel 2
    "CCT": 200,
} 






"""Aqui van los base rates de los otros proveedores, si se quiere agregar otro proveedor
solo hay que agregar otro diccionario con las tarifas base de ese proveedor y manteniendo
 los mismos niveles de servicio y estructura, y orden que los demas diccionarios
"""


# Lista de tarifas base por nivel de servicio de Baptist
LEVEL_OF_SERVICE_BASE_RATES_BAPTIST = {
    "WCH": 65,   # Silla de ruedas
    "STR": 150,  # Camilla
    "BLS NE": 28416,   # Soporte vital básico
    "BLS ER": 45466, # Soporte vital básico con especialista
    "ALS NE": 340.99,   # Soporte vital avanzado
    "ALS ER": 539.91,   # Soporte vital avanzado con especialista
    "ALS2": 781.44,  # Soporte vital avanzado nivel 2
    "CCT": 923.52,   # Transporte de cuidado critico
    
}

# Lista de tarifas base por nivel de servicio de HCA
LEVEL_OF_SERVICE_BASE_RATES_HCA = {
    "WCH": 70,   # Silla de ruedas
    "STR": 105,  # Camilla
    "BLS NE": 450,   # Soporte vital básico
    "BLS ER": 550, # Soporte vital básico con especialista
    "ALS NE": 500,   # Soporte vital avanzado
    "ALS ER": 600,   # Soporte vital avanzado con especialista
    "ALS2": 800,  # Soporte vital avanzado nivel 2
    "CCT": 950,   # Transporte de cuidado critico
    
}

# Lista de tarifas base por nivel de servicio de Tenants
LEVEL_OF_SERVICE_BASE_RATES_TENANTS = {
    "WCH": 65,   # Silla de ruedas
    "STR": 150,  # Camilla
    "BLS NE": 284.16,   # Soporte vital básico
    "BLS ER": 454.66, # Soporte vital básico con especialista
    "ALS NE": 340.99,   # Soporte vital avanzado
    "ALS ER": 539.91,   # Soporte vital avanzado con especialista
    "ALS2": 781.84,  # Soporte vital avanzado nivel 2
    "CCT": 923.52,   # Transporte de cuidado critico
    
}
# Incrementos por milla por nivel de servicio
LEVEL_OF_SERVICE_INCREMENTS_TENANTS = {
    "WCH": 2.5,
    "STR": 3.5,
    "BLS NE": 9.15,
    "BLS ER": 9.15, # Soporte vital básico con especialista
    "ALS NE": 9.15 ,
    "ALS ER": 9.15 ,  
    "ALS2": 9.15,  # Soporte vital avanzado nivel 2
    "CCT": 9.15 , 
}






"""Constantes para la parte de geolocalización y cálculo de rutas
   realmente no se usan demasiados y no son tan im[portantes pero quizas mada delnate si]"""


# Configuración de geolocalización
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
ROAD_DISTANCE_FACTOR = 1.3  # Factor para estimar distancia por carretera


