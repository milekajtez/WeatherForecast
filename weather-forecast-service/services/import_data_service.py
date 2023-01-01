import os
from datetime import datetime
import numpy as np
import pandas
from data_access.data_access_db import insert_weather_data, insert_load_data, load_collection, weather_collection
from helpers.help_data import weather_columns, load_columns, job_days_weight, finally_friday_weight, \
    weekend_saturday_weight, weekend_sunday_weight, holidays, processing_data_success_message

TRAINING_DATA_PATH = './Training Data'
WEATHER_DATA_PATH = './Training Data/NYS Weather Data'
LOAD_DATA_PATH = './Training Data/NYS Load  Data'


def load_all_csv_names_service():
    # Get a list of all the file paths in the root directory and its subdirectories
    file_paths = [os.path.join(root, file) for root, dirs, files in os.walk(TRAINING_DATA_PATH) for file in files]

    # Get only the names of the CSV files
    csv_file_names = [os.path.basename(path) for path in file_paths if path.endswith('.csv') or path.endswith('.xlsx')]

    return csv_file_names


def check_does_data_exists_service():
    load_data = load_collection.find_one({"index": "load"})
    weather_data = weather_collection.find_one({"index": "weather"})
    return load_data is not None and weather_data is not None


def process_csv_data_service():
    paths_load = load_all_paths('load')
    paths_weather = load_all_paths('weather')

    weather_combined = process_weather_data(paths_weather)

    load_combined = process_load_data(paths_load)

    load_combined['Weight'] = make_weight_column(load_combined['Time Stamp'])

    weather_combined.reset_index(inplace=True)
    weather_dict = weather_combined.to_dict("records")

    load_combined.reset_index(inplace=True)
    load_dict = load_combined.to_dict("records")

    insert_weather_data({"index": "weather", "data": weather_dict})
    insert_load_data({"index": "load", "data": load_dict})

    return processing_data_success_message


def process_weather_data(paths_weather):
    weather_data = []
    for path in paths_weather:
        df = pandas.read_csv(path, engine='python', sep=',', header=0, usecols=weather_columns)
        df.sort_index(inplace=True)
        df = df.interpolate(method='pad')
        df['datetime'] = pandas.to_datetime(df["datetime"], format='%Y-%m-%dT%H:%M:%S')
        df['datetime'] = df['datetime'].dt.strftime('%m/%d/%Y %H:%M:%S')
        df['temp'] = np.where(df['temp'] > 140, np.nan, df['temp'])
        df = df.interpolate(method='linear')
        weather_data.append(df)

    return pandas.concat(weather_data)


def process_load_data(paths_load):
    load_current = []
    for path in paths_load:
        df = pandas.read_csv(path, engine='python', sep=',', header=0, usecols=load_columns)
        df.sort_index(inplace=True)
        df = df.interpolate(method='linear')
        load_current.append(df[(df['Name'] == 'N.Y.C.') & (df['Time Stamp'].str.contains(':00:00'))])

    return pandas.concat(load_current)


def load_all_paths(data_type):
    # Determine the root directory to search based on the data_type parameter
    if data_type == 'load':
        root_dir = os.path.abspath(LOAD_DATA_PATH)
    elif data_type == 'weather':
        root_dir = os.path.abspath(WEATHER_DATA_PATH)
    else:
        raise ValueError('Invalid data_type: {}'.format(data_type))

    # Get a list of all the file paths in the root directory
    file_paths = [os.path.join(root, file) for root, dirs, files in os.walk(root_dir) for file in files]
    return file_paths


def make_weight_column(dates_columns):
    def get_weight(date):
        current_date = datetime.strptime(date.split(' ')[0], '%m/%d/%Y').date()
        current_weekday = current_date.weekday()

        weight = 1
        if current_date in holidays:
            weight += holidays[current_date].holiday_weight
        elif current_weekday <= 3:
            weight += job_days_weight
        elif current_weekday == 4:
            weight += finally_friday_weight
        elif current_weekday == 5:
            weight += weekend_saturday_weight
        else:
            weight += weekend_sunday_weight

        return weight

    weight_column = [get_weight(date) for date in dates_columns]
    return weight_column

