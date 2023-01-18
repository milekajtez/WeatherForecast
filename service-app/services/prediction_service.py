import pandas
from helpers.help_data import weather_columns, prediction_no_data_message, prediction_uploaded_success, \
    weather_columns_training, load_for_prediction, weather_only_datetime
from io import StringIO
import numpy as np
from services.import_data_service import parse_weather_conditions, make_weight_column, make_season_column
from data_access.data_access_db import insert_prediction_data, prediction_collection, insert_prediction_result
from services.training_service import filter_by_date_range
from helpers.prediction.prediction_preparer import PredictionPreparer
from helpers.prediction.prediction_regression import PredictionRegression
from models.prediction_result import PredictionResult

NUMBER_OF_COLUMNS_PREDICTION = 3
CSV_NAME = "predict_result.csv"

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
    weather_data = prediction_collection.find_one({"index": "prediction"})
    weather = filter_by_date_range(weather_data['data'], start, end, 'datetime')
    if len(weather) == 0:
        return prediction_no_data_message

    weather_df = pandas.DataFrame(weather, columns=weather_columns_training)
    load_df = pandas.DataFrame(weather, columns=load_for_prediction)
    preparer = PredictionPreparer(weather_df, load_df, NUMBER_OF_COLUMNS_PREDICTION)
    test_x = preparer.prepare_for_prediction()
    regression = PredictionRegression()
    test_predict = regression.predict(test_x)

    predicted_loads = preparer.inverse_transform_for_prediction(test_predict)
    datetimes = [item['datetime'] for item in weather]
    mongoDbData = [{'datetime': datetime, 'load': predicted_loads[index]} for index, datetime in enumerate(datetimes)]

    makeCSV(datetimes, predicted_loads)
    insert_prediction_result({"index": "prediction", "data": mongoDbData})

    return PredictionResult(datetimes, predicted_loads);

def makeCSV(datetimes, predicted_loads):
    df = pandas.DataFrame({'Datetime': datetimes, 'Load': predicted_loads})
    df.to_csv(CSV_NAME, index=False)
