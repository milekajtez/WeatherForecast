from models.holiday import Holiday

processing_data_success_message = "Import data from csv successfully. See 'Display data' page to see all imported data"
weather_columns = ['datetime', 'temp', 'feelslike', 'humidity', 'snow', 'windspeed', 'winddir', 'cloudcover',
                   'conditions']
load_columns = ['Time Stamp', 'Name', 'Load']

weather_only_datetime = ['datetime']
weather_columns_training = ['temp', 'winddir', 'conditions']
load_columns_training = ['Load']
load_for_prediction = ['snow']

training_success_message = 'Training successfully completed'
training_no_data_message = "For current date range we don't have any data for training"
prediction_no_data_message = "for current date range we don't have any data for prediction"
prediction_uploaded_success = 'Uploading file for prediction successfully'

weekend_sunday_weight = 3
weekend_saturday_weight = 1.5
finally_friday_weight = 1
job_days_weight = 0

winter = 1.5
spring = 1
summer = 3
autumn = 1

weather_conditions = [
    'Clear',
    'Partially cloudy',
    'Overcast',
    'Rain',
    'Rain, Partially cloudy',
    'Rain, Overcast',
    'Snow, Partially cloudy',
    'Snow, Overcast',
    'Snow'
]

holidays = [
    Holiday("01/01/2018", 0.25, job_days_weight),
    Holiday("01/01/2019", 0.25, job_days_weight),
    Holiday("01/01/2020", 0.25, job_days_weight),
    Holiday("01/01/2021", 0.25, job_days_weight),
    Holiday("04/01/2018", 0.15, weekend_sunday_weight),
    Holiday("04/21/2019", 0.15, weekend_sunday_weight),
    Holiday("04/12/2020", 0.66, weekend_sunday_weight),
    Holiday("05/02/2021", 0.66, weekend_sunday_weight),
    Holiday("07/04/2018", 0.25, job_days_weight),
    Holiday("07/04/2019", 0.25, job_days_weight),
    Holiday("07/04/2020", 0.25, weekend_saturday_weight),
    Holiday("07/04/2021", 0.25, weekend_sunday_weight),
    Holiday("10/31/2018", 0.15, job_days_weight),
    Holiday("10/31/2019", 0.15, job_days_weight),
    Holiday("10/31/2020", 0.15, weekend_saturday_weight),
    Holiday("10/31/2021", 0.15, weekend_saturday_weight)
]
