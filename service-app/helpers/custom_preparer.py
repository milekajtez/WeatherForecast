import numpy
from sklearn.preprocessing import MinMaxScaler


class CustomPreparer:
    def __init__(self, dataframe, number_of_columns, share_for_training):
        self.test_y = None
        self.test_x = None
        self.train_y = None
        self.train_x = None
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.datasetOrig = dataframe.values
        self.datasetOrig = self.datasetOrig.astype('float32')
        self.number_of_columns = number_of_columns
        self.predictor_column_no = self.number_of_columns - 1
        self.share_for_training = share_for_training

    def prepare_for_training(self):
        dataset = self.scaler.fit_transform(self.datasetOrig)
        train_size = int(len(dataset) * self.share_for_training)
        # test_size = len(dataset) - train_size
        train, test = dataset[0:train_size, :], dataset[train_size:len(dataset), :]
        print(len(train), len(test))
        look_back = self.number_of_columns
        train_x, train_y = self.create_dataset(train, look_back)
        test_x, test_y = self.create_dataset(test, look_back)
        train_x = numpy.reshape(train_x, (train_x.shape[0], 1, train_x.shape[1]))
        test_x = numpy.reshape(test_x, (test_x.shape[0], 1, test_x.shape[1]))
        self.train_x = train_x
        self.train_y = train_y
        self.test_x = test_x
        self.test_y = test_y
        return train_x.copy(), train_y.copy(), test_x.copy(), test_y.copy()

    """def prepare_for_prediction(self):
        dataset = self.scaler.fit_transform(self.datasetOrig)
        train_size = int(len(dataset) * self.share_for_training)
        test_size = len(dataset) - train_size + 1
        test = dataset[test_size:len(dataset), :]
        look_back = self.number_of_columns
        test_x = self.create_dataset_for_prediction(test, look_back)
        test_x = numpy.reshape(test_x, (test_x.shape[0], 1, test_x.shape[1]))

        self.test_x = test_x

        train_size = int(len(dataset) * self.share_for_training)
        test_size = len(dataset) - train_size
        train, test = dataset[0:train_size, :], dataset[test_size:len(dataset), :]
        print(len(train), len(test))
        look_back = self.number_of_columns
        train_x, train_y = self.create_dataset(train, look_back)
        test_x, test_y = self.create_dataset(test, look_back)
        train_x = numpy.reshape(train_x, (train_x.shape[0], 1, train_x.shape[1]))
        test_x = numpy.reshape(test_x, (test_x.shape[0], 1, test_x.shape[1]))
        self.train_x = train_x
        self.train_y = train_y
        self.test_x = test_x
        self.test_y = test_y
        return train_x.copy(), train_y.copy(), test_x.copy(), test_y.copy()
        return test_x.copy()"""

    def inverse_transform(self, train_predict, test_predict):
        train_predict = numpy.reshape(train_predict, (train_predict.shape[0], train_predict.shape[1]))
        test_predict = numpy.reshape(test_predict, (test_predict.shape[0], test_predict.shape[1]))
        self.train_x = numpy.reshape(self.train_x, (self.train_x.shape[0], self.train_x.shape[2]))
        self.test_x = numpy.reshape(self.test_x, (self.test_x.shape[0], self.test_x.shape[2]))
        train_x_and_predict = numpy.concatenate((self.train_x, train_predict), axis=1)
        test_x_and_predict = numpy.concatenate((self.test_x, test_predict), axis=1)
        train_y = numpy.reshape(self.train_y, (self.train_y.shape[0], 1))
        test_y = numpy.reshape(self.test_y, (self.test_y.shape[0], 1))
        train_x_and_y = numpy.concatenate((self.train_x, train_y), axis=1)
        test_x_and_y = numpy.concatenate((self.test_x, test_y), axis=1)
        train_x_and_predict = self.scaler.inverse_transform(train_x_and_predict)
        train_x_and_y = self.scaler.inverse_transform(train_x_and_y)
        test_x_and_predict = self.scaler.inverse_transform(test_x_and_predict)
        test_x_and_y = self.scaler.inverse_transform(test_x_and_y)
        train_predict = train_x_and_predict[:, self.predictor_column_no]
        train_y = train_x_and_y[:, self.predictor_column_no]
        test_predict = test_x_and_predict[:, self.predictor_column_no]
        test_y = test_x_and_y[:, self.predictor_column_no]
        return train_predict, train_y, test_predict, test_y

    @staticmethod
    def create_dataset(dataset, look_back):
        data_x, data_y = [], []
        for i in range(len(dataset)-1):
            a = dataset[i, 0:look_back-1]
            data_x.append(a)
            data_y.append(dataset[i, look_back-1])
        return numpy.array(data_x), numpy.array(data_y)

    """@staticmethod
    def create_dataset_for_prediction(dataset, look_back):
        data_x = []
        for i in range(len(dataset) - 1):
            a = dataset[i, 0:look_back - 1]
            data_x.append(a)
        return numpy.array(data_x)"""
