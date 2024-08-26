# Backend con FLASK API RESTFUL

Para la configuración del entorno de desarrollo y la ejecución de la API del backend, sigue los comandos detallados en este archivo.

## Comandos Principales

### 1. Crear y Activar Entorno Virtual

Crear:

```bash
python -m venv .venv
```

Activar:

- Windows: `.venv/Scripts/activate`
- Linux/Mac: `source .venv/bin/activate`

Desactivar:

```bash
deactivate
```

#### Configuración Adicional para Windows

En sistemas Windows, es posible que necesites permitir la ejecución de scripts de PowerShell para activar el entorno virtual u otros comandos de configuración. Para hacerlo, abre una ventana de PowerShell con permisos de administrador y ejecuta:

```bash
Set-ExecutionPolicy Unrestricted -Scope Process
```

Esta política de ejecución se aplicará solo al proceso actual de PowerShell. Esto significa que la política se revertirá a su valor anterior cuando se cierre la sesión de PowerShell.

### 2. Instalación de Dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar Variables de Entorno para Flask

Asignar variable de aplicación:

- Windows PowerShell: `$env:FLASK_APP = "manage.py"`
- Windows CMD: `set FLASK_APP=manage.py`
- Linux/Mac: `export FLASK_APP=manage.py`

Activar modo DEBUG:

- Windows PowerShell: `$env:FLASK_DEBUG = "1"`
- Windows CMD: `set FLASK_DEBUG=1`
- Linux/Mac: `export FLASK_DEBUG=1`

### 4. Ejecutar Pruebas

```bash
flask test
```

### 5. Iniciar la Aplicación

```bash
flask run
```

## Acceso a la Aplicación

Una vez que la aplicación esté en funcionamiento, puedes acceder a la documentación Swagger en: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Autenticación con Postman

Para usar la API con Postman, asegúrate de incluir el encabezado de autorización:

- `Key: Authorization`
- `Valor: <token generado durante el inicio de sesión>`
