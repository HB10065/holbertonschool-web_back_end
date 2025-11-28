#!/usr/bin/env python3
'''Module Doc'''
import random
import asyncio


async def async_generator():
    '''Function Doc'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
