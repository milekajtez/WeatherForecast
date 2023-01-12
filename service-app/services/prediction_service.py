import pandas
from helpers.help_data import weather_columns
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

    return 'Uploading file for prediction successfully'


def predict_service(start, end):
    print(start)
    print(end)
    """weather_data = prediction_collection.find_one({"index": "prediction"})
    weather = filter_by_date_range(weather_data['data'], start, end, 'datetime')

    if len(weather) == 0:
        return prediction_no_data_message

    weather_df = pandas.DataFrame(weather, columns=weather_columns_training)
    preparer = CustomPreparer(weather_df, NUMBER_OF_COLUMNS_PREDICTION, 1)
    test_x = preparer.prepare_for_prediction()
    print(test_x)
    ann_regression = AnnRegression()
    test_predict = ann_regression.predict_method(test_x)
    print(test_predict)
    """
    return "test_predict"
