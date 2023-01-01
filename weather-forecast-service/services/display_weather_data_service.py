import datetime

from data_access.data_access_db import weather_collection
from models.Temperature import Temperature


def average_temperatures_per_year_service():
    weather_data = weather_collection.find_one({"index": "weather"})
    # Initialize variables for each year
    averages = {
        '2018': 0,
        '2019': 0,
        '2020': 0,
        '2021': 0
    }

    counts = {
        '2018': 0,
        '2019': 0,
        '2020': 0,
        '2021': 0
    }

    # Iterate over the weather data and sum the temperatures and counts for each year
    for item in weather_data['data']:
        year = item['datetime'][6:10]
        if year in averages:
            averages[year] += float(item['temp'])
            counts[year] += 1

    # Calculate the average temperature for each year
    avg_temps = [averages[year] / counts[year] for year in averages]
    return avg_temps


def get_conditions_per_year_service(year):
    weather_data = weather_collection.find_one({"index": "weather"})

    # Initialize variables for each weather condition
    counts = {
        'Clear': 0,
        'Partially cloudy': 0,
        'Overcast': 0,
        'Rain, Partially cloudy': 0,
        'Rain, Overcast': 0,
        'Snow, Partially cloudy': 0,
        'Snow, Overcast': 0
    }
    total_count = 0

    # Iterate over the weather data and count the occurrences of each weather condition
    for item in weather_data['data']:
        if year in item['datetime']:
            condition = item['conditions']
            if condition in counts:
                counts[condition] += 1
                total_count += 1

    # Calculate the percentage of each weather condition
    percentages = {condition: counts[condition] * 100 / total_count for condition in counts}
    return list(percentages.values())


def get_temperature_per_month_service():
    weather_data = weather_collection.find_one({"index": "weather"})
    # Initialize variables for each year
    months = {
        '2018': [0] * 12,
        '2019': [0] * 12,
        '2020': [0] * 12,
        '2021': [0] * 12
    }
    counts = {
        '2018': [0] * 12,
        '2019': [0] * 12,
        '2020': [0] * 12,
        '2021': [0] * 12
    }

    # Iterate over the weather data and sum the temperatures and counts for each month of each year
    for item in weather_data['data']:
        year = item['datetime'][6:10]
        month = int(item['datetime'][:2]) - 1
        if year in months:
            months[year][month] += float(item['temp'])
            counts[year][month] += 1

    # Calculate the average temperature for each month of each year
    avg_temps = {
        year: [months[year][i] / counts[year][i] if counts[year][i] != 0 else 0 for i in range(12)] for year in months
    }

    return Temperature(*avg_temps.values())


def get_other_weather_data_service(year):
    weather_data = weather_collection.find_one({"index": "weather"})

    counts = {
        'windSpeed': [0] * 12,
        'cloudCover': [0] * 12,
        'snow': [0] * 12
    }

    # Iterate over the weather data and sum the temperatures and counts for each month of each year
    earliest_date = datetime.datetime(1, 1, 1, 0, 0)
    current_date = earliest_date.strftime("%m/%d/%Y")
    for item in weather_data['data']:
        current_year = item['datetime'][6:10]
        if current_year != year:
            continue

        if current_date == item['datetime'][0:10]:
            continue

        month = int(item['datetime'][:2]) - 1
        if item['windspeed'] != 0:
            counts['windSpeed'][month] += 1
            current_date = item['datetime'][0:10]
        if item['cloudcover'] != 0:
            counts['cloudCover'][month] += 1
            current_date = item['datetime'][0:10]
        if item['snow'] != 0:
            counts['snow'][month] += 1
            current_date = item['datetime'][0:10]

    return counts
