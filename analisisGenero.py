import pandas as pd  # Importa Pandas para trabajar con datos.
import matplotlib.pyplot as plt  # Importa herramientas para crear gráficas.

from conexionBD import conexionBD  # Importa la clase de conexión a la BD.


class analisisGenero:

    def __init__(self, conexion):  # Recibe y guarda la conexión a PostgreSQL.
        self.conexion = conexion

    def obtener_genero(self):  # Consulta la cantidad de candidatos por género.

        # Cuenta los candidatos de cada género.
        consulta = """
            SELECT id_genero, COUNT(*) AS cantidad
            FROM siac.tcandidato_judicial
            WHERE id_genero IN (1, 2)
            GROUP BY id_genero
            ORDER BY id_genero;
        """

        # Ejecuta la consulta y guarda los resultados en un DataFrame.
        df = pd.read_sql(consulta, self.conexion)

        return df  # Devuelve los datos obtenidos.
    # las graficas de pastel sirven para mostrar los resultados en porcentaje
    def mostrar_grafica(self):  # Muestra los resultados en una gráfica circular.

        df = self.obtener_genero()  # Obtiene los datos de la consulta.

        # Asigna un nombre a cada ID de género.
        nombres = {
            1: "mujeres",
            2: "hombres"
        }

        # Agrega una columna con el nombre de cada género.
        df["genero"] = df["id_genero"].map(nombres)

        print(df)  # Muestra la tabla de resultados.

        # Crea la gráfica según la cantidad de candidatos.
        plt.pie(
            df["cantidad"],  # Define el tamaño de cada sección.
            labels=df["genero"],  # Muestra el nombre de cada género.
            autopct="%1.0f%%"  # Muestra los porcentajes. 
        )

        plt.title("Candidaturas por género")  # Agrega el título.
        plt.show()  # Muestra la gráfica.

    
    def mostrar_grafica_colores(self):
        # Obtiene los mismos datos de la consulta.
        df = self.obtener_genero()

        # Cambia los ID por los nombres de los géneros.
        nombres = {
            1: "mujeres",
            2: "hombres"
        }
        df["genero"] = df["id_genero"].map(nombres)

        print(df)

        # Define un color para cada sección.
        colores = ["#DA5296", "#FFC0CB"]

        # Crea la gráfica con los colores elegidos.
        plt.pie(
            df["cantidad"],
            labels=df["genero"],
            autopct="%1.1f%%",
            colors=colores
        )

        plt.title("Candidaturas por género")
        plt.show()
