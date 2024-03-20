import numpy
import pandas as pnd
import matplotlib.pyplot as plt
 
# region CORRUPTION
corruption = pnd.read_csv('./data_source/corruption.csv')
corruption.set_index('country', inplace = True)
 
# Drop Nan records  
corruption.dropna(axis=0, inplace=True)
corruption.drop_duplicates(inplace=True)
 
# Test dataframe
def test_corruption():
    print('\nCORRUPTION')
    print(corruption)
# endregion
 
# region RICHEST_COUNTRIES
richest_countries = pnd.read_csv('./data_source/richest_countries.csv')
richest_countries.set_index('country', inplace = True)
 
# Drop Nan records  
richest_countries.dropna(axis=0, inplace=True)
richest_countries.drop_duplicates(inplace=True)
 
# Test dataframe
def test_richest_countries():
    print('\nRICHEST_COUNTRIES')
    print(richest_countries)
# endregion
 
# region WORLD DATA
world_data = pnd.read_csv('./data_source/world_data_2023.csv')
world_data.set_index('Country', inplace = True)
 
# Select the necessary columns
columns = ['CPI', 'CPI Change', 'Population', 'Gasoline Price', 'Unemployment rate']
world_data = world_data[columns]
 
# Drop Nan records  
world_data.dropna(axis=0, inplace=True)
world_data.drop_duplicates(inplace=True)
 
# Test dataframe
def test_world_data():
    print('\nWORLD DATA')
    print(world_data)
# endregion
 
# region WORLD GDP DATA
world_gdp_data = pnd.read_csv('./data_source/world_gdp_data.csv', encoding='latin1')
world_gdp_data.rename(columns={'country_name': 'country'}, inplace=True)
world_gdp_data.set_index('country', inplace = True)
 
# Select the necessary columns
world_gdp_data.rename(columns={'2023': 'GDP'}, inplace=True)
world_gdp_data = world_gdp_data['GDP']
 
# Drop Nan records  
world_gdp_data.dropna(axis=0, inplace=True)
# world_gdp_data.drop_duplicates(inplace=True)
 
# Test dataframe
def test_world_gdp_data():
    print('\nWORLD GDP DATA')
    print(world_gdp_data)
# endregion

# region Final dataframe 
# Concat cost_of_living, corruption, world_gpd_data, world_data
inflation_data = pnd.concat([corruption, world_gdp_data, world_data], axis=1, join='inner')
 
# Test dataframe
def test_inflation_data():
    print('\nINFLATION DATA')
    print(inflation_data.shape)
# endregion
    
# region right countries datagram
right_countries = ["United States", "Spain", "Japan", "Canada", "France"]
df_right_countries = inflation_data.loc[right_countries]
df_right_countries.sort_index(inplace=True)
# endregion

# region left countries datagram
left_countries = ["Portugal", "Brazil", "Belgium", "United Kingdom", "Nicaragua"]
df_left_countries = inflation_data.loc[left_countries]
df_left_countries.sort_index(inplace=True)
# endregion

# region Countries
countries = right_countries + left_countries
df_countries = inflation_data.loc[countries]
# endregion

# region WORLD GDP DATA LAST 5 YEARS
world_gdp_data_last5_year = pnd.read_csv('./data_source/world_gdp_data.csv', encoding='latin1')
world_gdp_data_last5_year.rename(columns={'country_name': 'country'}, inplace=True)
world_gdp_data_last5_year.set_index('country', inplace = True)
 
# Select the necessary columns
world_gdp_data_last5_year = world_gdp_data_last5_year[['2019', '2020', '2021', '2022', '2023']]
 
# Drop Nan records  
world_gdp_data_last5_year.dropna(axis=0, inplace=True)
# world_gdp_data.drop_duplicates(inplace=True)
 
world_gdp_data_last5_year = world_gdp_data_last5_year.loc[countries]
rigth_world_gdp_data_last5_year = world_gdp_data_last5_year.loc[right_countries]
left_world_gdp_data_last5_year = world_gdp_data_last5_year.loc[left_countries]

# Test dataframe
def test_world_gdp_data_last5_year():
    print('\nWORLD GDP DATA LAST 5 YEARS')
    print(world_gdp_data_last5_year)
# endregion