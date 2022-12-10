from fastapi import FastAPI
from helpers.define_configuration import DefineConfiguration
from services.importFiles import ImportFiles

app = FastAPI()
config = DefineConfiguration()
config.configureCors(app)


@app.get("/")
async def getMessage():
    return 'test'


@app.get("/importFiles/loadCSVNames")
async def loadNamesOfAllCSVFiles():
    import_files = ImportFiles()
    return import_files.loadNamesOfAllCSVFiles()


@app.get("/importFiles")
async def getImportFiles():
    return {"message": "Import data"}
