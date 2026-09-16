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

## 🧮 Evaluación y aprobación del curso

Las ponderaciones y fechas de esta sección corresponden a [`Slides.pdf`](Slides.pdf), unidad **Bienvenida al curso**, diapositivas 6 a 10. Todas las evaluaciones tienen **60% de exigencia**.

### Nota de presentación de cátedra

| Evaluación | Ponderación en la presentación | Contenido |
|---|---:|---|
| Control 1 ($C_1$) | 5% | Diagnóstico |
| Control 2 ($C_2$) | 10% | Fundamentos estadísticos |
| Control 3 ($C_3$) | 10% | Regularización y Ensemble Learning |
| Control 4 ($C_4$) | 15% | Clasificación supervisada y no supervisada |
| Caso de estudio 1 ($CE_1$) | 35% | Aplicación e integración de contenidos: regresión |
| Caso de estudio 2 ($CE_2$) | 25% | Aplicación e integración de contenidos: clasificación |
| **Total** | **100%** | |

$$
N_{PC}=0.05C_1+0.10C_2+0.10C_3+0.15C_4+0.35CE_1+0.25CE_2.
$$

### Examen ponderado de cátedra

- **Eximición:** quienes obtengan $N_{PC}\geq 5.0$ se eximen y su nota definitiva de cátedra es $N_C=N_{PC}$.
- **Al rendir el examen:** la presentación pondera **70%** y el examen ($N_E$), **30%** de la nota definitiva de cátedra:

$$
N_C=0.70N_{PC}+0.30N_E.
$$

### Nota de laboratorio

| Componente | Ponderación en laboratorio |
|---|---:|
| Actividades de DataCamp ($N_D$) | 30% |
| Código del caso de estudio 1 ($N_{\mathrm{Cod}1}$) | 35% |
| Código del caso de estudio 2 ($N_{\mathrm{Cod}2}$) | 35% |
| **Total** | **100%** |

$$
N_L=0.30N_D+0.35N_{\mathrm{Cod}1}+0.35N_{\mathrm{Cod}2}.
$$

El laboratorio **no tiene evaluación final**. El examen ponderado forma parte exclusivamente de la cátedra.

### Aprobación y nota final

Se deben aprobar **ambos componentes por separado**:

$$
N_C\geq 4.0 \qquad \text{y} \qquad N_L\geq 4.0.
$$

Si ambos están aprobados, la nota final combina **60% de cátedra** y **40% de laboratorio**:

$$
N_F=0.60N_C+0.40N_L.
$$

---

## 🗓️ Calendario del curso · Segundo semestre de 2026

El curso se desarrolla entre el **21 de septiembre de 2026** y el **11 de enero de 2027**. Las fechas de la tabla indican el **lunes de inicio de cada semana**. Se conserva la nomenclatura de bloques de las diapositivas: **L1–L2** (lunes) y **M3** (martes).

### Planificación semanal

| Semana | Inicio | Clases y actividades | Evaluación | Laboratorio |
|---:|---|---|---|---|
| 1 | 21/09/2026 | Bienvenida al curso (L1); Fundamentos estadísticos I (L2–M3) | — | — |
| 2 | 28/09/2026 | Fundamentos estadísticos II (L2–M3) | **Control 1 · 5%** (L1) | — |
| 3 | 05/10/2026 | Fundamentos estadísticos III (L1–L2) | — | Presencial (M3) |
| 4 | 12/10/2026 | Feriado (L1–L2); libre (M3) | — | — |
| 5 | 19/10/2026 | Regularización I (L2) | **Control 2 · 10%** (L1) | Presencial (M3) |
| 6 | 26/10/2026 | Regularización II (L1); Ensemble Learning (L2–M3) | — | — |
| 7 | 02/11/2026 | Clasificación supervisada I (L2) | **Control 3 · 10%** (L1) | Presencial (M3) |
| 8 | 09/11/2026 | Libre | Entrega del caso 1: **11/11/2026, 11:59 a. m.** | — |
| 9 | 16/11/2026 | Presentaciones del caso de estudio 1 | **Caso 1 · 35%** (L1–L2–M3) | — |
| 10 | 23/11/2026 | Clasificación supervisada II (L1–L2) | — | — |
| 11 | 30/11/2026 | Clasificación supervisada III (L1–L2) | — | — |
| 12 | 07/12/2026 | Receso (L1–L2); feriado (M3) | — | — |
| 13 | 14/12/2026 | Clasificación no supervisada I (L1–L2) | Inicio y sorteo del caso 2: **15/12/2026** (M3) | Presencial (M3) |
| 14 | 21/12/2026 | Clasificación no supervisada II (L1–L2) | — | Presencial (M3) |
| 15 | 28/12/2026 | Evaluación de clasificación | **Control 4 · 15%** (L1–L2); entrega del caso 2: **30/12/2026, 11:59 a. m.** | Online (M3) |
| 16 | 04/01/2027 | Presentaciones del caso de estudio 2 | **Caso 2 · 25%** (L1–L2–M3) | — |
| 17 | 11/01/2027 | Examen ponderado de cátedra | **Examen · 30% de la nota definitiva de cátedra** (L1–L2) | — |

