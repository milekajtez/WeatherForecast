import pymongo

PORT = 27017
DATABASE_NAME = 'forecast_db'
LOAD_COLLECTION_NAME = 'load_collection'
WEATHER_COLLECTION_NAME = 'weather_collection'

connection = pymongo.MongoClient('localhost', PORT)
database = connection[DATABASE_NAME]
load_collection = database[LOAD_COLLECTION_NAME]
weather_collection = database[WEATHER_COLLECTION_NAME]


def insert_weather_data(data):
    weather_collection.insert_one(data)
    print("ssss")


def insert_load_data(data):
    load_collection.insert_many(data)
