# Proyecto de Tabla de Datos Financieros

Este proyecto consiste en una aplicación web que permite visualizar y analizar datos financieros. Utiliza Angular para el frontend y Flask para el backend.

## Requisitos

- Node.js y npm
- Angular CLI
- Python 3.x
- pip

## Instalación

### Frontend (Angular)

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd tu_repositorio
    ```
3. Instala las dependencias de Angular:
    ```bash
    npm install
    ```
4. Inicia el servidor de desarrollo de Angular:
    ```bash
    ng serve
    ```

### Backend (Flask)

1. Navega al directorio del backend:
    ```bash
    cd backend
    ```
2. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    ```
3. Activa el entorno virtual:
    - En Windows:
      ```bash
      venv\Scripts\activate
      ```
    - En macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
4. Instala las dependencias de Flask:
    ```bash
    pip install -r requirements.txt
    ```
5. Inicia el servidor Flask:
    ```bash
    python backend.py
    ```

## Uso

1. Asegúrate de que ambos servidores (Angular y Flask) estén en funcionamiento.
2. Abre tu navegador y navega a `http://localhost:4200` para ver la aplicación en acción.

## Funcionalidades

- Visualización de datos financieros en una tabla.
- Estadísticas financieras calculadas y mostradas en una tabla separada.
- Carga de datos financieros desde el servidor Flask.

## Estructura del Proyecto

### Frontend (Angular)

