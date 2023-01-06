import math
from sklearn.metrics import mean_squared_error, mean_absolute_error


class Scorer:
    @staticmethod
    def get_rmse_error(train_y, train_predict, test_y, test_predict):
        train_score = math.sqrt(mean_squared_error(train_y, train_predict))
        test_score = math.sqrt(mean_squared_error(test_y, test_predict))
        return train_score, test_score

    @staticmethod
    def get_mape_error(y_actual, forecast):
        n = len(y_actual)
        mape = sum(abs(y_actual[i] - forecast[i]) / abs(y_actual[i]) for i in range(n)) * 100 / n
        return mape
