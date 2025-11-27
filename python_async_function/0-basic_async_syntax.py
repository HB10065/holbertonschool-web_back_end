#!/usr/bin/env python3
'''Module Doc'''
import random, asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''an async function that has a random delay and returns said delay'''
    dealyed = random.uniform(0, max_delay)
    await asyncio.sleep(dealyed)

    return dealyed
