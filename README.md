# Sistema de Gestión y Análisis de Datos (DataManager CLI)

CLI en Python para **cargar datos desde CSV**, **filtrar/ordenar**, **calcular estadísticas** y **exportar resultados a JSON**.  
Proyecto organizado en módulos e incluye suite de tests.

---

## Estructura del proyecto

datamanager/
│
├── main.py
├── data_loader.py
├── processor.py
├── exporter.py
├── utils.py
│
├── tests/
│ ├── test_utils.py
│ ├── test_processor.py
│ └── test_exporter.py
│
├── data/
│ └── datos_censo_pp.csv
│
└── outputs/
└── resultados_censo.json


- `data_loader.py`: carga datos desde CSV y retorna lista de diccionarios.
- `processor.py`: filtros, ordenamiento y estadísticas.
- `exporter.py`: exportación a JSON.
- `utils.py`: funciones auxiliares (validación/normalización).
- `main.py`: menú CLI .

---
