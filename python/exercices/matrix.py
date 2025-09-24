from pymongo import MongoClient
import json

def matrix(collectionName):
    matrix_movies = []
    for movie in collectionName.find({"title": "The Matrix"}):
        matrix_movies.append(movie)
    return matrix_movies