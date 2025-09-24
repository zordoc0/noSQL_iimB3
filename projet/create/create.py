from pymongo import MongoClient
import json
import uuid
import datetime

def create_item(table, item, created_by=None):
    try:
        pid = str(uuid.uuid4())
        item['pid'] = pid
        item['created_at'] = datetime.datetime.now()
        item['updated_at'] = item['created_at']
        if created_by:
            item['created_by'] = created_by
        result = table.insert_one(item)
        return result.inserted_id
    except Exception as e:
        print(f"Error creating item: {e}")
        return None

def create_items(table, items, created_by=None):
    try:
        for item in items:
            pid = str(uuid.uuid4())
            item['pid'] = pid
            item['created_at'] = datetime.datetime.now()
            item['updated_at'] = item['created_at']
            if created_by:
                item['created_by'] = created_by
        result = table.insert_many(items)
        return result.inserted_ids
    except Exception as e:
        print(f"Error creating items: {e}")
        return None
