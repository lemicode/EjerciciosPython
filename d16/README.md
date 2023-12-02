# Creación de entornos virtuales para Python

1. pip install virtualenv
2. (Opcional) Validar paquetes de Python instaldos --> pip freeze
3. Creación de un entorno:
   Opción 1: virtualenv my_env
   Opción 2: python3 -m venv my_env
4. Activar entorno
    Opción 1: ./venv/Scripts/activate
    Opción 2 (MacOS): source venv/bin/activate
5. Desactivar --> deactivate


# Instalar django

> pip install django

# Estructura de directorio inicial sugerido

- web/ (nombre general cualquiera)
  - src/ (nombre sugerido)
    - nombre_proyecto/
      - nombre_app1/
        - migrations/
        - templates/
        - ...
      - nombre_app2/
      - ...
      - nombre_proyecto/ (Lo remite automáticamente el generador de Python al crear el proyecto)
      - db.sqlite3
      - manage.py
  - venv/ (Nombre cualquiera del entorno virtual para el proyecto en particular) 

# Crear proyecto django

> django-admin startproject proyecto

# Iniciar proyecto

Dentro de la carpeta del proyecto ejecutar --> python3 manage.py runserver

# Correr migraciones

> python3 manage.py migrate

# Crear súper usuario 

> python3 manage.py createsuperuser

# Crear aplicación

> python3 manage.py startapp nombre_app

# Crear archivos de migración a partir de los modelos

> python3 manage.py makemigrations

# Archivo manage.py

Es como el CLI de django

# Archivo admin.py de la app

En este archivo se registran los modelos para que sean incluidos en el panel del admin

# Archivo settings.py del proyecto

Uso:

- Registro de las nuevas apps
- Registro de la carpeta templates
- Se configura ***LOGIN_URL = 'url_del_login'*** para que se redireccione al sitio establecido cuando se ingrese a una 
url restringuida
- Se modifica el idioma por defecto
