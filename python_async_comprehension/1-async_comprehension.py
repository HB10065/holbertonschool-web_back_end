#!/usr/bin/env python3
'''Module Doc'''
from typing import List
import importlib
async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Function Doc'''
    return [n async for n in async_generator()]
