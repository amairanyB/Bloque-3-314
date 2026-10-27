# instalar primero pip install openpyxl
# usamos pandas
import pandas as pd

# leer archivo excel cuando esta en nuetra carpeta
tcandidatosJ_xlsx = pd.read_excel("candidato_judicial.xlsx")
print(tcandidatosJ_xlsx)
print(tcandidatosJ_xlsx.info())

# ver las filas
# Mostrar todas las columnas
# pd.set_option('display.max_columns', None)

print("\nprimeras 10 filas: ")
print("\n",tcandidatosJ_xlsx.head(10))

print("\nultimas 10 filas:")
print("\n", tcandidatosJ_xlsx.tail(10))

print("\nfila 318:")
print("\n", tcandidatosJ_xlsx.iloc[318])

print("\nfila, 0, 5, 10: ")
print("\n", tcandidatosJ_xlsx.iloc[[0, 5, 10]])

print("\nrango de las filas de la 10 a la 20:")
print("\n", tcandidatosJ_xlsx.iloc[10:20])