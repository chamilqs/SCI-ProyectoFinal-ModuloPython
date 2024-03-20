from InflationModel import Inflation
import dataframes as df

def GetAll() -> list[Inflation]:
    try:
        inflation_data = df.inflation_data.reset_index()
        inflation_data = tuple(inflation_data.values)

        inflationList = list(map(lambda inflation: Inflation(
            Country = inflation[0],
            AnnualIncome = inflation[1],
            CorruptionIndex = inflation[2],
            GDP = inflation[3],
            CPI = inflation[4],
            CPIChange = inflation[5],
            Population = inflation[6],
            GasolinePrice = inflation[7],
            UnemploymentRate = inflation[8]
        ), inflation_data))
    
        return inflationList
    except:
        return None

def GetByCountry(country: str) -> Inflation:
    try:
        country_inflation_data = df.inflation_data.loc[country]        
        country_inflation_data = tuple(country_inflation_data.values)

        country_inflation = Inflation(
            Country = country,
            AnnualIncome = country_inflation_data[0],
            CorruptionIndex = country_inflation_data[1],
            GDP = country_inflation_data[2],
            CPI = country_inflation_data[3],
            CPIChange = country_inflation_data[4],
            Population = country_inflation_data[5],
            GasolinePrice = country_inflation_data[6],
            UnemploymentRate = country_inflation_data[7]
        )
    
        return country_inflation
    except Exception as ex:
        return ex

def GetAllLeft() -> list[Inflation]:
    try:
        left_inflation_data = df.df_left_countries.reset_index()
        left_inflation_data = tuple(left_inflation_data.values)

        leftInflationList = list(map(lambda inflation: Inflation(
            Country = inflation[0],
            AnnualIncome = inflation[1],
            CorruptionIndex = inflation[2],
            GDP = inflation[3],
            CPI = inflation[4],
            CPIChange = inflation[5],
            Population = inflation[6],
            GasolinePrice = inflation[7],
            UnemploymentRate = inflation[8]
        ), left_inflation_data))

        return leftInflationList
    except:
        return None
    
def GetAllRight() -> list[Inflation]:
    try:
        right_inflation_data = df.df_right_countries.reset_index()
        right_inflation_data = tuple(right_inflation_data.values)

        rightInflationList = list(map(lambda inflation: Inflation(
            Country = inflation[0],
            AnnualIncome = inflation[1],
            CorruptionIndex = inflation[2],
            GDP = inflation[3],
            CPI = inflation[4],
            CPIChange = inflation[5],
            Population = inflation[6],
            GasolinePrice = inflation[7],
            UnemploymentRate = inflation[8]
        ), right_inflation_data))

        return rightInflationList
    except:
        return None