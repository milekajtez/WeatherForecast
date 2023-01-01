from models.Holiday import Holiday

processing_data_success_message = "Import data from csv successfully. See 'Display data' page to see all imported data"
weather_columns = ['datetime', 'temp', 'feelslike', 'snow', 'windspeed', 'cloudcover', 'conditions']
load_columns = ['Time Stamp', 'Name', 'Load']

weather_columns_training = ['temp', 'feelslike', 'snow', 'windspeed', 'cloudcover', 'conditions']
load_columns_training = ['Load']

training_success_message = 'Training successfully completed'
training_no_data_message = "For current date range we don't have any data for training"

weekend_sunday_weight = 0.75
weekend_saturday_weight = 0.5
finally_friday_weight = 0.25
job_days_weight = 0

weather_conditions = [
    'Clear',
    'Partially cloudy',
    'Overcast',
    'Rain',
    'Rain, Partially cloudy',
    'Rain, Overcast',
    'Snow, Partially cloudy',
    'Snow, Overcast'
]

holidays = [
    Holiday("2018-01-01", 0.67, job_days_weight),
    Holiday("2018-01-15", 0.7, job_days_weight),
    Holiday("2018-02-14", 0.56, job_days_weight),
    Holiday("2018-02-19", 0.35, job_days_weight),
    Holiday("2018-03-30", 0.35, finally_friday_weight),
    Holiday("2018-04-01", 0.66, weekend_sunday_weight),
    Holiday("2018-05-13", 0.76, weekend_sunday_weight),
    Holiday("2018-05-28", 0.75, job_days_weight),
    Holiday("2018-06-01", 0.4, finally_friday_weight),
    Holiday("2018-06-17", 0.71, weekend_sunday_weight),
    Holiday("2018-07-04", 0.9, job_days_weight),
    Holiday("2018-09-03", 0.7, job_days_weight),
    Holiday("2018-10-08", 0.25, job_days_weight),
    Holiday("2018-10-31", 0.67, job_days_weight),
    Holiday("2018-11-11", 0.76, weekend_sunday_weight),
    Holiday("2018-11-22", 0.8, job_days_weight),
    Holiday("2018-12-25", 0.75, job_days_weight),
    Holiday("2018-01-01", 0.67, job_days_weight),

    Holiday("2019-01-21", 0.7, job_days_weight),
    Holiday("2019-02-14", 0.56, job_days_weight),
    Holiday("2019-02-18", 0.35, job_days_weight),
    Holiday("2019-04-19", 0.35, finally_friday_weight),
    Holiday("2019-04-21", 0.66, weekend_sunday_weight),
    Holiday("2019-05-12", 0.76, weekend_sunday_weight),
    Holiday("2019-05-27", 0.75, job_days_weight),
    Holiday("2019-06-16", 0.71, weekend_sunday_weight),
    Holiday("2019-07-04", 0.9, job_days_weight),
    Holiday("2019-09-02", 0.7, job_days_weight),
    Holiday("2019-10-14", 0.25, job_days_weight),
    Holiday("2019-10-31", 0.67, job_days_weight),
    Holiday("2019-11-11", 0.76, job_days_weight),
    Holiday("2019-11-28", 0.8, job_days_weight),
    Holiday("2019-12-25", 0.75, job_days_weight),

    Holiday("2020-01-01", 0.67, job_days_weight),
    Holiday("2020-01-20", 0.7, job_days_weight),
    Holiday("2020-02-14", 0.56, finally_friday_weight),
    Holiday("2020-02-17", 0.35, job_days_weight),
    Holiday("2020-04-10", 0.35, finally_friday_weight),
    Holiday("2020-04-12", 0.66, weekend_sunday_weight),
    Holiday("2020-05-10", 0.76, weekend_sunday_weight),
    Holiday("2020-05-25", 0.75, job_days_weight),
    Holiday("2020-06-21", 0.71, weekend_sunday_weight),
    Holiday("2020-07-03", 0.9, finally_friday_weight),
    Holiday("2020-07-04", 0.9, weekend_saturday_weight),
    Holiday("2020-09-07", 0.7, job_days_weight),
    Holiday("2020-10-12", 0.25, job_days_weight),
    Holiday("2020-10-31", 0.67, weekend_saturday_weight),
    Holiday("2020-11-11", 0.76, job_days_weight),
    Holiday("2020-11-26", 0.8, job_days_weight),
    Holiday("2020-12-25", 0.75, finally_friday_weight),

    Holiday("2021-01-01", 0.67, job_days_weight),
    Holiday("2021-01-18", 0.7, job_days_weight),
    Holiday("2021-02-14", 0.56, weekend_saturday_weight),
    Holiday("2021-02-15", 0.35, job_days_weight),
    Holiday("2021-04-02", 0.35, finally_friday_weight),
    Holiday("2021-05-02", 0.66, weekend_sunday_weight),
    Holiday("2021-05-09", 0.76, weekend_sunday_weight),
    Holiday("2021-05-31", 0.75, job_days_weight),
    Holiday("2021-06-20", 0.71, weekend_sunday_weight),
    Holiday("2021-07-04", 0.9, weekend_sunday_weight),
    Holiday("2021-07-05", 0.9, job_days_weight),
    Holiday("2021-09-06", 0.7, job_days_weight),
    Holiday("2021-10-11", 0.25, job_days_weight),
    Holiday("2021-10-31", 0.67, weekend_saturday_weight),
    Holiday("2021-11-11", 0.76, job_days_weight),
    Holiday("2021-11-25", 0.8, job_days_weight),
    Holiday("2021-12-25", 0.75, finally_friday_weight)
]
