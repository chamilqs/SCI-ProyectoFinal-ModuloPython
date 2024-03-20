import dataframes as df
import matplotlib.pyplot as plt
import numpy as np

# Gráfico de araña 5 de derecha unemployment rate (corruption_index OPTIONAL)
def spider_umployee_right():
    unemployment_rates = df.df_right_countries['Unemployment rate']

    # Crear un gráfico de radar
    labels=np.array(df.df_right_countries.index)
    stats=unemployment_rates.values

    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    stats = np.concatenate((stats,[stats[0]]))
    angles = np.concatenate((angles,[angles[0]]))

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.fill(angles, stats, color='orange', alpha=0.25)
    ax.plot(angles, stats, color='orange', linewidth=2)

    # Añadir etiquetas
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=12)
    ax.set_title("Rango de desempleo entre los países de derecha", fontsize=14)

    plt.show()

if __name__ == "__main__":
    spider_umployee_right()