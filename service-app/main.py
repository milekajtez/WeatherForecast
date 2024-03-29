from fastapi import FastAPI
from weather_api.cors_configuration import configureCors
from weather_api.controllers import import_and_process_data_controller, \
    display_weather_data_controller, display_load_data_controller, training_controller, prediction_controller

# Swagger UI: http://127.0.0.1:8000/docs
# ReDoc: http://127.0.0.1:8000/redoc

app = FastAPI()
configureCors(app)

app.include_router(import_and_process_data_controller.router, prefix='/importData')
app.include_router(display_weather_data_controller.router, prefix='/displayWeatherData')
app.include_router(display_load_data_controller.router, prefix='/displayLoadData')
app.include_router(training_controller.router, prefix='/training')
app.include_router(prediction_controller.router, prefix='/prediction')
