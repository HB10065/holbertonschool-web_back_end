#!/usr/bin/env python3
'''
Module Doc
'''
import typing
import importlib
async_generator = importlib.import_module('0-async_generetor.py').async_generator


async def async_comprehension() -> typing.List[float]:
    '''
    Function Doc
    '''
    gen_list = [i async for i in async_generator()]

    return gen_list
