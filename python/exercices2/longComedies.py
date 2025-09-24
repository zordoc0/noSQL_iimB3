from pymongo import MongoClient
import json

def longComedies(movies_collection):
    long_comedies = []
    for movie in movies_collection.find({"genres": "Comedy"}).sort("runtime", -1).limit(5):
        long_comedies.append(movie)
    return long_comedies