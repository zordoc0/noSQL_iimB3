from pymongo import MongoClient
import json
from create.create import create_item, create_items
from get.get import get_item_by_attr
from connectDb import connectDb
import datetime

dbname = "rendu_b3_iim"
db = connectDb(dbname)




def seeder_users(collection):
    userstest = [
        {
            "name": "Alice",
            "email": "alice@example.com",
            "role": "admin"
        },
        {
            "name": "Bob",
            "email": "bob@example.com",
            "role": "worker"
        },
        {
            "name": "Charlie",
            "email": "charlie@example.com",
            "role": "admin"
        },
        {
            "name": "David",
            "email": "david@example.com",
            "role": "worker"
        },
        {
            "name": "Eve",
            "email": "eve@example.com",
            "role": "chief"
        },
        {
            "name": "Frank",
            "email": "frank@example.com",
            "role": "worker"
        },
        {
            "name": "Grace",
            "email": "grace@example.com",
            "role": "admin"
        },
        {
            "name": "Heidi",
            "email": "heidi@example.com",
            "role": "admin"
        },
        {
            "name": "Ivan",
            "email": "ivan@example.com",
            "role": "worker"
        },
        {
            "name": "Judy",
            "email": "judy@example.com",
            "role": "worker"
        },
    ]
    create_items(collection, userstest)

def seeder_teams(collection):
    teamstest = [
        {
            "name": "Team Workers",
            "members": get_item_by_attr(db['users'], {"role": "worker"}, fields={"_id":0,"pid":1})
        },
        {
            "name": "Team Admins",
            "members": get_item_by_attr(db['users'], {"role": "admin"}, fields={"_id":0,"pid":1})
        },
        {
            "name": "Team Chiefs",
            "members": get_item_by_attr(db['users'], {"role": "chief"}, fields={"_id":0,"pid":1})
        }
    ]
    create_items(collection, teamstest)


def seeder_projects(collection):
    projectstest = [
        {
            "name": "Project Alpha",
            "teams": get_item_by_attr(db['teams'], {"name": "Team Workers"}, fields={"_id":0,"pid":1}),
            "tags": ["urgent", "high-priority"],
            "budget": 10000,
            "deadline": datetime.datetime(2024, 12, 31)
        },
        {
            "name": "Project Beta",
            "teams": get_item_by_attr(db['teams'], {"name": "Team Admins"}, fields={"_id":0,"pid":1}),
            "tags": ["maintenance"],
            "budget": 5000,
            "deadline": datetime.datetime(2024, 11, 30)
        },
        {
            "name": "Project Gamma",
            "teams": get_item_by_attr(db['teams'], {"name": "Team Chiefs"}, fields={"_id":0,"pid":1}),
            "tags": ["research", "long-term"],
            "budget": 20000,
            "deadline": datetime.datetime(2025, 6, 30)
        },
        {
            "name": "Project Delta",
            "teams": get_item_by_attr(db['teams'], {"name": "Team Workers"}, fields={"_id":0,"pid":1}) + get_item_by_attr(db['teams'], {"name": "Team Admins"}, fields={"_id":0,"pid":1}),
            "tags": ["collaboration", "medium-priority"],
            "budget": 15000,
            "deadline": datetime.datetime(2024, 10, 15)
        }
    ]
    create_items(collection, projectstest)