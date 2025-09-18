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
LEVEL_OF_SERVICE_INCREMENTS_BAPTIST = {
    "WCH": 5,
    "STR": 9,
    "BLS NE": 13,
    "BLS ER": 13, # Soporte vital básico con especialista
    "ALS NE": 13 ,
    "ALS ER": 13 ,  
    "ALS2": 13,  # Soporte vital avanzado nivel 2
    "CCT": 13 , 
}

# Lista de tarifas base por nivel de servicio de HCA
LEVEL_OF_SERVICE_BASE_RATES_JUPITER_MEDICAL_CENTER = {
    "WCH": 70,   # Silla de ruedas
    "STR": 105,  # Camilla
    "BLS NE": 450,   # Soporte vital básico
    "BLS ER": 550, # Soporte vital básico con especialista
    "ALS NE": 500,   # Soporte vital avanzado
    "ALS ER": 600,   # Soporte vital avanzado con especialista
    "ALS2": 800,  # Soporte vital avanzado nivel 2
    "CCT": 950,   # Transporte de cuidado critico
    
}
LEVEL_OF_SERVICE_INCREMENTS_JUPITER_MEDICAL_CENTER = {
    "WCH": 5,
    "STR": 9,
    "BLS NE": 13,
    "BLS ER": 13, # Soporte vital básico con especialista
    "ALS NE": 13 ,
    "ALS ER": 13 ,  
    "ALS2": 13,  # Soporte vital avanzado nivel 2
    "CCT": 13 , 
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










"""Citrus County"""
# Lista de tarifas base por nivel de servicio de Arbor Trail Rehab and Skilled Nursing Center
LEVEL_OF_SERVICE_BASE_RATES_ARBOR_TRAIL_REHAB_AND_SKILLED_NURSING_CENTER = {
    "WCH": 65,   # Silla de ruedas
    "STR": 80,  # Camilla
    "BLS NE": 272.61,   # Soporte vital básico
    "BLS ER": 436.17, # Soporte vital básico con especialista
    "ALS NE": 327.13,   # Soporte vital avanzado
    "ALS ER": 517.96,   # Soporte vital avanzado con especialista
    "ALS2": 749.67,  # Soporte vital avanzado nivel 2
    "CCT": 885.98,   # Transporte de cuidado critico
    
}
# Incrementos por milla por nivel de servicio
LEVEL_OF_SERVICE_INCREMENTS_ARBOR_TRAIL_REHAB_AND_SKILLED_NURSING_CENTER = {
    "WCH": 3,
    "STR": 3,
    "BLS NE": 9.15,
    "BLS ER": 9.15, # Soporte vital básico con especialista
    "ALS NE": 9.15 ,
    "ALS ER": 9.15 ,  
    "ALS2": 9.15,  # Soporte vital avanzado nivel 2
    "CCT": 9.15 , 
}

# Lista de tarifas base por nivel de servicio de Cedar Creek
LEVEL_OF_SERVICE_BASE_RATES_CEDAR_CREEK = {
    "WCH": 65,   # Silla de ruedas
    "STR": 80,  # Camilla
    "BLS NE": 272.61,   # Soporte vital básico
    "BLS ER": 436.17, # Soporte vital básico con especialista
    "ALS NE": 327.13,   # Soporte vital avanzado
    "ALS ER": 517.96,   # Soporte vital avanzado con especialista
    "ALS2": 749.67,  # Soporte vital avanzado nivel 2
    "CCT": 885.98,   # Transporte de cuidado critico
    
}
# Incrementos por milla por nivel de servicio de Cedar Creek
LEVEL_OF_SERVICE_INCREMENTS_CEDAR_CREEK = {
    "WCH": 2.5,
    "STR": 5,
    "BLS NE": 9.15,
    "BLS ER": 9.15, # Soporte vital básico con especialista
    "ALS NE": 9.15 ,
    "ALS ER": 9.15 ,  
    "ALS2": 9.15,  # Soporte vital avanzado nivel 2
    "CCT": 9.15 , 
}
# Lista de tarifas base por nivel de servicio de Citrus Health and Rehab Center
LEVEL_OF_SERVICE_BASE_RATES_CITRUS_HEALTH_AND_REHAB_CENTER = {
    "WCH": 65,   # Silla de ruedas
    "STR": 150,  # Camilla
    "BLS NE": 272.61,   # Soporte vital básico
    "BLS ER": 436.17, # Soporte vital básico con especialista
    "ALS NE": 327.13,   # Soporte vital avanzado
    "ALS ER": 517.96,   # Soporte vital avanzado con especialista
    "ALS2": 749.67,  # Soporte vital avanzado nivel 2
    "CCT": 885.98,   # Transporte de cuidado critico
    
}
# Incrementos por milla por nivel de servicio de Cedar Creek
LEVEL_OF_SERVICE_INCREMENTS_CITRUS_HEALTH_AND_REHAB_CENTER = {
    "WCH": 2.5,
    "STR": 3.5,
    "BLS NE": 9.15,
    "BLS ER": 9.15, # Soporte vital básico con especialista
    "ALS NE": 9.15 ,
    "ALS ER": 9.15 ,  
    "ALS2": 9.15,  # Soporte vital avanzado nivel 2
    "CCT": 9.15 , 
}
# Lista de tarifas base por nivel de servicio de Clearsky Rehab Hospital of Lecanto
LEVEL_OF_SERVICE_BASE_RATES_CLEARSKY_REHAB_HOSPITAL_OF_LECANTO = {
    "WCH": 65,   # Silla de ruedas
    "STR": 80,  # Camilla
    "BLS NE": 272.61,   # Soporte vital básico
    "BLS ER": 436.17, # Soporte vital básico con especialista
    "ALS NE": 327.13,   # Soporte vital avanzado
    "ALS ER": 517.96,   # Soporte vital avanzado con especialista
    "ALS2": 749.67,  # Soporte vital avanzado nivel 2
    "CCT": 885.98,   # Transporte de cuidado critico
    
}
# Incrementos por milla por nivel de servicio de Cedar Creek
LEVEL_OF_SERVICE_INCREMENTS_CLEARSKY_REHAB_HOSPITAL_OF_LECANTO = {
    "WCH": 3,
    "STR": 3,
    "BLS NE": 9.15,
    "BLS ER": 9.15, # Soporte vital básico con especialista
    "ALS NE": 9.15 ,
    "ALS ER": 9.15 ,  
    "ALS2": 9.15,  # Soporte vital avanzado nivel 2
    "CCT": 9.15 , 
}
# Lista de tarifas base por nivel de servicio de Crystal River Health and Rehab Center
LEVEL_OF_SERVICE_BASE_RATES_CRYSTAL_RIVER_HEALTH_AND_REHAB_CENTER = {
    "WCH": 65,   # Silla de ruedas
    "STR": 80,  # Camilla
    "BLS NE": 272.61,   # Soporte vital básico
    "BLS ER": 436.17, # Soporte vital básico con especialista
    "ALS NE": 327.13,   # Soporte vital avanzado
    "ALS ER": 517.96,   # Soporte vital avanzado con especialista
    "ALS2": 749.67,  # Soporte vital avanzado nivel 2
    "CCT": 885.98,   # Transporte de cuidado critico
    
}
# Incrementos por milla por nivel de servicio de Cedar Creek
LEVEL_OF_SERVICE_INCREMENTS_CRYSTAL_RIVER_HEALTH_AND_REHAB_CENTER = {
    "WCH": 2.5,
    "STR": 5,
    "BLS NE": 9.15,
    "BLS ER": 9.15, # Soporte vital básico con especialista
    "ALS NE": 9.15 ,
    "ALS ER": 9.15 ,  
    "ALS2": 9.15,  # Soporte vital avanzado nivel 2
    "CCT": 9.15 , 
}
# Lista de tarifas base por nivel de servicio de Diamond Ridge Health and Rehab Center
LEVEL_OF_SERVICE_BASE_RATES_DIAMOND_RIDGE_HEALTH_AND_REHAB_CENTER= {
    "WCH": 65,   # Silla de ruedas
    "STR": 80,  # Camilla
    "BLS NE": 272.61,   # Soporte vital básico
    "BLS ER": 436.17, # Soporte vital básico con especialista
    "ALS NE": 327.13,   # Soporte vital avanzado
    "ALS ER": 517.96,   # Soporte vital avanzado con especialista
    "ALS2": 749.67,  # Soporte vital avanzado nivel 2
    "CCT": 885.98,   # Transporte de cuidado critico
    
}
# Incrementos por milla por nivel de servicio de Cedar Creek
LEVEL_OF_SERVICE_INCREMENTS_CRYSTAL_RIVER_HEALTH_AND_REHAB_CENTER = {
    "WCH": 3,
    "STR": 3,
    "BLS NE": 9.15,
    "BLS ER": 9.15, # Soporte vital básico con especialista
    "ALS NE": 9.15 ,
    "ALS ER": 9.15 ,  
    "ALS2": 9.15,  # Soporte vital avanzado nivel 2
    "CCT": 9.15 , 
}
# Lista de tarifas base por nivel de servicio de Sunflower Springs
LEVEL_OF_SERVICE_BASE_RATES_SUNFLOWER_SPRINGS= {
    "WCH": 75,   # Silla de ruedas
    "STR": 150,  # Camilla
    "BLS NE": 272.61,   # Soporte vital básico
    "BLS ER": 436.17, # Soporte vital básico con especialista
    "ALS NE": 327.13,   # Soporte vital avanzado
    "ALS ER": 517.96,   # Soporte vital avanzado con especialista
    "ALS2": 749.67,  # Soporte vital avanzado nivel 2
    "CCT": 885.98,   # Transporte de cuidado critico
    
}
# Incrementos por milla por nivel de servicio de Cedar Creek
LEVEL_OF_SERVICE_INCREMENTS_SUNFLOWER_SPRINGS = {
    "WCH": 2.5,
    "STR": 5,
    "BLS NE": 9.15,
    "BLS ER": 9.15, # Soporte vital básico con especialista
    "ALS NE": 9.15 ,
    "ALS ER": 9.15 ,  
    "ALS2": 9.15,  # Soporte vital avanzado nivel 2
    "CCT": 9.15 , 
}
#
LEVEL_OF_SERVICE_BASE_RATES_SUPERIOR_RESIDENCES_OF_LECANTO= {
    "WCH": 75,   # Silla de ruedas
    "STR": 150,  # Camilla
    "BLS NE": 272.61,   # Soporte vital básico
    "BLS ER": 436.17, # Soporte vital básico con especialista
    "ALS NE": 327.13,   # Soporte vital avanzado
    "ALS ER": 517.96,   # Soporte vital avanzado con especialista
    "ALS2": 749.67,  # Soporte vital avanzado nivel 2
    "CCT": 885.98,   # Transporte de cuidado critico
    
}
# Incrementos por milla por nivel de servicio de Cedar Creek
LEVEL_OF_SERVICE_INCREMENTS_SUPERIOR_RESIDENCES_OF_LECANTO = {
    "WCH": 2.5,
    "STR": 5,
    "BLS NE": 9.15,
    "BLS ER": 9.15, # Soporte vital básico con especialista
    "ALS NE": 9.15 ,
    "ALS ER": 9.15 ,  
    "ALS2": 9.15,  # Soporte vital avanzado nivel 2
    "CCT": 9.15 , 
}
# Lista de tarifas base por nivel de servicio de Tampa General Hospital Crystal River
LEVEL_OF_SERVICE_BASE_RATES_TAMPA_GENERAL_HOSPITAL_CRYSTAL_RIVER= {
    "WCH": 75,   # Silla de ruedas
    "STR": 150,  # Camilla
    "BLS NE": 272.61,   # Soporte vital básico
    "BLS ER": 436.17, # Soporte vital básico con especialista
    "ALS NE": 327.13,   # Soporte vital avanzado
    "ALS ER": 517.96,   # Soporte vital avanzado con especialista
    "ALS2": 749.67,  # Soporte vital avanzado nivel 2
    "CCT": 885.98,   # Transporte de cuidado critico
    
}
# Incrementos por milla por nivel de servicio de Cedar Creek
LEVEL_OF_SERVICE_INCREMENTS_TAMPA_GENERAL_HOSPITAL_CRYSTAL_RIVER = {
    "WCH": 3,
    "STR": 5,
    "BLS NE": 9.15,
    "BLS ER": 9.15, # Soporte vital básico con especialista
    "ALS NE": 9.15 ,
    "ALS ER": 9.15 ,  
    "ALS2": 9.15,  # Soporte vital avanzado nivel 2
    "CCT": 9.15 , 
}
# Lista de tarifas base por nivel de servicio de TGH Crystal River Emergency Center
LEVEL_OF_SERVICE_BASE_RATES_TGH_CRYSTAL_RIVER_EMERGENCY_CENTER= {
    "WCH": 75,   # Silla de ruedas
    "STR": 150,  # Camilla
    "BLS NE": 272.61,   # Soporte vital básico
    "BLS ER": 436.17, # Soporte vital básico con especialista
    "ALS NE": 327.13,   # Soporte vital avanzado
    "ALS ER": 517.96,   # Soporte vital avanzado con especialista
    "ALS2": 749.67,  # Soporte vital avanzado nivel 2
    "CCT": 885.98,   # Transporte de cuidado critico
    
}
# Incrementos por milla por nivel de servicio de Cedar Creek
LEVEL_OF_SERVICE_INCREMENTS_TGH_CRYSTAL_RIVER_EMERGENCY_CENTER = {
    "WCH": 3,
    "STR": 5,
    "BLS NE": 9.15,
    "BLS ER": 9.15, # Soporte vital básico con especialista
    "ALS NE": 9.15 ,
    "ALS ER": 9.15 ,  
    "ALS2": 9.15,  # Soporte vital avanzado nivel 2
    "CCT": 9.15 , 
}
# Lista de tarifas base por nivel de servicio de The Gardens Assisted Living and Memory Care
LEVEL_OF_SERVICE_BASE_RATES_THE_GARDENS_ASSISTED_LIVING_AND_MEMORY_CARE= {
    "WCH": 65,   # Silla de ruedas
    "STR": 80,  # Camilla
    "BLS NE": 272.61,   # Soporte vital básico
    "BLS ER": 436.17, # Soporte vital básico con especialista
    "ALS NE": 327.13,   # Soporte vital avanzado
    "ALS ER": 517.96,   # Soporte vital avanzado con especialista
    "ALS2": 749.67,  # Soporte vital avanzado nivel 2
    "CCT": 885.98,   # Transporte de cuidado critico
    
}
# Incrementos por milla por nivel de servicio de Cedar Creek
LEVEL_OF_SERVICE_INCREMENTS_THE_GARDENS_ASSISTED_LIVING_AND_MEMORY_CARE = {
    "WCH": 3,
    "STR": 3,
    "BLS NE": 9.15,
    "BLS ER": 9.15, # Soporte vital básico con especialista
    "ALS NE": 9.15 ,
    "ALS ER": 9.15 ,  
    "ALS2": 9.15,  # Soporte vital avanzado nivel 2
    "CCT": 9.15 , 
}
# Lista de tarifas base por nivel de servicio de Vitas Inpatient Hospice
LEVEL_OF_SERVICE_BASE_RATES_VITAS_INPATIENT_HOSPICE= {
    "WCH": 75,   # Silla de ruedas
    "STR": 150,  # Camilla
    "BLS NE": 272.61,   # Soporte vital básico
    "BLS ER": 436.17, # Soporte vital básico con especialista
    "ALS NE": 327.13,   # Soporte vital avanzado
    "ALS ER": 517.96,   # Soporte vital avanzado con especialista
    "ALS2": 749.67,  # Soporte vital avanzado nivel 2
    "CCT": 885.98,   # Transporte de cuidado critico
    
}
# Incrementos por milla por nivel de servicio de Cedar Creek
LEVEL_OF_SERVICE_INCREMENTS_VITAS_INPATIENT_HOSPICE = {
    "WCH": 2.5,
    "STR": 5,
    "BLS NE": 9.15,
    "BLS ER": 9.15, # Soporte vital básico con especialista
    "ALS NE": 9.15 ,
    "ALS ER": 9.15 ,  
    "ALS2": 9.15,  # Soporte vital avanzado nivel 2
    "CCT": 9.15 , 
}
"""Aqui termina la seccion de citrus county"""


#Diccionario de proveedores por condado 
COUNTY_PROVIDERS = {
    "Palm Beach": ["Standard", "Baptist", "Jupiter Medical Center", "Tenants (PBHN)"],
    "Broward": [ "Standard"],
    "Monroe": ["Standard"],
    "Citrus": [ "Arbor Trail Rehab and Skilled Nursing Center", "Cedar Creek", 
               "Citrus Health and Rehab Center",  "Clearsky Rehab Hospital of Lecanto", 
               "Crystal River Health and Rehab Center", "Diamond Ridge Health and Rehab Center",
               "Sunflower Springs", "Superior Residences of Lecanto","Tampa General Hospital Crystal River",
               "TGH Crystal River Emergency Center","The Gardens Assisted Living and Memory Care",
               "Vitas Inpatient Hospice"],
}







"""Constantes para la parte de geolocalización y cálculo de rutas
   realmente no se usan demasiados y no son tan importantes pero quizas mada delnate si"""


# Configuración de geolocalización
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
ROAD_DISTANCE_FACTOR = 1.3  # Factor para estimar distancia por carretera


