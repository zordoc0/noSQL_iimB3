from pymongo import MongoClient
import json

def filmsFrom1999(moviesCollection):
    movies = []
    for movie in moviesCollection.find({"year": 1999}):
        movies.append(movie)
    return movies