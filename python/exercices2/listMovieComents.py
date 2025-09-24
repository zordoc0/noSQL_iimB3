from pymongo import MongoClient
import json

def listMovieComents(movies_collection, comments_collection):
    pipeline = [
        {
            "$lookup": {
                "from": "comments",
                "localField": "title",
                "foreignField": "movie_title",
                "as": "comments"
            }
        },
        {
            "$project": {
                "title": 1,
                "comments.text": 1,
                "_id": 0
            }
        }
    ]

    result = list(movies_collection.aggregate(pipeline))
    return result