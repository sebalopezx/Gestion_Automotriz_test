# Proyecto: "Gestión Automotriz"
`<link>` : <https://github.com/sebalopezx/Gestion_Automotriz><br>
`<link>` : <https://gestion-automotriz.onrender.com/>

<img src="https://github.com/sebalopezx/Gestion_Automotriz/blob/master/static/images/fondo_login.jpg" alt="Logo del proyecto" width="100" height="100">

> Logo del proyecto

![Static Badge](https://img.shields.io/badge/Creador-Sebasti%C3%A1n%20L%C3%B3pez-orange) ![Static Badge](https://img.shields.io/badge/Versi%C3%B3n-1.0-orange)


**Tabla de Contenido**

+ [Descripción de la aplicación](#Descripción-de-la-aplicación)
	* [Tecnologías usadas](#Tecnologías-usadas)
	* [Aspectos técnicos](#Aspectos-técnicos)
+ [Manejo de la aplicación](#Manejo-de-la-aplicación)
	* [Clientes](#Clientes)
	* [Recepcionista](#Recepcionista)
	* [Administrador](#Administrador)
+ [Instalación de entorno localhost](#Instalación-de-entorno-localhost)

## Descripción de la aplicación

El objetivo principal de este proyecto es implementar un eficiente sistema de reservas para el departamento de mantenimiento de un taller mecánico.
Este sistema permitirá gestionar la programación de citas de mantenimiento, cuentas de usuario, vehículos registrados, y un sistema de puntos para descuentos por servicio.
>Proyecto de estudio

### Tecnologías usadas:

- Django
- Bootstrap 5
- SCSS
- JavaScript
- JSON

### Aspectos técnicos:

| Aspectos  | Caracteristica |
| ------------- | ------------- | 
| Base de datos | `<PostgreSQL>` | 
| Base de datos para pruebas: | `<SQLite3>` | 
| Framework Django | `<Model View Template>` | 
| Diseño | `<Simple y Minimalista>` |
| Arquitectura | `<Modular>` | 



## Manejo de la aplicación
El sistema tiene de tres intefaces de usuario:


### Clientes
El cliente podra gestionar:
- Cuenta de usuario y password
- Agregar vehículos al sistema
- Agendar cita de mantenimiento
- Listar sus citas agendadas
- Listar sus vehículos
- Visualizar estado de vehículo en mantenimiento


![](https://github.com/sebalopezx/Gestion_Automotriz/blob/master/static/images/state_job.PNG)
> Listar vehículos y entrar a ver estado en tiempo real


### Recepcionista
El recepcionista podra gestionar:
- Gestionar de citas diarias (día actual)
- Gestionar todas las citas agendadas
- Gestionar citas finalizadas o canceladas
- Gestionar mecánicos

![](https://github.com/sebalopezx/Gestion_Automotriz/blob/master/static/images/list_jobs.png)
> Listar vehículos con citas agendadas


![](https://github.com/sebalopezx/Gestion_Automotriz/blob/master/static/images/user_mechanic.png)
> Listar mecánicos para su gestión



## Instalación de entorno localhost

Para poder ejecutar el proyecto en un entorno de localhost, se debera:
1. Clonar el repositorio
```
git clone https://github.com/sebalopezx/Gestion_Automotriz
```
2. Abrir en editor de código, ir a modulo de settings dentro del proyecto y cambiar tres estados comentados del proyecto. 
El primero es descomentar DEBUG=True.
```
DEBUG = True
# DEBUG = 'RENDER' not in os.environ
```
El segundo es descomentar la base de datos a Sqlite3.
```
# DATABASES = {
#     'default': dj_database_url.config(
#         # default=os.environ.get('DATABASE_URL')
#         default='postgresql://postgres:postgres@localhost/postgres'
#     )
# }
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
El tercero es descomentar la línea de SESSION = False.
```
# SESSION_COOKIE_SECURE = True  
SESSION_COOKIE_SECURE = False  
```

3. Ejecutar mediante cmd o dentro del terminal de Python el siguiente archivo:
```
ejectute_project.bat
```

> Este archivo contiene los **pip** para instalar todas las dependencias y requerimientos del proyecto creando todo dentro de un entorno virtual **'venv'** de Python.

4. En caso que no quede activo el entorno **'venv'**, se debe activar desde la carpeta raiz del proyecto en el temrinal:
```
.\venv\Scripts\activate
```
>(venv)  = Demuestra el entorno ativo

5. Ejecutar el comando de Django en el terminal:
```
python manage.py runserver
```
