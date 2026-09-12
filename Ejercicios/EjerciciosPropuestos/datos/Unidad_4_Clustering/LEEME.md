# Clasificación no supervisada

**Caso: segmentación de una cartera industrial.** Un distribuidor desea organizar servicio y visitas comerciales usando comportamiento de clientes. La base mezcla escalas, categorías, faltantes, densidades y observaciones extremas. Se comparan familias de clustering y se estudia si sus segmentos son estables y útiles seis meses después. No se proporcionan etiquetas de ``grupo verdadero''.

## Instructivo

**Carpeta:** `datos/Unidad_4_Clustering/`. `clientes_enero.csv` contiene 720 clientes y 10 columnas con resúmenes de los seis meses anteriores al corte de enero. `clientes_julio.csv` tiene 720 clientes y las mismas columnas, con historia al corte de julio. Comparten 660 identificadores: hay 60 clientes de enero ausentes en julio y 60 nuevos. `resultados_semestre.csv` contiene 720 filas y 3 columnas con abandono y margen del semestre posterior a enero para los clientes de la base original.

**Representación.** E41–E49 usan únicamente enero. La representación A incluye las seis variables numéricas de comportamiento; B puede incorporar además canal, contrato y región mediante Gower. ID no define semejanza. Documente imputación, escala, transformaciones de asimetría y pesos. No descarte automáticamente tickets altos: podrían representar clientes relevantes. Compare métricas internas entre algoritmos solo cuando comparten población y representación o disimilitud apropiada. Reporte claramente la cobertura cuando se excluye ruido.

**Estabilidad.** En E49 reajuste también la representación en cada submuestra para evaluar el procedimiento completo y compare etiquetas sobre IDs comunes. Puede agregar un análisis secundario con representación fija para aislar variación del algoritmo. Los nombres de grupos no están identificados: use emparejamiento para Jaccard y perfiles; ARI ya es invariante a permutaciones. Una etiqueta que cambia de número no es fragmentación.

**Asignación futura.** Para K-means use centroides congelados; para PAM, medoides; para GMM, responsabilidades. Una partición jerárquica o de densidad requiere una regla adicional explícita: por ejemplo, asignación al representante dentro de un radio validado, con abstención fuera de soporte, o un método de predicción propio de la implementación. Esa regla es una extensión operacional, no el mismo acto de reagrupar toda la base. Reagrupar julio puede ser un análisis secundario, distinguiéndolo de migración con modelo congelado.

**Uso externo.** E50 une resultados por ID a los grupos de enero; no usa abandono ni margen futuro como entrada, ni para reoptimizar $K$ antes de declarar validación. Reporte asociaciones e incertidumbre y evite convertirlas en efectos causales. Un piloto comercial debe definir intervención, control y costos, aunque no se ejecute en esta guía.

**Archivos auxiliares.** CSV UTF-8, coma, punto decimal y `NA`; `diccionario.csv` registra disponibilidad y `inicio.R` abre enero. El generador usa semilla 20260913. Los patrones son sintéticos; recuperar la estructura interna del generador no es el objetivo ni una prueba de que existan segmentos naturales en datos reales.

## Etapas de los desafíos

41. Auditar clientes y tendencia — consulte el enunciado completo en la guía.
42. Dos representaciones explícitas — consulte el enunciado completo en la guía.
43. K-means con múltiples inicios — consulte el enunciado completo en la guía.
44. Segmentos representados por clientes — consulte el enunciado completo en la guía.
45. Jerarquía de segmentos — consulte el enunciado completo en la guía.
46. Segmentación por densidad — consulte el enunciado completo en la guía.
47. Densidad variable — consulte el enunciado completo en la guía.
48. Segmentos probabilísticos — consulte el enunciado completo en la guía.
49. Elegir con estabilidad — consulte el enunciado completo en la guía.
50. Segmentos en operación — consulte el enunciado completo en la guía.

## Inicio

Abra una terminal o R en esta carpeta y ejecute `inicio.py` o `inicio.R`. Ambos solo cargan la primera base y muestran su estructura; no resuelven los ejercicios. Para reproducir los datos originales, ejecute `generar_datos.py` desde la raíz del paquete. Este comando vuelve a escribir los CSV de datos y diccionarios; conserve sus análisis en una carpeta separada.
