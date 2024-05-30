from pymongo import MongoClient

def get_mongo_client():
    client = MongoClient('mongodb://localhost:27017/')  # Update with your MongoDB connection string
    return client

def get_database(client, db_name):
    return client[db_name]
