#!/usr/bin/env python3
'''
Module Doc
'''
import random, asyncio


async def wait_random(max_delay = 10.0):
    '''
    Function Doc
    '''
    num = random.random(0.0, max_delay)
    await asyncio.sleep(num)
    return num
