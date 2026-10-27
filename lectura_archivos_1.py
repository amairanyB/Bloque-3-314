# importar pandas
import pandas as pd

# leer archivo csv cuando lo tenemos en nuestra carpeta
tcandidatosJ_csv = pd.read_csv('candidato_judicial.csv')
print(tcandidatosJ_csv)
print(tcandidatosJ_csv.info())

# ver las filas
# Mostrar todas las columnas
# pd.set_option('display.max_columns', None)

print("\nprimeras 10 filas: ")
print("\n",tcandidatosJ_csv.head(10))

print("\nultimas 10 filas:")
print("\n", tcandidatosJ_csv.tail(10))

print("\nfila 318:")
print("\n", tcandidatosJ_csv.iloc[318])

print("\nfila, 0, 5, 10: ")
print("\n", tcandidatosJ_csv.iloc[[0, 5, 10]])

print("\nrango de las filas de la 10 a la 20:")
print("\n", tcandidatosJ_csv.iloc[10:20])