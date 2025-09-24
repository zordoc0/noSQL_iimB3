from pymongo import MongoClient
import json

def array_push_item_by_attr(table, attributes, array, new_item, updated_by=None):
    try:
        table.update_one(attributes, {'$push': {array: new_item}})
        return table.find_one(attributes)
    except Exception as e:
        print(f"Error pushing item to array by attributes: {e}")
        return None
    
def array_push_item_by_pid(table, pid, array, new_item, updated_by=None):
    try:
        attribute = {'pid': pid}
        table.update_one(attribute, {'$push': {array: new_item}})
        return table.find_one(attribute)
    except Exception as e:
        print(f"Error pushing item to array by pid: {e}")
        return None
    
def array_pull_item_by_attr(table, attributes, array, item_to_remove, updated_by=None):
    try:
        table.update_one(attributes, {'$pull': {array: item_to_remove}})
        return table.find_one(attributes)
    except Exception as e:
        print(f"Error pulling item from array by attributes: {e}")
        return None

def array_pull_item_by_pid(table, pid, array, item_to_remove, updated_by=None):
    try:
        attribute = {'pid': pid}
        table.update_one(attribute, {'$pull': {array: item_to_remove}})
        return table.find_one(attribute)
    except Exception as e:
        print(f"Error pulling item from array by pid: {e}")
        return None
    
