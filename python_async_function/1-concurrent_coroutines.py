#!/usr/bin/env python3
'''
Module Doc
'''
import asyncio
import importlib
import typing


wait_random = wait_random = importlib.import_module(
    '0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    '''
    Function Doc
    '''
    wait_list = []
    task = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for a in asyncio.as_completed(task):
        i = await a
        wait_list.append(i)

    return wait_list
