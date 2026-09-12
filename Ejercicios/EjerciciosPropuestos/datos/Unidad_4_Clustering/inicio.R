# Abra R en esta carpeta. Este archivo solo carga y audita; no resuelve los desafios.
set.seed(20260913)
datos <- read.csv("clientes_enero.csv", na.strings="NA", fileEncoding="UTF-8", stringsAsFactors=FALSE)
diccionario <- read.csv("diccionario.csv", fileEncoding="UTF-8")
str(datos)
colSums(is.na(datos))
stopifnot(nrow(datos)>0)
# Consulte los ejercicios 41--50 y el instructivo de la guia antes de abrir prueba final.
