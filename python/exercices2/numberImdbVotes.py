from unittest import result
from pymongo import MongoClient
import json

def numberImdbVotes(db):
    tab = []
    for movie in db.find({"imdb.votes": {"$gte": 0}}).sort("imdb.votes", -1).limit(5):
        tab.append(movie)
    return tab
