"""Carga de datos; no contiene soluciones. Se puede ejecutar desde cualquier carpeta."""
from pathlib import Path
import pandas as pd

carpeta = Path(__file__).resolve().parent
datos = pd.read_csv(carpeta / "desarrollo.csv", na_values="NA")
diccionario = pd.read_csv(carpeta / "diccionario.csv")
print(datos.shape)
print(datos.dtypes)
print(datos.isna().sum())
# Consulte los ejercicios 41–50 antes de abrir las particiones reservadas.
