#!/usr/bin/env python3
'''Module Documentation'''


def list_all(mongo_collection):
    '''Lists all documents of a collection
    '''
    return list(mongo_collection.find())
