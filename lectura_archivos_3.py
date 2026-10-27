# usamos pandas
import pandas as pd

# leer archivos ubicados en otra carpeta
# leer el csv
dtoMunJudicial_csv = pd.read_csv(
    r'C:\Users\Usuario\Documents\tdto_mun_sec_judicial.csv'
)
print(dtoMunJudicial_csv)

# leer el xlsx
dtoMunJud_xlxs = pd.read_excel(
    r'C:\Users\Usuario\Documents\tdto_mun_sec_judicial.xlsx'
)
print(dtoMunJud_xlxs)
