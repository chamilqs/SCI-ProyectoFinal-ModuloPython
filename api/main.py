from fastapi import FastAPI, HTTPException
from InflationModel import Inflation
import InflationService

app = FastAPI()

@app.get('/get-all', status_code=200, response_model=list[Inflation])
async def get_all() -> list[Inflation]:
    try:
        inflationList = InflationService.GetAll()

        if inflationList == None:
            return HTTPException(status_code=404, detail="County Not Found")
        
        return inflationList
    except:
        return HTTPException(status_code=500, detail="Internal Error")


@app.get('/get-by-name/{country}', status_code=200, response_model=Inflation)
async def get_by_name(country: str) -> Inflation:
    inflation = InflationService.GetByCountry(country)

    if inflation == None:
        raise HTTPException(status_code=404, detail="Country Not Found")
        
    return inflation 

@app.get('/get-all-left', status_code=200, response_model=list[Inflation])
async def get_all_left() -> list[Inflation]:
    leftInflationList = InflationService.GetAllLeft()

    if leftInflationList == None:
        raise HTTPException(status_code=404, detail="Countries Not Found")
        
    return leftInflationList

@app.get('/get-all-right', status_code=200, response_model=list[Inflation])
async def get_all_right() -> list[Inflation]:
    rightInflationList = InflationService.GetAllRight()

    if rightInflationList == None:
        raise HTTPException(status_code=404, detail="Countries Not Found")
        
    return rightInflationList