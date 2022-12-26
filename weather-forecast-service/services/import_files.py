import os

import numpy as np
import pandas
from helpers.help_data import weather_columns, load_columns
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
        print(weather_combined)

        load_current = []
        for path in paths_load:
            df = pandas.DataFrame()
            df.sort_index(inplace=True)
            df = pandas.read_csv(path, engine='python', sep=',', header=0, usecols=load_columns)
            df = df.interpolate(method='linear')
            load_current.append(df[(df['Name'] == 'N.Y.C.') & (df['Time Stamp'].str.contains(':00:00'))])

        load_combined = pandas.concat(load_current)
        print(load_combined)
        # working with data
        # here will be adding data to mongodb database
        return 'Success'
