# Importar pandas
import pandas as pd

# Importar la clase para la conexión a la base de datos
from conexionBD import conexionBD


class escrituraArchivos:

    # Método para establecer la conexión
    def __init__(self):
        self.bd = conexionBD()
        self.conexion = self.bd.conexion

    # Método para guardar la tabla tdistrito_judicial
    def guardar_distritos(self):

        # Consulta para obtener los registros de la tabla
        consulta = """
        SELECT * FROM siac.tdistrito_judicial
        """

        # Ejecutar la consulta y guardar los resultados en un DataFrame
        df = pd.read_sql(consulta, self.conexion)

        # Guardar el DataFrame en un archivo CSV
        df.to_csv("tdistrito_judicial.csv", index=False)

        # Guardar el DataFrame en un archivo Excel
        df.to_excel("tdistrito_judicial.xlsx", index=False)


# Crear un objeto de la clase
archivos = escrituraArchivos()

# Ejecutar el método para guardar los archivos
archivos.guardar_distritos()
