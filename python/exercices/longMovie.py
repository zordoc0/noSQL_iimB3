from pymongo import MongoClient
import json

def longMovie(moviesCollection):
    long_movies = []
    for movie in moviesCollection.find({"runtime": {"$gt": 120}}):
        long_movies.append(movie)
    return long_movies

