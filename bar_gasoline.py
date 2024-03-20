import matplotlib.pyplot as plt
import dataframes as df

# 5- Gráfico de barra horizontal del precio de la gasolina (5 paises de derecha). 
# 6- Gráfico de barra horizontal del precio de la gasolina (5 paises de izquierda). 
def bar_gasoline():
    df_right_countries_gasoline = df.df_right_countries["Gasoline Price"].sort_values()
    right_countries_names = df_right_countries_gasoline.index
    right_countries_values = df_right_countries_gasoline.values

    df_left_countries_gasoline = df.df_left_countries["Gasoline Price"].sort_values()
    left_countries_names = df_left_countries_gasoline.index
    left_countries_values = df_left_countries_gasoline.values

    plt.figure(figsize=(15,7))

    # Países de derecha
    plt.subplot(121)
    plt.title('Precio de gasolina en países de derecha')
    plt.barh(right_countries_names, right_countries_values)
    plt.xlabel('Precio por galón', fontsize=12, color='black')
    plt.ylabel('Países', fontsize=12, color='black')

    # Países de izquierda
    plt.subplot(122)
    plt.title('Precio de gasolina en países de izquierda')
    plt.barh(left_countries_names, left_countries_values)
    plt.xlabel('Precio por galón', fontsize=12, color='black')
    plt.ylabel('Países', fontsize=12, color='black')

    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
    plt.show()


if __name__ == "__main__":
    bar_gasoline()