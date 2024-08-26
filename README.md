# LOCATELTechnicalTest - Sales Administrative System

## Descripción

Este proyecto es un sistema administrativo básico de ventas diseñado para gestionar productos de aseo personal para clientes registrados. El sistema está orientado a proporcionar una solución confiable, ágil y segura para registrar y gestionar datos relacionados con las ventas.

## Tecnologías Utilizadas

- **Frontend**: Vue 2
- **Backend**: Python con Flask
- **Base de Datos**: SQLite
- **Otras Dependencias**: (Lista de librerías o frameworks adicionales, si los hay)

## Funcionalidades

El sistema administrativo de ventas incluye las siguientes funcionalidades clave:

### 1. Gestión de Clientes

- **Crear un Cliente**: Permite registrar los datos de un cliente en el sistema.
  - Campos:
    - Cédula
    - Nombre
    - Dirección
    - Teléfono
    - Email

### 2. Gestión de Productos

- **Crear Producto**: Permite registrar un nuevo producto de aseo personal en el sistema.
  - Campos:
    - Código
    - Nombre
    - Valor de Venta
    - ¿Maneja IVA?
    - % de IVA si Maneja

### 3. Gestión de Ventas

- **Registrar Cabecera Venta**: Permite registrar la información general de una venta.
  - Campos:
    - Consecutivo de la Venta
    - Fecha
    - Cliente
    - Total Venta

- **Registrar Detalle Venta**: Permite registrar los detalles específicos de los productos vendidos en cada venta.
  - Campos:
    - Producto
    - Valor Producto
    - IVA Calculado

### 4. Reportes

- **Listado de Ventas Realizadas por Fecha**: Permite generar un listado de todas las ventas realizadas filtradas por fecha, facilitando el análisis de ventas.

## Instalación y Ejecución

Para obtener instrucciones detalladas sobre la instalación y ejecución de cada componente, consulta los README específicos de cada uno:

- **Backend**: [Instrucciones del Backend](./backend/README.md)
- **Frontend**: [Instrucciones del Frontend](./frontend/README.md)

## Estructura del Proyecto

- `backend/`: Contiene el código del servidor Flask.
- `frontend/`: Contiene el código de la aplicación Vue 2.
- `README.md`: Este archivo.

## Licencia

Este proyecto está licenciado bajo la [MIT License](https://github.com/SantiYami/LOCATELTechnicalTest?tab=MIT-1-ov-file).
