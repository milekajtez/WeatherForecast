import os
import pandas

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

        data_frame_weather = pandas.DataFrame()

        for path in paths_weather:
            current = pandas.read_csv(path, engine='python', sep=',', header=None,
                                      names=['name', 'datetime', 'conditions'])
            data_frame_weather = pandas.concat([data_frame_weather, current])

        current = []
        for path in paths_load:
            df = pandas.DataFrame()
            df.sort_index(inplace=True)
            df = pandas.read_csv(path, engine='python', sep=',', header=None,
                                 names=['Date', 'Time Stamp', 'Name', 'PTID', 'Load'])

            current.append(df[(df['Name'] == 'N.Y.C.') & (df['Date'].str.contains('00:00'))])

        combined = pandas.concat(current)
        print(combined)
        return 'Success'
