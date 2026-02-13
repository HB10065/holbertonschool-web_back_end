#!/usr/bin/env python3
'''Documentation'''


def insert_school(mongo_collection, **kwargs):
    '''Documentation'''
    insert = mongo_collection.insert_one(kwargs)
    return insert.inserted_id
