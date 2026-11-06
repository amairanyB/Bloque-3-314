import pandas as pd

# podemos crear nuestros archvos con un diccionario

# diccionario
data = { 
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 24, 33],
    'Country': ['USA', 'Sweden', 'Germany']
    }
# guardarlo
df = pd.DataFrame(data)

# escribir el dataframe df en archvos csv y xlsx
df.to_csv('data.csv', index = False)
df.to_excel('data.xlsx')
