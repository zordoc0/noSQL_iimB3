from pymongo import MongoClient
import json

def selectCollection(db, collection_name):
    try:
        collection = db[collection_name]
        return collection
    except Exception as e:
        print(f"Error selecting collection: {e}")
        return None
