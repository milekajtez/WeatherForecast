from helpers.ann_base import AnnBase
from tensorflow import keras

MODEL_FOR_PREDICTION_NAME = "trained_model_01-18-2023_22-59-22"


def get_model_from_path(path):
    model = keras.models.load_model(path)
    return model


class PredictionRegression(AnnBase):
    def __init__(self):
        super().__init__()
        self.test_predict = None
        self.test_x = None
        self.model = None

    def predict(self, test_x):
        self.test_x = test_x
        self.model = get_model_from_path(MODEL_FOR_PREDICTION_NAME)
        test_predict = self.model.predict(test_x)
        return test_predict
