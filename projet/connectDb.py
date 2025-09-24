from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv

load_dotenv()
mongo_uri = os.getenv("MONGODB_URI")

def connectDb(dbname):
    try:
        client = MongoClient(mongo_uri)
        client.admin.command('ping')
        print("Connected to MongoDB")
        possible_dbs = [dbname]
        for db_name in possible_dbs:
            if db_name in client.list_database_names():
                print(f"Database '{db_name}' exists.")
            else:
                print(f"Database '{db_name}' does not exist.")

        db = client[dbname]
        return db
    
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None
    