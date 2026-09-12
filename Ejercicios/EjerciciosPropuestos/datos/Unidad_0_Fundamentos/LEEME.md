# Fundamentos estadísticos

**Caso: rediseño de preparación de pedidos.** Un operador logístico compara tres procedimientos mediante 360 lotes de ensayo independientes. Cada lote tiene una medición de referencia y una posterior; se asigna al azar uno de tres métodos a 120 lotes. El objetivo combina tiempo, cumplimiento y planificación de recursos. Los desafíos E41–E50 construyen un único informe; conserve sus resultados entre etapas.

## Instructivo

**Carpeta:** `datos/Unidad_0_Fundamentos/`. El archivo `lotes_piloto.csv` contiene 360 filas y 12 columnas. `diccionario.csv` documenta cada campo y `inicio.R` carga la base sin resolver los ejercicios.

**Secuencia.** E41 audita; E42–E43 estudian probabilidades y muestreo; E44–E47 estiman y contrastan; E48 explora asociación; E49 prepara un modelo; E50 integra y abre su prueba. En E49 use semilla 20260909 y separe por lotes, conservando un lote en una sola partición. Ningún resultado de E50 se usa para volver a seleccionar el modelo.

**Diseño y disponibilidad.** Los centros y turnos describen condiciones del piloto; la independencia asumida corresponde a lotes de ensayo, no a lecturas de sensores. El tratamiento es `metodo`. La referencia `tiempo_antes_min` fue medida antes de aplicar el método. Para pronósticos operacionales explique si se dispondrá de esa referencia. `tiempo_despues_min`, `incumple_sla` y `costo_final_clp` se conocen al cerrar el proceso: no son predictores disponibles al recibir un pedido. La alarma se registra previamente; su relación con el incumplimiento es sintética.

**Criterios de decisión.** La mejora mínima de interés es 2 minutos de reducción media. El incumplimiento se define como tiempo posterior superior a 32 minutos. El piloto no representa automáticamente una muestra aleatoria de todas las plantas del país. Declare cuándo una conclusión se apoya en aleatorización y cuándo en un modelo o en supuestos de transporte.

**Formato de datos.** CSV UTF-8, separador coma, punto decimal y `NA` para faltantes. Todos los datos son sintéticos y reproducibles con `generar_datos.py`. No se requiere el libro Excel citado en la versión anterior. El generador documenta el caso, pero sus ecuaciones no deben utilizarse como respuestas a la inferencia solicitada.

## Etapas de los desafíos

41. Auditar el piloto — consulte el enunciado completo en la guía.
42. Valor informativo de la alarma — consulte el enunciado completo en la guía.
43. Distribución de una media — consulte el enunciado completo en la guía.
44. Estimar una mejora — consulte el enunciado completo en la guía.
45. Una decisión preespecificada — consulte el enunciado completo en la guía.
46. Comparar los procedimientos — consulte el enunciado completo en la guía.
47. Incumplimiento por método — consulte el enunciado completo en la guía.
48. Asociación entre carga y tiempo — consulte el enunciado completo en la guía.
49. Explicar y predecir tiempos — consulte el enunciado completo en la guía.
50. Informe integrado y prueba final — consulte el enunciado completo en la guía.

## Inicio

Abra una terminal o R en esta carpeta y ejecute `inicio.py` o `inicio.R`. Ambos solo cargan la primera base y muestran su estructura; no resuelven los ejercicios. Para reproducir los datos originales, ejecute `generar_datos.py` desde la raíz del paquete. Este comando vuelve a escribir los CSV de datos y diccionarios; conserve sus análisis en una carpeta separada.
