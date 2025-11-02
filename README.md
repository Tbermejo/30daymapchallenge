# 30daymapchallenge
# Mapa interactivo PM10 - Streamlit


Repositorio con una aplicación Streamlit para visualizar la evolución anual del promedio de PM10 por estaciones en Colombia usando Plotly. La base de datos de calidad de aire la cual recopila el Instituto de Hidrología, Meteorología y Estudios Ambientales – IDEAM, en el marco de la Operación Estadísticas de Monitoreo y Seguimiento de la Calidad del Aire. Este consolidado considera los promedios anuales de contaminantes atmosféricos y de parámetros meteorológicos determinados a partir de los Sistemas de Monitoreo de Calidad del Aire.


## Estructura del repositorio


- `30daymapchallengeapp.py` : app Streamlit principal
- `PM10.csv` : archivo CSV con los datos
- `requirements.txt` : dependencias de Python


## Cómo ejecutar localmente


1. Clona el repositorio o descarga los archivos.
2. Crea y activa un entorno virtual (recomendado):
```bash
python -m venv .venv
source .venv/bin/activate # macOS / Linux
.\.venv\Scripts\activate # Windows PowerShell
