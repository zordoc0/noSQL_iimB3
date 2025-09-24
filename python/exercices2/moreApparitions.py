from pymongo import MongoClient
import json

def moreApparitions(comments_collection):
    pipeline = [
        {"$unwind": "$name"},
        {"$group": {
            "_id": "$name",
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1}},
        {"$limit": 5}
    ]

    result = list(comments_collection.aggregate(pipeline))
    return result