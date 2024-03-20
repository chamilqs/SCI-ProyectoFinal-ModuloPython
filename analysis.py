import pandas as pnd
import dataframes as df
 
#Initial Summary of data
print('\n\SUMMARY OF INFLATION DATASET: \n')
summary_initial = df.inflation_data.info()
print(summary_initial)
 
#Simple stats of the inflation dataset
print('\n\nSTATISTICS OF INFLATION DATASET: \n')
stats = df.inflation_data.describe()
print(stats)

# Right Countries
right_countries = ["United States", "Brazil", "Japan", "Canada", "France"]
right_countries_df = df.inflation_data.loc[right_countries]
print(right_countries_df.head())
 
# Left Countries
left_countries = ["Portugal", "Sweden", "Belgium", "United Kingdom", "Nicaragua"]
left_countries_df = df.inflation_data.loc[left_countries]
print(left_countries_df.head())
 
# Richest Countries
richest_countries = df.richest_countries.head(5)
print(richest_countries)


 
