from fastapi import APIRouter
from services.training_service import training_model_service

router = APIRouter()


@router.post("/trainingModel")
async def training_model(start: str = "01-01-0001", end: str = "01-01-0001", option: str = '90'):
    return training_model_service(start, end, option)
