import matplotlib.pyplot as plt
import numpy as np
import dataframes as df

# 7- Gráfico plot con la población y cpi del país más rico de izquierda (matriz de correlación).
# 8- Gráfico plot con la población y cpi del país más rico de derecha (matriz de correlación).
def plot_last5_years():
    # Datos proporcionados
    years = df.rigth_world_gdp_data_last5_year.describe().loc['mean'].index
    data_left = list(df.left_world_gdp_data_last5_year.describe().loc['mean'].values)
    data_right = list(df.rigth_world_gdp_data_last5_year.describe().loc['mean'].values)

    fig, ax = plt.subplots()

    # Graficar datos izquierdos
    ax.plot(years, data_left, label='Izquierda')
    ax.set_xticks(years)

    # Graficar datos derechos
    ax.plot(years, data_right, label='Derecha')
    ax.set_xticks(years)

    # Configuraciones adicionales
    ax.set_title('Promedio de GDP por países de izquierda y derecha')
    ax.set_xlabel('Años')
    ax.set_ylabel('Valores')
    ax.legend()

    plt.show()


if __name__ == "__main__":
    plot_last5_years()