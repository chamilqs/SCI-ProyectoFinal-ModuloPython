from pydantic import BaseModel

class Inflation(BaseModel):
    Country: str
    AnnualIncome: int
    CorruptionIndex: int
    GDP: float
    CPI: str
    CPIChange: float
    Population: str
    GasolinePrice: str
    UnemploymentRate: float