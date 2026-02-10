#!/usr/bin/env python3
'''
Docstring for pagination.0-simple_helper_function
'''


def index_range(page, page_size):
    '''
    Docstring for index_range
    '''
    if page < 1:
        raise ValueError('page must be greater than 0')
    if page_size < 1:
        raise ValueError('page_size must be greater than 0')

    return ((page - 1) * page_size, page * page_size)
