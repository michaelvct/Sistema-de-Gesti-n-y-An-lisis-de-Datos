# DataManager CLI

Integrantes:
*Cochachin Polich, Victor
*Gavino, Jorge
* Claudia, Vivas

Proyecto en Python que implementa una herramienta de línea de comandos (CLI) para **cargar**, **procesar**, **analizar** y **exportar resultados** a partir de un archivo CSV.

Incluye:
- Código organizado en **módulos**.
- **CLI interactivo** (menú).
- **Suite de tests** con `pytest`.
- **Exportación a JSON**.
- **Ejemplo documentado** de ejecución.

---

## 📁 Estructura del proyecto

```text
datamanager/
│
├── main.py
├── data_loader.py
├── processor.py
├── exporter.py
├── utils.py
│
├── tests/
│   ├── test_processor.py
│
└── data/
    └── estudiantes.csv
```

---

## ✅ Requisitos

- macOS / Linux / Windows  
- **Python 3.10+** (recomendado)  
- `pytest` para correr tests

Verifica tu versión:

```bash
python3 --version
```

---

## ⚙️ Instalación y entorno virtual (macOS)

Desde Terminal, ubícate en la carpeta `datamanager/` (donde está `main.py`):

```bash
cd /ruta/a/datamanager
```

Crea y activa un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Actualiza `pip` e instala dependencias:

```bash
python -m pip install --upgrade pip
python -m pip install pytest
```

> Nota: Si ya tienes el entorno creado, solo ejecuta `source .venv/bin/activate`.

---

## ▶️ Ejecución del programa (CLI)

Ejecuta el CLI:

```bash
python main.py
```

Verás un menú similar a:

- 1 - Cargar datos  
- 2 - Filtrar  
- 3 - Ordenar  
- 4 - Mostrar estadísticas  
- 5 - Exportar estadísticas (JSON)  
- 6 - Salir  

### 📌 Cargar el CSV

Cuando selecciones `1 - Cargar datos`, ingresa la ruta:

```text
data/estudiantes.csv
```

---

## 🧪 Ejecutar tests

Desde la carpeta `datamanager/` y con el entorno activo `(.venv)`:

```bash
pytest -q
```

Si todo está correcto, verás algo como:

```text
3 passed in 0.00s
```

> Si tuviste problemas de imports en pytest, una forma robusta es:
```bash
python -m pytest -q
```

---

## 📤 Exportación a JSON

El programa permite exportar resultados (por ejemplo estadísticas) a un archivo JSON.

Pasos típicos:
1. Cargar datos (opción 1)
2. Mostrar estadísticas (opción 4)
3. Exportar (opción 5)
4. Escribir un nombre de salida (ejemplo):

```text
output_stats.json
```

El archivo generado quedará en la carpeta donde ejecutes el programa (o en la ruta que indiques).

---

## 🧾 Ejemplo documentado de ejecución

A continuación un ejemplo típico (inputs del usuario y resultados esperados):

1) Ejecutar el programa:
```bash
python main.py
```

2) Seleccionar `1 - Cargar datos`  
Ruta ingresada:
```text
data/estudiantes.csv
```

Salida esperada (ejemplo):
```text
✅ Cargados N estudiantes válidos.
⚠️ Se descartaron M filas inválidas (si aplica).
📌 Mostrando 15 de N estudiantes:
- ...
```

3) Seleccionar `4 - Mostrar estadísticas`  
Salida esperada (ejemplo):
```text
📊 Estadísticas:
- total_estudiantes: N
- promedio_general: ...
- edad_min: ...
- edad_max: ...
- conteo_por_carrera: {...}
```

4) Seleccionar `5 - Exportar estadísticas (JSON)`  
Ruta ingresada:
```text
output_stats.json
```

Salida esperada:
```text
✅ Exportado a: output_stats.json
```
