import numpy
import pandas as pnd
import matplotlib.pyplot as plt
import dataframes as df
from bar_gasoline import bar_gasoline
from bar_ten_countries import bar_ten_countries
from plot_last5_years import plot_last5_years
from spider_unemployee_right import spider_umployee_right
from spider_unemployee_left import spider_umployee_left


# 1- Gráfico de barra top 5 de los paises más ricos (dataframe aparte).
df_richest_countries = df.richest_countries.head(5)

# 2- Gráfico de araña 5 de izquierda unemployment rate (corruption_index OPTIONAL).
# 3- Gráfico de araña 5 de derecha unemployment rate (corruption_index OPTIONAL).
spider_umployee_right()
spider_umployee_left()

# 4- Gráfico de barra agrupado de 10 países (CPI, GDP, ANUAL_INCOME).
bar_ten_countries()

# 5- Gráfico de barra horizontal del precio de la gasolina (5 paises de derecha). 
# 6- Gráfico de barra horizontal del precio de la gasolina (5 paises de izquierda). 
bar_gasoline()

# 7- Gráfico scatter con la población y cpi del país más rico de izquierda (matriz de correlación).
# 8- Gráfico scatter con la población y cpi del país más rico de derecha (matriz de correlación).
plot_last5_years()

