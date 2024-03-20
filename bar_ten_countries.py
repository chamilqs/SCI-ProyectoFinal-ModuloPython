import matplotlib.pyplot as plt
import numpy as np
import dataframes as df


# 4- Gráfico de barra agrupado de 10 países (CPI, GDP) 
def bar_ten_countries():
    df_countries = df.df_countries.sort_index()

    countries = df_countries.index
    countries_cpi_gdp = {
        'CPI': df_countries['CPI Change'].values,
        'GDP': df_countries['GDP'].values,
    }

    x = np.arange(len(countries))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in countries_cpi_gdp.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Índices')
    ax.set_title('10 Países (CPI, GDP)')
    ax.set_xticks(x + width, countries)
    ax.legend(loc='upper left', ncols=2)
    ax.set_ylim(10)

    plt.show()

if __name__ == "__main__":
    bar_ten_countries()