from fastapi import APIRouter
from services.display_load_data_service import get_loads_per_month_service

router = APIRouter()


@router.get("/getLoadsPerMonth", tags=['Display load data'])
async def get_loads_per_month():
    return get_loads_per_month_service()
