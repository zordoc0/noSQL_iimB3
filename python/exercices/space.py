from pymongo import MongoClient
import json

def space(movies_collection):
    space_movies = []
    query = {
        "plot": {"$regex": "space", "$options": "i"}
    }
    for movie in movies_collection.find(query):
        space_movies.append(movie)
    return space_movies