from fastapi import FastAPI
from services.import_files import ImportFiles
from services.load_data import LoadData
from weather_api.cors_configuration import configureCors
from weather_api.controllers import test_controller

# Swagger UI: http://127.0.0.1:8000/docs
# ReDoc: http://127.0.0.1:8000/redoc

app = FastAPI()
configureCors(app)

import_files = ImportFiles()
load_data = LoadData()

app.include_router(test_controller.router, prefix='/test')


@app.get("/importFiles/loadCSVNames")
async def loadNamesOfAllCSVFiles():
    return import_files.loadNamesOfAllCSVFiles()


@app.post("/importDataFromCSV")
async def getImportFiles():
    return import_files.importDataFromCSVToDatabase


@app.get("/loadDataForDisplay", status_code=200)
async def loadDataForDisplay(load_type: str = "load"):
    return load_data.loadDataForDisplay(load_type)


@app.get("/averageTemperaturesPerYears")
async def getTemperaturesAveragePerYear():
    return load_data.getTemperaturesAveragePerYear()


@app.get("/getNumberOfDaysWithSpecificConditionsPerYear")
async def getTemperaturesAveragePerYear(year: str = "2018"):
    return load_data.getNumberOfDaysWithSpecificConditionsPerYear(year)


@app.get("/getMonthsTemperature")
async def getMonthsTemperature():
    return load_data.getMonthsTemperature()


@app.get("/getMonthsLoads")
async def getMonthsLoads():
    return load_data.getMonthsLoads()
