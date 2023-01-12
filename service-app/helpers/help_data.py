from models.holiday import Holiday

processing_data_success_message = "Import data from csv successfully. See 'Display data' page to see all imported data"
weather_columns = ['datetime', 'temp', 'feelslike', 'snow', 'windspeed', 'cloudcover', 'conditions']
load_columns = ['Time Stamp', 'Name', 'Load']

weather_columns_training = ['temp', 'feelslike', 'weight', 'season']
load_columns_training = ['Load']

training_success_message = 'Training successfully completed'
training_no_data_message = "For current date range we don't have any data for training"
prediction_no_data_message = "for current date range we don't have any data for prediction"

weekend_sunday_weight = 0.35
weekend_saturday_weight = 0.3
finally_friday_weight = 0.15
job_days_weight = 0

winter = 0.15
spring = 0.05
summer = 0.35
autumn = 0.05

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
