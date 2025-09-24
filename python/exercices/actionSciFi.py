from pymongo import MongoClient
import json

def actionSciFi(movies_collection):
    action_sci_fi_movies = []
    query = {
        "genres": {"$all": ["Action", "Sci-Fi"]}
    }
    for movie in movies_collection.find(query):
        action_sci_fi_movies.append(movie)
    return action_sci_fi_movies