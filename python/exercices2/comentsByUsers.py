from pymongo import MongoClient
import json

def comentsByUsers(comments_collection):
    pipeline = [
        {
            "$group": {
                "_id": "$name",
                "comments": {"$push": "$text"},
                "count": {"$sum": 1}
            }
        },
        {
            "$project": {
                "name": "$_id",
                "comments": 1,
                "count": 1,
                "_id": 0
            }
        },
        {
            "$sort": {"count": -1}
        }
    ]

    result = list(comments_collection.aggregate(pipeline))
    return result