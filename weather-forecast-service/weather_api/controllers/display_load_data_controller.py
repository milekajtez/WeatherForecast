from fastapi import APIRouter
from services.display_load_data_service import get_loads_per_month_service, get_loads_and_temperature_service

router = APIRouter()


@router.get("/getLoadsPerMonth", tags=['Display load data'])
async def get_loads_per_month():
    return get_loads_per_month_service()


@router.get("/getLoadsAndTemperature", tags=['Display load data'])
async def get_loads_and_temperature(start: str = "01-01-0001", end: str = "01-01-0001"):
    return get_loads_and_temperature_service(start, end)
