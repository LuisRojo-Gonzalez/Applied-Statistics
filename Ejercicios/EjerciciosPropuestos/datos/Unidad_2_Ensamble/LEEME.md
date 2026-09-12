# Aprendizaje por ensamble

**Caso: anticipar espera al ingresar a un terminal logístico.** La empresa dispone de ventanas operacionales independientes, con congestión, recursos y documentación conocidos al arribo. Quiere estimar minutos de espera para coordinar muelles. El caso compara árboles, bagging, Random Forest, boosting y combinaciones; importancia y gráficos parciales apoyan la interpretación del modelo seleccionado.

## Instructivo

**Carpeta:** `datos/Unidad_2_Ensamble/`.

`desarrollo.csv` contiene 900 ventanas y `prueba_final.csv`, 300; ambos tienen 12 columnas. Son ventanas sintéticas independientes de condiciones comparables, no una serie horaria ni múltiples filas del mismo camión. Esta premisa permite el esquema de pliegues aleatorios; si se reutilizara con datos dependientes habría que rediseñarlo.

**Particiones.** Cree cinco pliegues externos comunes con semilla 20260911. Para una estimación honesta después de ajustar hiperparámetros, use tres pliegues internos dentro de cada porción externa de entrenamiento. El escalado o imputación, cuando se utilicen, también se aprende dentro del ajuste. Mantenga los identificadores de los pliegues para comparar errores por las mismas ventanas. OOB sirve para diagnóstico y ajuste dentro de desarrollo, sin reemplazar la prueba final.

**Secuencia y complejidad.** E41–E45 establecen las familias; E46 las compara; E47–E48 auditan interpretación; E49–E50 combinan y deciden. Las matrices OOF destinadas a pesos o meta-modelos deben generarse de nuevo dentro del entrenamiento de cada pliegue externo. No basta que las bases excluyan la fila si su etiqueta ya intervino en elegir sus hiperparámetros o en entrenar el meta-modelo que la evalúa.

**Datos disponibles.** Al arribo se conocen cola, muelles, peso, dotación, revisión documental y prioridad. El tiempo real y el costo por espera se conocen después. `codigo_aleatorio` es un identificador numérico sin significado operativo; puede incorporarse solo en la auditoría de E47 y debe marcarse como tal. `cola_proxy` contiene información redundante y exige cautela en importancia y PDP.

**Prueba y entrega.** Abra prueba únicamente en E50, tras seleccionar todo el sistema, y compare con el baseline calculado en desarrollo. Informe minutos de error y costo computacional medido en el mismo equipo, sin prometer causalidad a partir de cortes o importancias. Se entregan `diccionario.csv`, `inicio.R` y generador reproducible con semilla 20260911; CSV UTF-8, coma y punto decimal.

## Etapas de los desafíos

41. Un árbol para tiempos de espera — consulte el enunciado completo en la guía.
42. Bagging y estabilidad — consulte el enunciado completo en la guía.
43. Diversidad de un bosque — consulte el enunciado completo en la guía.
44. Contrastar OOB con validación — consulte el enunciado completo en la guía.
45. Boosting de espera — consulte el enunciado completo en la guía.
46. Comparación defendible — consulte el enunciado completo en la guía.
47. Auditar la importancia — consulte el enunciado completo en la guía.
48. Explicar patrones del modelo — consulte el enunciado completo en la guía.
49. Combinar familias — consulte el enunciado completo en la guía.
50. Decisión final del sistema — consulte el enunciado completo en la guía.

## Inicio

Abra una terminal o R en esta carpeta y ejecute `inicio.py` o `inicio.R`. Ambos solo cargan la primera base y muestran su estructura; no resuelven los ejercicios. Para reproducir los datos originales, ejecute `generar_datos.py` desde la raíz del paquete. Este comando vuelve a escribir los CSV de datos y diccionarios; conserve sus análisis en una carpeta separada.
