from pymongo import MongoClient
import json

def recentMovies(movies_collection):
    recent_movies = []
    for movie in movies_collection.find({"released": {"$ne": None}}).sort("released", -1).limit(5):
        recent_movies.append(movie)
    return recent_movies