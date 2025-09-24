from pymongo import MongoClient
import json

def titleYear(moviesCollection):
    titles_years = []
    for movie in moviesCollection.find({}, {"title": 1, "year": 1, "_id": 0}):
        titles_years.append(movie)
    return titles_years