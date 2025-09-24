from pymongo import MongoClient
import json

def moviesByGender(movies_collection):
    pipeline = [
        {"$unwind": "$genres"}, #Découpe par genre
        {"$group": {"_id": "$genres", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    result = list(movies_collection.aggregate(pipeline))
    return result