from pymongo import MongoClient
import json

def get_items(table, attributes, fields=None, sort=None, skip=0, limit=None,return_stats=False, pipeline=None):
    try:
        if pipeline:
            items = list(table.aggregate(pipeline))
            count = len(items)
        else:
            cursor = table.find(attributes, fields)
            if sort:
                cursor = cursor.sort(sort)
            if skip:
                cursor = cursor.skip(skip)
            if limit:
                cursor = cursor.limit(limit)
            items = list(cursor)
            count = table.count_documents(attributes)
        
        if return_stats:
            return {
                "count": count,
                "items": items
            }
        return items
    except Exception as e:
        print(f"Error getting items: {e}")
        return None