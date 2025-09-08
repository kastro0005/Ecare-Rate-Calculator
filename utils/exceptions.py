class LocationError(Exception):
    """Error personalizado para problemas de geolocalización"""
    pass

class ValidationError(Exception):
    """Error personalizado para validaciones de entrada"""
    pass

class RateCalculationError(Exception):
    """Error personalizado para problemas en el cálculo de tarifas"""
    pass