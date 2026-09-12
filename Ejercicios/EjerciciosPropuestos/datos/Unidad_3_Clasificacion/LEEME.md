# Clasificación supervisada

**Caso: alertas de atraso y ruteo de reclamos.** Un operador necesita priorizar pedidos con riesgo de atraso y asignar sus reclamos al área correcta. Se generan probabilidades, se valida su calidad y se convierten en decisiones bajo capacidad. El primer flujo es binario y semanal; el segundo, multiclase, comparte el contexto de servicio pero utiliza una base propia.

## Instructivo

**Carpeta:** `datos/Unidad_3_Clasificacion/`. El flujo binario contiene `entrenamiento.csv`, 1.200 pedidos de semanas 1–12; `validacion.csv`, 300 de semanas 13–15; y `prueba_final.csv`, 300 de semanas 16–18. Hay 100 pedidos por semana y 13 columnas por archivo. Una fila corresponde a un pedido, con desenlace observado en la misma semana antes del siguiente corte semanal. Si se ampliara el horizonte real, habría que introducir separación por maduración de etiquetas.

**Cortes de desarrollo.** Use semanas 1–6 para ajustar y 7–8 para evaluar; 1–8 frente a 9–10; 1–10 frente a 11–12. Mantenga comunes esos cortes entre familias. Hiperparámetros, imputación, escala, selección, calibración y balanceo deben aprenderse dentro de la porción de entrenamiento, mediante subdivisiones temporales adicionales cuando se necesiten. La validación externa permite elegir la política; la prueba final se abre solo en E50. No se exige reajustar con validación: si se hace, debe congelarse y reproducirse el protocolo completo de calibración antes de abrir prueba.

**Decisiones binarias.** Positivo significa atraso. La compensación real es posterior y se excluye. Use costo fijo hipotético de falso negativo de 120.000 CLP y de falso positivo de 6.000 CLP, aciertos con costo cero, y máximo de 20 alertas semanales. El costo mide errores de clasificación bajo una matriz docente: no demuestra que llamar al cliente evite el atraso. Compare políticas con los mismos casos y reporte capacidad, recall y costo por semana. No llene cupos con beneficio esperado negativo.

**Flujo multiclase.** `reclamos_multiclase.csv` tiene 1.000 filas y 8 columnas; `rol_particion` distingue 700 de entrenamiento, 150 de validación y 150 de prueba. Las señales se observan al abrir el reclamo; su clase se conoce al resolverlo. No use ID ni rol como predictores. Las particiones simulan casos independientes de la misma población, sin pretender evaluación temporal. E50 mantiene su prueba separada de la del flujo binario.

**Entrega y formato.** Incluya probabilidades, matriz, curva PR, calibración con conteos y costo de la política congelada. `diccionario.csv` documenta ambos flujos y `inicio.R` abre solo entrenamiento binario. CSV UTF-8, coma, punto decimal y `NA`; generador con semilla 20260912. Todas las bases son sintéticas y no contienen información personal real.

## Etapas de los desafíos

41. Formular y auditar despachos — consulte el enunciado completo en la guía.
42. Riesgos con logística — consulte el enunciado completo en la guía.
43. Evaluar a umbral fijo — consulte el enunciado completo en la guía.
44. Discriminar y calibrar — consulte el enunciado completo en la guía.
45. Política de alertas — consulte el enunciado completo en la guía.
46. Vecindarios de pedidos — consulte el enunciado completo en la guía.
47. Familias de árboles — consulte el enunciado completo en la guía.
48. Fronteras lineales y no lineales — consulte el enunciado completo en la guía.
49. Auditar robustez y desbalance — consulte el enunciado completo en la guía.
50. Entrega integrada de clasificación — consulte el enunciado completo en la guía.

## Inicio

Abra una terminal o R en esta carpeta y ejecute `inicio.py` o `inicio.R`. Ambos solo cargan la primera base y muestran su estructura; no resuelven los ejercicios. Para reproducir los datos originales, ejecute `generar_datos.py` desde la raíz del paquete. Este comando vuelve a escribir los CSV de datos y diccionarios; conserve sus análisis en una carpeta separada.
