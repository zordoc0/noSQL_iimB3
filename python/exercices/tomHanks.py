from pymongo import MongoClient
import json

def tomHanks(movies_collection):
    tom_hanks_movies = []
    query = {
        "cast": "Tom Hanks"
    }
    for movie in movies_collection.find(query):
        tom_hanks_movies.append(movie)
    return tom_hanks_movies 