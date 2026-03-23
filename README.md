# 📊 Procesador de Empleados en Python

Proyecto desarrollado en Python para el procesamiento eficiente de datos desde archivos CSV, utilizando **generadores (`yield`)**, **pipelines de datos** y únicamente la **librería estándar de Python**.

---

## 🚀 Objetivo

Construir un sistema modular capaz de:

* Leer archivos CSV de gran tamaño
* Filtrar datos de forma eficiente
* Procesar información mediante pipelines
* Generar reportes agregados
* Guardar resultados en archivos

---

## 🧠 Conceptos aplicados

Este proyecto está enfocado en buenas prácticas y fundamentos sólidos de Python:

* Generadores (`yield`)
* Manejo de archivos (file handling)
* Programación funcional (filtros, pipelines)
* `dataclasses` para modelado de datos
* `argparse` para CLI (línea de comandos)
* `logging` para trazabilidad
* Estructura modular de proyecto
* Procesamiento eficiente (sin cargar todo en memoria)

---

## 📁 Estructura del proyecto

```
proyecto_empleados/
│
├── main.py
├── config.py
├── data/
├── output/
├── logs/
│   └── app.log
│
├── src/
│   ├── reader.py
│   ├── filters.py
│   ├── pipeline.py
│   └── report.py
│
└── tests/
    └── test_pipeline.py
```

---

## 📄 Formato del archivo CSV

Ejemplo:

```
nombre,rol,salario,activo
Ana,IT,2000,True
Luis,ventas,1200,False
Carlos,IT,1800,True
```

---

## ⚙️ Instalación

No requiere librerías externas.

Solo necesitas Python 3.8+.

```bash
git clone <tu-repositorio>
cd proyecto_empleados
```

---

## ▶️ Uso

Ejecutar desde consola:

```bash
python main.py --input data/empleados_test_v2.csv --min_salario 2000 --solo_activos
```

---

## 🔧 Argumentos disponibles

| Argumento        | Descripción                     |
| ---------------- | ------------------------------- |
| `--input`        | Ruta del archivo CSV de entrada |
| `--output`       | Ruta del archivo de salida      |
| `--min_salario`  | Salario mínimo para filtrar     |
| `--solo_activos` | Filtra solo empleados activos   |

---

## 📊 Ejemplo de salida

Archivo generado:

```
Rol: IT
Cantidad: 2
Promedio Salario: 1900.00

Rol: ventas
Cantidad: 1
Promedio Salario: 1600.00
```

---

## 📝 Logging

El sistema genera logs en:

```
logs/app.log
```

Ejemplo:

```
2026-03-23 10:00:00 - INFO - Inicio del proceso
2026-03-23 10:00:01 - INFO - Proceso finalizado correctamente
```

---

## 🧪 Testing

Puedes ejecutar tests básicos para validar la lógica:

```bash
python -m pytest
```

*(Opcional si decides usar pytest)*

---

## 💡 Características destacadas

* Procesamiento eficiente con generadores
* Bajo consumo de memoria
* Código modular y escalable
* Separación cl
