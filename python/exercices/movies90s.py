from pymongo import MongoClient
import json

def movies90s(movies_collection):
    movies_90s = []
    for movie in movies_collection.find({"year": {"$gte": 1990, "$lt": 2000}}):
        movies_90s.append(movie)
    return movies_90s