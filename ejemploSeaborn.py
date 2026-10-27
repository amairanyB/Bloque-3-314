# librerias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV con pandas
propinas = pd.read_csv('tip.csv')

# Imprimir el DataFrame completo en la consola
print(propinas.to_string())

# Crear una figura con un solo gráfico, ya sin espacios para otros graficos con matplotlib
fig, axes = plt.subplots(figsize=(6, 5)) # figsize establece su tamaño

# Crear el gráfico de barras de la columna sex con seaborn
sns.countplot(
    data=propinas, 
    x='sex', 
    order=['Female', 'Male'], 
    ax=axes 
)

# Agregar etiquetas y título
axes.set_xlabel("Sex")
axes.set_ylabel("Frecuencia")
axes.set_title("Gráfico de barras de la columna Sex")

# Mostrar el gráfico
plt.tight_layout()
plt.show()