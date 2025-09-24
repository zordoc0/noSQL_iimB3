from pymongo import MongoClient
import json

def averageRatingByGender(movies_collection):
    pipeline = [
        {"$unwind" : "$genres"},
        {"$group": {"_id": "$genres", "averageRating": {"$avg": "$imdb.rating"}}},
        {"$sort": {"averageRating": -1}}
    ]
    result = list(movies_collection.aggregate(pipeline))
    return result