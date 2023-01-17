import pandas
from helpers.help_data import weather_columns, prediction_uploaded_success
from io import StringIO
import numpy as np
from services.import_data_service import parse_weather_conditions, make_weight_column, make_season_column
from data_access.data_access_db import insert_prediction_data

NUMBER_OF_COLUMNS_PREDICTION = 5


def upload_data_for_prediction_service(data):
    data = data.decode('utf-8')
    test_data = StringIO(data)
    df = pandas.read_csv(test_data, sep=',', usecols=weather_columns)
    df.sort_index(inplace=True)
    df = df.interpolate(method='pad')
    df['datetime'] = pandas.to_datetime(df["datetime"], format='%Y-%m-%dT%H:%M:%S')
    df['datetime'] = df['datetime'].dt.strftime('%m/%d/%Y %H:%M:%S')
    df['temp'] = np.where(df['temp'] > 140, np.nan, df['temp'])
    df = df.interpolate(method='linear')

    df = parse_weather_conditions(df)
    df['weight'] = make_weight_column(df['datetime'])
    df['season'] = make_season_column(df['datetime'])

    df.reset_index(inplace=True)
    weather_dict = df.to_dict("records")
    insert_prediction_data({"index": "prediction", "data": weather_dict})

    return prediction_uploaded_success


def predict_service(start, end):
    print(start)
    print(end)
    return "test_predict"
