#!/usr/bin/env python3
'''
Module Doc
'''
import random
import asyncio
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    '''
    Function Doc
    '''
    for _ in range(10):
        asyncio.sleep(1)
        yield random.uniform(0, 10)
