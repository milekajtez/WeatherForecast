from fastapi import FastAPI

from helpers.define_configuration import DefineConfiguration
from services.import_files import ImportFiles
from services.load_data import LoadData

app = FastAPI()
config = DefineConfiguration()
config.configureCors(app)

import_files = ImportFiles()
load_data = LoadData()


@app.get("/")
async def getMessage():
    return 'test'


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
