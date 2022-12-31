from fastapi import APIRouter

from services.import_data_service import load_all_csv_names_service, process_csv_data_service, \
    check_does_data_exists_service

router = APIRouter()


@router.get("/loadCSVNames", tags=['Import data'])
async def load_all_csv_names():
    return load_all_csv_names_service()


@router.get("/checkDoesDataExists")
async def check_does_data_exists():
    return check_does_data_exists_service()


@router.post("/processCsvData")
async def process_csv_data():
    return process_csv_data_service()
