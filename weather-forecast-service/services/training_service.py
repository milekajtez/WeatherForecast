import pandas
from datetime import datetime
from data_access.data_access_db import load_collection, weather_collection
from helpers.ann_regression import AnnRegression
from helpers.custom_preparer import CustomPreparer
from helpers.scorer import Scorer
from helpers.help_data import training_success_message, training_no_data_message, weather_columns_training, \
    load_columns_training

NUMBER_OF_COLUMNS = 7


def training_model_service(start, end, option):
    load_data = load_collection.find_one({"index": "load"})
    weather_data = weather_collection.find_one({"index": "weather"})

    weather = filter_by_date_range(weather_data['data'], start, end, 'datetime')
    load = filter_by_date_range(load_data['data'], start, end, 'Time Stamp')
    if len(weather) == 0 or len(load) == 0:
        return training_no_data_message

    weather_df = pandas.DataFrame(weather, columns=weather_columns_training)
    load_df = pandas.DataFrame(load, columns=load_columns_training)

    weather_df = weather_df.replace(to_replace='Clear', value=0)
    weather_df = weather_df.replace(to_replace='Partially cloudy', value=1)
    weather_df = weather_df.replace(to_replace='Overcast', value=2)
    weather_df = weather_df.replace(to_replace='Rain', value=3)
    weather_df = weather_df.replace(to_replace='Rain, Partially cloudy', value=4)
    weather_df = weather_df.replace(to_replace='Rain, Overcast', value=5)
    weather_df = weather_df.replace(to_replace='Snow, Partially cloudy', value=6)
    weather_df = weather_df.replace(to_replace='Snow, Overcast', value=7)
    weather_df = weather_df.replace(to_replace='Snow', value=8)

    df_all_data = pandas.concat([load_df, weather_df], axis=1, ignore_index=True, sort=False)
    df_all_data = df_all_data.interpolate(method='linear')
    date_frame_for_training = df_all_data.rename(columns={0: 'Time Stamp', 1: 'Load', 2: 'Temp', 3: 'Feelslike',
                                                          4: 'Snow', 5: 'Windspeed', 6: 'Cloudcover', 7: 'Conditions'})

    preparer = CustomPreparer(date_frame_for_training, NUMBER_OF_COLUMNS, float(option) / 100)
    train_x, train_y, test_x, test_y = preparer.prepare_for_training()

    ann_regression = AnnRegression()
    train_predict, test_predict = ann_regression.compile_fit_predict(train_x, train_y, test_x)
    train_predict, train_Y, test_predict, test_y = preparer.inverse_transform(train_predict, test_predict)
    scorer = Scorer()
    train_score, test_score = scorer.get_score(train_Y, train_predict, test_y, test_predict)
    print('Train Score: %.2f RMSE' % (train_score))
    print('Test Score: %.2f RMSE' % (test_score))

    result  = scorer.get_mape_score(test_y, test_predict)
    print(result)
    return training_success_message


def filter_by_date_range(array, start, end, date_column):
    list_result = []
    current_start = datetime.strptime(start, '%Y-%m-%d').date()
    current_end = datetime.strptime(end, '%Y-%m-%d').date()

    for item in array:
        current_date = datetime.strptime(item[date_column], '%m/%d/%Y %H:%M:%S').date()
        if current_start < current_date < current_end:
            list_result.append(item)

    return list_result
