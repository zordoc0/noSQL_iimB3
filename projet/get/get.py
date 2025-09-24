from pymongo import MongoClient
import json

def get_item_by_attr(table, attributes, fields=None, pipeline=None):
    try:
        items = list(table.aggregate(pipeline)) if pipeline else list(table.find(attributes, fields))
        return items
    except Exception as e:
        print(f"Error getting item by attributes: {e}")
        return None

def get_item_by_pid(table, pid, fields=None):
    try:
        item = table.find_one({'pid': pid}, fields)
        return item
    except Exception as e:
        print(f"Error getting item by pid: {e}")
        return None

