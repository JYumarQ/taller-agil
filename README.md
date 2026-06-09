# Sistema de Reputación Turística

Proyecto integrador desarrollado para procesar y clasificar reseñas hoteleras, evaluado bajo los marcos de Scrum, Kanban y Extreme Programming (XP).

## Equipo y Roles de Scrum
*   **Product Owner:** Elier (Priorización de Backlog)
*   **Scrum Master:** Juan Yumar (Gestión de Impedimentos)
*   **Developer:** Yaimir (Ejecución Técnica)

## Marcos de Trabajo Aplicados
*   **Scrum:** Gestión del Sprint Backlog y cumplimiento de ceremonias.
*   **Kanban:** Gestión visual del flujo de trabajo en Taiga con límites estrictos de WIP=2 en las columnas de desarrollo activo[cite: 6].
*   **XP (Extreme Programming):** Desarrollo guiado por pruebas (TDD) con cobertura de pruebas unitarias antes del código y sesiones de Pair Programming[cite: 6].

## Requisitos del Sistema
*   Python 3.x instalado[cite: 6].
*   El archivo de origen `resenas.txt` debe estar en la misma carpeta que el script[cite: 6].

## Instrucciones de Ejecución

### Ejecutar Clasificador y Pruebas Unitarias
El script ejecutará automáticamente la suite de pruebas unitarias (`unittest`) antes de procesar el archivo masivo de reseñas[cite: 6]. Ejecute el comando:

```bash
python3 clasificador_simple.py
