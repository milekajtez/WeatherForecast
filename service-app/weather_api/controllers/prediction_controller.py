from fastapi import APIRouter, UploadFile, File

from services.prediction_service import upload_data_for_prediction_service, predict_service

router = APIRouter()


@router.post("/uploadDataForPrediction", tags=['Prediction'])
async def upload_data_for_prediction(fileForPrediction: UploadFile = File()):
    data = await fileForPrediction.read()
    return upload_data_for_prediction_service(data)


@router.get("/predict", tags=['Prediction'])
async def predict(start: str = "01-01-0001", end: str = "01-01-0001"):
    return predict_service(start, end)
