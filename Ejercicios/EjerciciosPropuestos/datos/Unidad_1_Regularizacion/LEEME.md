# Regularización, validación cruzada y modelos flexibles

**Caso: planificación de horas-persona en centros de distribución.** Se dispone de registros diarios de ocho centros, con carga redundante, faltantes y relaciones potencialmente no lineales. Se quiere planificar recursos al inicio del turno y estudiar transporte a un noveno centro. E41–E50 comparten el mismo protocolo y culminan en una decisión entre modelos.

## Instructivo

**Carpeta:** `datos/Unidad_1_Regularizacion/`. Archivos: `entrenamiento.csv`, 960 filas (120 fechas por 8 centros); `validacion.csv`, 240 filas (30 fechas); `prueba_final.csv`, 240 filas (30 fechas); `centro_nuevo.csv`, 30 filas del centro C9 en julio. Cada archivo contiene 21 columnas. La unidad es un centro en una fecha con un turno observado; no son lecturas repetidas dentro de la misma fila.

**Protocolo obligatorio del caso.** Entrenamiento ocupa los primeros 120 días de 2026; validación, los siguientes 30, y prueba, los últimos 30 del período de 180 días. E42 define los cortes temporales dentro de entrenamiento. E44–E49 usan esos mismos cortes para ajustar hiperparámetros y la validación externa para comparar candidatos ya especificados. En E50 se congela la decisión y se puede reajustar en entrenamiento más validación antes de abrir las dos pruebas. El centro nuevo evalúa otro dominio, no aporta datos para elegir el ganador.

**Variables y datos disponibles.** Los pedidos y recursos son información planificada al inicio; las horas-persona efectivas se conocen al finalizar. El costo de cierre es posterior y se excluye. Fecha sirve para particionar y crear calendario conocido; registro y rol de partición no son predictores. Los proxies son mediciones redundantes, mientras que las variables de ruido permiten examinar selección espuria. Establezca tratamiento de niveles nuevos de centro sin aprenderlo de la prueba.

**Entregables específicos.** Conserve índices de los cortes, receta de transformación y tabla común de RMSE/MAE por corte, por familia y por centro. Use la misma respuesta y observaciones evaluables al comparar familias. Si una familia requiere retirar filas, vuelva a evaluar los demás modelos sobre la misma población y reporte la pérdida de cobertura. Registre la convención de penalización del software para que los valores de $\lambda$ sean interpretables.

**Lectura.** CSV UTF-8 con coma, punto decimal y `NA`. `diccionario.csv` detalla variables y faltantes por archivo; `inicio.R` carga entrenamiento. El paquete incluye `generar_datos.py`, semilla 20260910. Los datos son simulados; sus ecuaciones de generación no sustituyen validación ni constituyen una solución que deba recuperarse exactamente.

## Etapas de los desafíos

41. Definir la planificación — consulte el enunciado completo en la guía.
42. Protocolo común en el tiempo — consulte el enunciado completo en la guía.
43. Construir la receta reproducible — consulte el enunciado completo en la guía.
44. Ajustar Ridge — consulte el enunciado completo en la guía.
45. Selección y estabilidad con Lasso — consulte el enunciado completo en la guía.
46. Grupos correlacionados — consulte el enunciado completo en la guía.
47. Detectar no linealidad — consulte el enunciado completo en la guía.
48. Curvas de saturación — consulte el enunciado completo en la guía.
49. Modelo aditivo de recursos — consulte el enunciado completo en la guía.
50. Selección congelada y prueba — consulte el enunciado completo en la guía.

## Inicio

Abra una terminal o R en esta carpeta y ejecute `inicio.py` o `inicio.R`. Ambos solo cargan la primera base y muestran su estructura; no resuelven los ejercicios. Para reproducir los datos originales, ejecute `generar_datos.py` desde la raíz del paquete. Este comando vuelve a escribir los CSV de datos y diccionarios; conserve sus análisis en una carpeta separada.
