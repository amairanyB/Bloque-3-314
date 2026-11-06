# pandas
import pandas as pd

# leer archvo csv cuando lo tenemos en nuestra carpeta
candidatosJ = pd.read_csv('candidato_judicial.csv')
print(candidatosJ)

# funcion .info() nos permite ver la informacion del archivo csv
print(candidatosJ.info())





