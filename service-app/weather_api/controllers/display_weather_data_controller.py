from fastapi import APIRouter

from services.display_weather_data_service import average_temperatures_per_year_service, \
    get_conditions_per_year_service, get_temperature_per_month_service, get_other_weather_data_service

router = APIRouter()


@router.get("/averageTemperaturesPerYear", tags=['Display weather data'])
async def average_temperatures_per_year():
    return average_temperatures_per_year_service()


@router.get("/getConditionsPerYear", tags=['Display weather data'])
async def get_conditions_per_year(year: str = "2018"):
    return get_conditions_per_year_service(year)


@router.get("/getTemperaturePerMonth", tags=['Display weather data'])
async def get_temperature_per_month():
    return get_temperature_per_month_service()


@router.get("/getOtherWeatherData", tags=['Display weather data'])
async def get_other_weather_data(year: str = "2018"):
    return get_other_weather_data_service(year)
