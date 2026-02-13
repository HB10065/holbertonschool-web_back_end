#!/ust/bin/env python3
'''Documentation'''


def update_topics(mongo_collection, name, topics):
    '''Update
    '''
    return mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