Los porcentajes de controles y casos corresponden a la **nota de presentación de cátedra**. El porcentaje del examen corresponde a la **nota definitiva de cátedra**, según las fórmulas anteriores. El símbolo «—» indica que la planificación no especifica una actividad en esa columna.

### Fechas de los casos de estudio

| Caso | Inicio (M3) | Entrega, hasta las **11:59 a. m.** | Presentación (L1–L2–M3) |
|---|---|---|---|
| **1 · Regresión** | 06/10/2026 | 11/11/2026 | 16/11/2026 |
| **2 · Clasificación supervisada o no supervisada** | 15/12/2026 | 30/12/2026 | 04/01/2027 |

- El enfoque del **caso 2** se asignará por **sorteo el 15/12/2026**, al inicio del bloque **M3**.
- Las entregas se realizarán mediante el **formulario de Google** que se comunicará oportunamente.
- Los envíos por otro medio se considerarán **no entregados** y se evaluarán con la **nota mínima (1.0)**.

> **Nota sobre la fecha del caso 2:** se utiliza el **04/01/2027**, indicado en la planificación semanal de la diapositiva 6. La tabla de la diapositiva 8 contiene una errata en el año («04/01/26»).

### Actividades de DataCamp

Las siguientes actividades forman el componente $N_D$, equivalente al **30% de la nota de laboratorio**. «U» identifica las unidades de cada curso de DataCamp.

<details>
<summary><strong>Ver actividades, dedicación y fechas de entrega</strong></summary>

| Inicio | Actividad | Unidades / alcance | Horas | Entrega |
|---|---|---|---:|---|
| 21/09/2026 | Exploratory Data Analysis in R | Curso completo | 4 | 28/09/2026 |
| 21/09/2026 | Machine Learning with caret in R | U4 · Preprocessing Data | 1 | 28/09/2026 |
| 28/09/2026 | Statistical Inference in R | Curso completo | 16 | 19/10/2026 |
| 19/10/2026 | Machine Learning with caret in R | U1 · Regression Models: Fitting and Evaluating Their Performance | 1 | 26/10/2026 |
| 19/10/2026 | Nonlinear Modeling with Generalized Additive Models (GAMs) in R | U1 + U2 · Introduction to Generalized Additive Models; Interpreting and Visualizing GAMs | 2 | 26/10/2026 |
| 19/10/2026 | Supervised Learning in R: Regression | U4 · Dealing with Non-Linear Responses | 1 | 26/10/2026 |
| 26/10/2026 | Machine Learning with Tree-Based Models in R | U2 · Regression Trees and Cross-Validation | 1 | 02/11/2026 |
| 16/11/2026 | Machine Learning with caret in R | U2 · Classification Models: Fitting and Evaluating Their Performance | 1 | 23/11/2026 |
| 16/11/2026 | Supervised Learning in R: Classification | Curso completo | 4 | 23/11/2026 |
| 23/11/2026 | Support Vector Machines in R | Curso completo | 4 | 30/11/2026 |
| 14/12/2026 | Cluster Analysis in R | U1 + U3 · Calculating Distance Between Observations; K-means Clustering | 2 | 21/12/2026 |
| 14/12/2026 | Mixture Models in R | U1 + U2 + U3 · Introduction to Mixture Models; Structure of Mixture Models and Parameters Estimation; Mixture of Gaussians with flexmix | 3 | 21/12/2026 |
| 21/12/2026 | Cluster Analysis in R | U2 · Hierarchical Clustering | 1 | 28/12/2026 |

</details>

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


