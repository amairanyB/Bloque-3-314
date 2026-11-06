# importar pandas
import pandas as pd

# importar la clase para la conexion con la BD
from conexionBD import conexionBD

class escritura_archivos_1:
    # metodo para establecer la conexion
    def __init__(self):
        self.bd = conexionBD()
        self.conexion = self.bd.conexion

    # método para guardar la tabla tdistrito_judicial
    def guardar_distritos(self):
        # consulta para obtener la tabla
        consulta = """
        SELECT * FROM siac.tdistrito_judicial
        """

        # ejecutar consulta y obtener los registros
        df = pd.read_sql(consulta, self.conexion)

        # ejecutar el dataframe en un archivo CSV
        df.to_csv("tdistrito_judicial.csv", index = False)

        # guardar el dataframe en un archivo excel
        df.to_excel("tdistrito_judicial.xlsx", index = False)

#crear objeto de la clase
archivos = escritura_archivos_1()
# ejecutar el método para guardar los archivos
archivos.guardar_distritos()