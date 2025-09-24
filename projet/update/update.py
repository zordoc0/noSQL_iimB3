from pymongo import MongoClient
import json
import datetime

def update_item_by_attr(table, attribute, item_data, updated_by=None):
    try:
        table.update_one(attribute, {'$set': item_data})
        table.update_one(attribute, {'$set': {'updated_at': datetime.datetime.now()}})
        return table.find_one(attribute)
    except Exception as e:
        print(f"Error updating item by attributes: {e}")
        return None 

def update_item_by_pid(table, pid, item_data, updated_by=None):
    try:
        attribute = {'pid': pid}
        table.update_one(attribute, {'$set': item_data})
        table.update_one(attribute, {'$set': {'updated_at': datetime.datetime.now()}})
        return table.find_one(attribute)
    except Exception as e:
        print(f"Error updating item by pid: {e}")
        return None

def update_items_by_attr(table, attributes, items_datas, updated_by=None):
    try:
        for item_data in items_datas:
            table.update_many(attributes, {'$set': item_data})
            table.update_many(attributes, {'$set': {'updated_at': datetime.datetime.now()}})
        return list(table.find(attributes))
    except Exception as e:
        print(f"Error updating items by attributes: {e}")
        return None

def update_items_by_pids(table, pids, items_datas, updated_by=None): 
    try:
        for pid, item_data in zip(pids, items_datas):
            attribute = {'pid': pid}
            table.update_one(attribute, {'$set': item_data})
            table.update_one(attribute, {'$set': {'updated_at': datetime.datetime.now()}})
        return list(table.find({'pid': {'$in': pids}}))
    except Exception as e:
        print(f"Error updating items by pids: {e}")
        return None

