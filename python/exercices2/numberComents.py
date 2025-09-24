from pymongo import MongoClient
import json

def numberComents(movies_collection):
    pipeline = [
        {"$match": {"imdb.rating": {"$exists": True}}},
        {"$group": {
            "_id": None,
            "totalComments": {"$sum": "$imdb.votes"}
        }}
    ]
    
    result = list(movies_collection.aggregate(pipeline))
    return result[0]['totalComments'] if result else 0