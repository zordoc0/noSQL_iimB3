from pymongo import MongoClient
import json

def comedy(moviesCollection):
    comedies = []
    for movie in moviesCollection.find({"genres": "Comedy"}):
        comedies.append(movie)
    return comedies