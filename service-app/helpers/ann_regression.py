from keras.models import Sequential
from keras.layers import Dense
from helpers.ann_base import AnnBase
from tensorflow import keras
from datetime import datetime

MODEL_NAME = "trained_model_" + str(datetime.now().strftime("%m-%d-%Y_%H-%M-%S"))


def get_model_from_path(path):
    model = keras.models.load_model(path)
    return model


class AnnRegression(AnnBase):
    def __init__(self):
        super().__init__()
        self.train_x = None
        self.model = None

    def get_model(self):
        model = Sequential()
        if self.number_of_hidden_layers > 0:
            model.add(Dense(self._number_of_neurons_in_first_hidden_layer, input_shape=(1, 3),
                            kernel_initializer=self.kernel_initializer, activation=self.activation_function))
            if self.number_of_hidden_layers > 1:
                for i in range(self.number_of_hidden_layers - 1):
                    model.add(
                        Dense(self.number_of_neurons_in_other_hidden_layers, kernel_initializer=self.kernel_initializer,
                              activation=self.activation_function))
        model.add(Dense(1, kernel_initializer=self.kernel_initializer))
        return model

    def compile_and_fit(self, train_x, train_y):
        self.model = self.get_model()
        self.model.compile(loss=self.cost_function, optimizer=self.optimizer)
        self.train_x = train_x
        self.model.fit(
            train_x, train_y, epochs=self.epoch_number, batch_size=self.batch_size_number, verbose=self.verbose)
        self.model.save(MODEL_NAME)

    def get_predict(self, test_x):
        train_predict = self.model.predict(self.train_x)
        test_predict = self.model.predict(test_x)
        return train_predict, test_predict

    def compile_fit_predict(self, train_x, train_y, test_x):
        self.compile_and_fit(train_x, train_y)
        # self.use_current_model(MODEL_NAME, train_x)
        return self.get_predict(test_x)
