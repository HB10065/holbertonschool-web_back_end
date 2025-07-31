#!/usr/bin/env python3
'''
Module Doc
'''
import random, asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    Function Doc
    '''
    num = random.uniform(0.0, max_delay)
    await asyncio.sleep(num)
    return num
