from fastapi import FastAPI
from helpers.define_configuration import DefineConfiguration
from services.importFiles import ImportFiles

app = FastAPI()
config = DefineConfiguration()
config.configureCors(app)

import_files = ImportFiles()


@app.get("/")
async def getMessage():
    return 'test'


@app.get("/importFiles/loadCSVNames")
async def loadNamesOfAllCSVFiles():
    return import_files.loadNamesOfAllCSVFiles()


@app.post("/importDataFromCSV")
async def getImportFiles():
    return import_files.importDataFromCSVToDatabase
