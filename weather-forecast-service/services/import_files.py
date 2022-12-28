import os
from datetime import datetime

import numpy as np
import pandas

from data_access.data_access_db import insert_weather_data, insert_load_data
from helpers.help_data import weather_columns, load_columns, job_days_weight, finally_friday_weight, \
    weekend_saturday_weight, weekend_sunday_weight, holidays

pandas.set_option('display.max_rows', None)

TRAINING_DATA = './Training Data'
WEATHER_DATA = './Training Data/NYS Weather Data'
LOAD_DATA = './Training Data/NYS Load  Data'


class ImportFiles:
    @staticmethod
    def loadNamesOfAllCSVFiles():
        result = []
        for path, dirs, files in os.walk(TRAINING_DATA):
            for f in files:
                result.append(f)

        return result

    @staticmethod
    def loadAllPaths(data_type):
        paths = []
        for root, dirs, files in os.walk(os.path.abspath(LOAD_DATA if data_type == 'load' else WEATHER_DATA)):
            for file in files:
                paths.append(os.path.join(root, file))

        return paths

    @staticmethod
    def makeWeightColumn(dates_columns):
        weight_column = []
        for date in dates_columns:
            current_date = datetime.strptime(date.split(' ')[0], '%m/%d/%Y').date()
            current_weekday = current_date.weekday()

            weight = 1
            holiday = [obj for obj in holidays if obj.get_date() == current_date]
            if len(holiday) > 0:
                weight += holiday[0].holiday_weight

            weight += job_days_weight if current_weekday <= 3 else finally_friday_weight if current_weekday == 4 else \
                weekend_saturday_weight if current_weekday == 5 else weekend_sunday_weight

            weight_column.append(weight)

        return weight_column

    @property
    def importDataFromCSVToDatabase(self):
        paths_load = self.loadAllPaths('load')
        paths_weather = self.loadAllPaths('weather')

        weather_current = []
        for path in paths_weather:
            df = pandas.DataFrame()
            df.sort_index(inplace=True)
            df = pandas.read_csv(path, engine='python', sep=',', header=0, usecols=weather_columns)
            df = df.interpolate(method='pad')
            df['temp'] = np.where(df['temp'] > 140, np.nan, df['temp'])
            df = df.interpolate(method='linear')
            weather_current.append(df)

        weather_combined = pandas.concat(weather_current)

        load_current = []
        for path in paths_load:
            df = pandas.DataFrame()
            df.sort_index(inplace=True)
            df = pandas.read_csv(path, engine='python', sep=',', header=0, usecols=load_columns)
            df = df.interpolate(method='linear')
            load_current.append(df[(df['Name'] == 'N.Y.C.') & (df['Time Stamp'].str.contains(':00:00'))])

        load_combined = pandas.concat(load_current)
        load_combined['Weight'] = self.makeWeightColumn(load_combined['Time Stamp'])

        weather_combined.reset_index(inplace=True)
        weather_dict = weather_combined.to_dict("records")

        load_combined.reset_index(inplace=True)
        load_dict = load_combined.to_dict("records")

        insert_weather_data({"index": "weather", "data": weather_dict})
        insert_load_data({"index": "load", "data": load_dict})

        return 'Success'
