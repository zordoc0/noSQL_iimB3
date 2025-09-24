from pymongo import MongoClient
import json

def bestMovies(movies_collection):
    best_movies = []
    for movie in movies_collection.find({"imdb.rating": {"$gte": 5}}).sort("imdb.rating", -1).limit(10):
        best_movies.append(movie)
    return best_movies
