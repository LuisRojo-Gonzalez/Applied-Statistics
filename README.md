<div align="center">

# 📊 Estadística Aplicada

**Modelamiento predictivo y análisis de datos para la toma de decisiones en Ingeniería Industrial**

Material docente del curso *Estadística Aplicada* — Departamento de Ingeniería Industrial, Universidad de Santiago de Chile (USACH).

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![R](https://img.shields.io/badge/Hecho%20con-R-276DC3.svg?logo=r)](https://www.r-project.org/)
[![Python](https://img.shields.io/badge/Datos-Python-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Universidad](https://img.shields.io/badge/USACH-Ingenier%C3%ADa%20Industrial-004b8d.svg)](https://www.usach.cl/)
![Estado](https://img.shields.io/badge/Estado-Activo-brightgreen.svg)

</div>

---

## 📌 Descripción

Este repositorio reúne el material del curso **Estadística Aplicada** para estudiantes de Ingeniería Industrial. El curso desarrolla razonamiento bajo incertidumbre, inferencia estadística y modelamiento predictivo, con énfasis en la interpretación de evidencia empírica y la comunicación de resultados aplicados a problemas industriales.

> **Objetivo general.** Comprender y aplicar herramientas de estadística aplicada, modelamiento predictivo y análisis de datos para estimar, contrastar e interpretar evidencia empírica en problemas de Ingeniería Industrial.

El trabajo práctico se realiza principalmente en **R**, y los conjuntos de datos de los ejercicios son **sintéticos y completamente reproducibles** mediante los generadores incluidos.

---

## 🗂️ Temario

| # | Unidad | Contenidos principales |
|---|--------|------------------------|
| 1 | **Bienvenida al curso** | Propósito, mapa del curso, evaluación y herramientas |
| 2 | **Fundamentos estadísticos** | Decisión, población, incertidumbre, probabilidad, muestreo, estimación e inferencia |
| 3 | **Regularización, validación cruzada y modelos flexibles** | OLS, ridge, lasso, elastic-net, splines / GAM, validación cruzada |
| 4 | **Ensemble Learning** | Árboles, Random Forest, boosting (XGBoost), combinación de modelos |
| 5 | **Clasificación supervisada** | Modelos de clasificación, métricas y evaluación |
| 6 | **Clasificación no supervisada** | Clustering y reducción de dimensionalidad |
| 7 | **Cierre del curso** | Integración y síntesis |
| 8 | **Anexos** | Material complementario |

Las diapositivas completas del curso están en [`Slides.pdf`](Slides.pdf).

---

## 📁 Estructura del repositorio

```
Applied-Statistics/
│
├── Slides.pdf                         # Diapositivas completas del curso
│
├── Programa/                          # Programa oficial y syllabus
│   ├── Programa_AnalisisEstadistico.pdf
│   ├── Syllabus.pdf
│   ├── Programas/                     # Programas de referencia de la carrera
│   └── Propuesta/                     # Propuesta y apuntes de rediseño del curso
│
├── Ejercicios/
│   ├── EjerciciosClase/               # Ejercicios trabajados en clases (PDF por unidad)
│   │   ├── 0_Fundamentos.pdf
│   │   ├── 1_Regularizacion.pdf
│   │   ├── 2_Ensemble.pdf
│   │   ├── 3_ClasificacionSupervisada.pdf
│   │   └── 4_ClasificacionNoSupervisada.pdf
│   │
│   └── EjerciciosPropuestos/
│       ├── Enunciados/                # Enunciados por unidad
│       ├── Soluciones/                # Soluciones de referencia
│       ├── datos/                     # Datasets sintéticos + diccionarios por unidad
│       │   ├── manifest.json          # Semilla y checksums (SHA-256) de cada CSV
│       │   ├── Unidad_0_Fundamentos/
│       │   ├── Unidad_1_Regularizacion/
│       │   ├── Unidad_2_Ensamble/
│       │   ├── Unidad_3_Clasificacion/
│       │   └── Unidad_4_Clustering/
│       └── generar_datos.py           # Reproduce todos los CSV de forma determinista
│
├── CaseStudy/                         # Proyectos integradores por equipos
│   ├── 1_Regression/                  # Caso 1 (común): predicción de respuesta continua
│   ├── 2_SupervisedLearning/          # Caso 2 (variante A): clasificación supervisada
│   └── 2_UnsupervisedLearning/        # Caso 2 (variante B): clasificación no supervisada
│
├── Pruebas/                           # Evaluaciones
│   ├── Teoricas/
│   └── Practicas/
│
└── Bibliografia/                      # Referencias del curso
```

Cada carpeta de `CaseStudy/` incluye el **enunciado**, la **guía de informe**, la **guía de presentación**, la **rúbrica**, la **pauta de evaluación** y las **plantillas** de informe (LaTeX) y presentación (PPT).

---

## 🧪 Conjuntos de datos

Los datos de los ejercicios propuestos son **sintéticos** y se distribuyen por unidad en `Ejercicios/EjerciciosPropuestos/datos/`. Cada unidad contiene:

- Los archivos `.csv` del caso (entrenamiento, validación, prueba final, etc.).
- Un `diccionario.csv` que documenta cada variable.
- Scripts `inicio.R` e `inicio.py` que solo **cargan y auditan** la base (no resuelven los ejercicios).
- Un `LEEME.md` con el contexto del caso y el instructivo.

Formato: **CSV UTF-8**, separador coma, punto decimal y `NA` para faltantes.

### Reproducibilidad

Todos los datasets se generan de forma determinista con una **semilla fija (`20260909`)**. El archivo [`manifest.json`](Ejercicios/EjerciciosPropuestos/datos/manifest.json) registra, para cada archivo, el número de filas, columnas y su checksum **SHA-256**, de modo que cualquier persona puede verificar la integridad de los datos.

```bash
# Regenerar todos los CSV desde cero
cd Ejercicios/EjerciciosPropuestos
python3 generar_datos.py
```

> ⚠️ `generar_datos.py` **reescribe** los CSV de datos y diccionarios. Guarde sus análisis en una carpeta separada.

---

## 🚀 Guía de uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/LuisRojo-Gonzalez/Applied-Statistics.git
cd Applied-Statistics
```

### 2. Requisitos

- **R** (≥ 4.0) para el trabajo estadístico y de modelamiento.
- **Python 3** (opcional) para regenerar los datasets sintéticos.

### 3. Empezar un ejercicio

Abra R (o Python) en la carpeta de la unidad correspondiente y ejecute el script de inicio, que carga y describe la base:

```r
# Desde Ejercicios/EjerciciosPropuestos/datos/Unidad_1_Regularizacion/
source("inicio.R")
```

```bash
# Equivalente en Python
python3 inicio.py
```

Consulte el `LEEME.md` de la unidad y el enunciado en `Enunciados/` antes de comenzar.

---

## 🎓 Proyectos integradores (Casos de estudio)

El curso contempla **dos casos de estudio** que integran las unidades:

- **Caso 1 — Regresión** *(común a todos los equipos)*: definir y resolver, de extremo a extremo, un problema de predicción de una respuesta continua en Ingeniería Industrial, integrando fundamentos, regularización y ensembles con un flujo reproducible.
- **Caso 2 — Clasificación** *(variante asignada aleatoriamente por equipo)*: **supervisada** (respuesta categórica) o **no supervisada** (clustering / segmentación).

Cada caso entrega enunciado, guías, rúbrica, pauta y plantillas de informe y presentación.

---

## 📚 Bibliografía

- *The Elements of Statistical Learning* — Hastie, Tibshirani & Friedman.
- *Statistical Inference* — Casella & Berger.
- *Applied Multivariate Statistical Analysis*.
- *Time Series Analysis and Its Applications* — Shumway & Stoffer.

> Los textos completos no se distribuyen en este repositorio por razones de derechos de autor.

---

## 📈 Registro de notas

El registro de calificaciones **no se publica en este repositorio**. Los estudiantes del curso pueden consultarlo en una planilla de Google Drive con acceso restringido:

🔗 **[Registro de notas (solo alumnos del curso)](AGREGAR_ENLACE_DE_GOOGLE_DRIVE)**

---

## 📝 Licencia

Este material se distribuye bajo la licencia **[Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)**.

Usted es libre de compartir y adaptar el material para fines no comerciales, dando el crédito correspondiente y distribuyendo sus contribuciones bajo la misma licencia.

---

## 👤 Autor

**Luis Rojo-González, Ph.D.**
Departamento de Ingeniería Industrial · Universidad de Santiago de Chile

---

<div align="center">
<sub>Material docente · Estadística Aplicada · USACH</sub>
</div>
