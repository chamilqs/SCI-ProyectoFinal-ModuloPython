import dataframes as df
import matplotlib.pyplot as plt
import pandas as pnd

# Datos
data_right = {
    'Country': list(df.df_right_countries.index),
    'Population': [int(population.replace(',', '')) for population in df.df_right_countries['Population']],
    'Annual Income': list(df.df_right_countries['annual_income'])
}

data_left = {
    'Country': list(df.df_right_countries.index),
    'Population': [int(population.replace(',', '')) for population in df.df_left_countries['Population']],
    'Annual Income': list(df.df_left_countries['annual_income'])
}

# Convertir a DataFrame
df_derecha = pnd.DataFrame(data_right)
df_izquierda = pnd.DataFrame(data_left)

# Gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(df_derecha['Population'], df_derecha['Annual Income'], color='blue', label='Países de derecha')
plt.scatter(df_izquierda['Population'], df_izquierda['Annual Income'], color='red', label='Países de izquierda')

# Línea diagonal
plt.plot([0, 3e8], [0, 80000], color='green', linestyle='--', label='Línea diagonal')

# Etiquetas y leyenda
plt.xlabel('Población')
plt.ylabel('Ingreso Anual')
plt.title('Comparación de Población e Ingreso Anual')
plt.legend()

# Mostrar gráfico
plt.grid(True)
plt.tight_layout()
plt.show()
