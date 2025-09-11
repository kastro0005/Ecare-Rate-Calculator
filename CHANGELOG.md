# Changelog

Todos los cambios notables de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Sin Lanzar]

### Agregado
- Preparación completa para producción
- Documentación completa del proyecto
- Archivo .gitignore optimizado
- Configuración de variables de entorno
- Licencia MIT

## [1.0.2] - 2025-01-09

### Agregado
- Soporte para múltiples proveedores (Baptist, HCA, Standard)
- Cálculo de tarifas dinámico basado en distancia y nivel de servicio
- Servicios adicionales:
  - Oxígeno (O2) con cálculo por litros
  - Servicios fuera de horario (After Hours)
  - Transporte de ida y vuelta (Deadheads)
  - Servicios de cuidado especial (STC)
  - Transporte bariátrico
  - Tiempo de espera
- Niveles de servicio completos:
  - WCH (Wheelchair - Silla de ruedas)
  - STR (Stretcher - Camilla)
  - BLS (Basic Life Support - Soporte vital básico)
  - ALS (Advanced Life Support - Soporte vital avanzado)
  - CCT (Critical Care Transport - Transporte de cuidado crítico)
- Interfaz gráfica moderna con Flet
- Integración con servicios de geolocalización
- Autocompletado de direcciones
- Cálculo automático de distancias
- Sistema de logging configurable
- Manejo de excepciones personalizado

### Mejorado
- Optimización del rendimiento de la aplicación
- Mejoras en la experiencia de usuario
- Estructura modular del código
- Configuración de tarifas centralizada

### Corregido
- Bugs en el cálculo de tarifas
- Problemas de importación de módulos
- Manejo de errores en servicios de geolocalización

### Técnico
- Implementación de arquitectura modular
- Separación de responsabilidades en servicios
- Configuración de PyInstaller para ejecutables
- Scripts de construcción automatizados
- Manejo de rutas para desarrollo y producción

## [1.0.1] - 2025-01-05

### Agregado
- Implementación inicial de múltiples proveedores
- Sistema básico de cálculo de tarifas
- Interfaz de usuario básica

### Corregido
- Problemas iniciales de configuración
- Errores en la lógica de cálculo

## [1.0.0] - 2025-01-01

### Agregado
- Lanzamiento inicial del proyecto
- Funcionalidad básica de cálculo de tarifas
- Interfaz de usuario con Flet
- Estructura básica del proyecto
- Configuración inicial de dependencias

---

## Tipos de Cambios

- `Agregado` para nuevas funcionalidades
- `Cambiado` para cambios en funcionalidades existentes
- `Obsoleto` para funcionalidades que serán removidas pronto
- `Removido` para funcionalidades removidas
- `Corregido` para corrección de bugs
- `Seguridad` para vulnerabilidades de seguridad
- `Técnico` para cambios técnicos internos

## Notas de Versión

### v1.0.2
Esta versión incluye mejoras significativas en la funcionalidad y preparación completa para producción. Se recomienda actualizar desde versiones anteriores.

### Próximas Funcionalidades Planeadas
- [ ] Exportación de reportes en PDF
- [ ] Integración con sistemas de facturación
- [ ] Historial de cálculos
- [ ] Configuración de tarifas personalizadas
- [ ] Soporte para múltiples idiomas
- [ ] API REST para integración externa
- [ ] Base de datos para almacenamiento persistente
- [ ] Autenticación de usuarios
- [ ] Reportes y analytics
- [ ] Notificaciones push