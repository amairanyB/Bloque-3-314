import pandas as pd
import matplotlib.pyplot as plt

from conexionBD import conexionBD # importa la conexión a la BD

class analisisGeneroBarras:

    def __init__(self, conexion): # Recibe y guarda la conexión a la BD
        self.conexion = conexion

    def obtener_genero(self): # consultar la cantidad de candidatos por género
        # la consulta sql, cuenta cúantos canddatos hay para cada genero, agrupa y ordena:
        consulta = """
            SELECT id_genero, COUNT(*) AS cantidad
            FROM siac.tcandidato_judicial
            WHERE id_genero IN (1, 2)
            GROUP BY id_genero 
            ORDER BY id_genero;
        """

        # ejecutar la consulta y guardar los resultados en df
        df = pd.read_sql(consulta, self.conexion)
        return df

    def mostrar_grafica_barras(self):
        df = self.obtener_genero() # para obtener los datos de la consulta

        # asignar un nombre a cada ID de género
        nombres = {
            1: "mujeres",
            2: "hombres"
        }

        # agrega una columna con el nombre para cada genero a nusetra consulta
        df["genero"] = df["id_genero"].map(nombres)
        
        print(df)  # Muestra la tabla de resultados.

        # Crear EL gráfico de barras
        
        # Datos para las barras.
        categorias = df["genero"] # la columna que da nombre a los id´s de genero
        cantidades = df["cantidad"] # cantidad es la columna creada en la sentencia sql para saber la cantidad de candidatos

        # Elegir un color para cada barra.
        colores = ["#0B2409", "#C1981E"]

        # Crear la figura y los ejes.
        fig, ax = plt.subplots(figsize=(8, 5)) # es el tamaño del área donde se crea el gráfico, ancho por largo
        # fig es lienzo para el grafico
        # ax es el espacio para los ejes, nuestra variable para la figura

        # Dibujar las barras.
        barras = ax.bar( # funcion para craer barras
            categorias,
            cantidades,
            color=colores,
            width=0.6, # ANCHO DE LAS BARRAS,UNO MAYOR LAs HACE MÁS ANCHAS  
            edgecolor="pink", # blue, red, white, black
            linewidth=1.5 # contorno
        )

        # Agregar el valor encima de cada barra, la funcion recibe barras
        ax.bar_label(barras, fontsize=11) 

        # Personalizar el título y los ejes.
        ax.set_title("Candidaturas por género", fontsize=16) 
        ax.set_xlabel("Género", fontsize=12)
        ax.set_ylabel("Cantidad de candidatos", fontsize=12)

        # Personalizar el fondo y la cuadrícula.
        ax.set_facecolor("#FFF8FC")
        ax.grid(axis="y", linestyle="--", alpha=0.3) # hace las lineas de la cuadricula: -, --, :, none
        ax.set_axisbelow(True)

        # Ajustar el diseño y mostrar la gráfica.
        fig.tight_layout()
        plt.show()
