import numpy
from sklearn.preprocessing import MinMaxScaler

LOAD_MAX = 9573
LOAD_MIN = 4115

class PredictionPreparer:
    def __init__(self, weather_df, load_df, number_of_columns):
        self.test_x = None
        self.number_of_columns = number_of_columns
        self.scaler_weather = MinMaxScaler(feature_range=(0, 1))
        self.datasetOrig_weather = weather_df.values
        self.datasetOrig_weather = self.datasetOrig_weather.astype('float32')
        self.scaler_load = MinMaxScaler(feature_range=(0, 1))
        self.datasetOrig_load = weather_df.values
        self.datasetOrig_load = self.datasetOrig_weather.astype('float32')

    def prepare_for_prediction(self):
        dataset = self.scaler_weather.fit_transform(self.datasetOrig_weather)
        test_x = numpy.reshape(dataset, (dataset.shape[0], 1, dataset.shape[1]))
        self.test_x = test_x
        return test_x.copy()

    def inverse_transform_for_prediction(self, test_predict):
        test_predict = numpy.reshape(test_predict, (test_predict.shape[0], test_predict.shape[1]))

        resulted_values = []
        for item in test_predict:
            new_value = item[0] * LOAD_MAX + LOAD_MIN
            resulted_values.append(new_value)

        return resulted_values

    @staticmethod
    def create_dataset(dataset, look_back):
        data_x = [],
        for i in range(len(dataset)):
            a = dataset[i, 0:look_back]
            data_x.append(a)

        return numpy.array(data_x)