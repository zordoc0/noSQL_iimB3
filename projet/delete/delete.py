from pymongo import MongoClient
import json


def delete_item_by_attr(table, attributes):
    try:
        result = table.delete_one(attributes)
        return result
    except Exception as e:
        print(f"Error deleting item by attributes: {e}")
        return False

def delete_item_by_pid(table, pid):
    try:
        result = table.delete_one({'pid': pid})
        return result
    except Exception as e:
        print(f"Error deleting item by pid: {e}")
        return False

def delete_items_by_attr(table, attributes):
    try:
        result = table.delete_many(attributes)
        return result
    except Exception as e:
        print(f"Error deleting items by attributes: {e}")
        return False
    
def delete_items_by_pids(table, pids):
    try:
        result = table.delete_many({'pid': {'$in': pids}})
        return result
    except Exception as e:
        print(f"Error deleting items by pids: {e}")
        return False
