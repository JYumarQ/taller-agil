# Sistema de Reputación Turística (Clasificador de Sentimientos)

## Descripción
Este proyecto es un script en Python diseñado para procesar reseñas de clientes extraídas de un archivo `.txt`, limpiarlas y clasificarlas mediante un análisis de polaridad simple basado en palabras clave (Positiva, Negativa, Neutral). Además, incluye un sistema de pruebas unitarias automatizadas utilizando `unittest`.

## Estructura de Archivos
* `clasificador_simple.py`: Script principal que contiene la lógica de limpieza, clasificación, ejecución de pruebas unitarias (TDD) y generación de reportes.
* `resenas.txt`: Archivo de texto que actúa como base de datos, conteniendo 20 reseñas de ejemplo.

## Requisitos
* Entorno de ejecución Linux o compatible (o terminal estándar en cualquier OS).
* Python 3.x instalado. No requiere librerías externas ni dependencias adicionales, solo la biblioteca estándar de Python.

## Instrucciones de Ejecución

### 1. Preparación
Asegúrese de que el archivo `resenas.txt` se encuentre exactamente en el mismo directorio que el script `clasificador_simple.py`.

### 2. Ejecutar Pruebas Unitarias y Reporte
El diseño del sistema permite correr el script de forma directa. Primero ejecutará la batería de pruebas y luego procesará el archivo de texto.

Ejecute el siguiente comando en la terminal:
```bash
python3 clasificador_simple.py
