from pymongo import MongoClient
import json

def goodMovie(movies_collection):
    goodMovies = []
    for movie in movies_collection.find({"imdb.rating": {"$gt": 8}}):
        goodMovies.append(movie)
    return goodMovies
