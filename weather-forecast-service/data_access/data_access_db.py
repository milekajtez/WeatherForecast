import pymongo

PORT = 27017
DATABASE_NAME = 'forecast_db'
COLLECTION_NAME = 'forecast_collection'

connection = pymongo.MongoClient('localhost', PORT)
database = connection[DATABASE_NAME]
collection = database[COLLECTION_NAME]


def insert_one_data(data):
    collection.insert_one(data)


def insert_data(data):
    collection.insert_many(data)
