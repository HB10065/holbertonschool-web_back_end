#!/usr/bin/env python3
'''
Module Doc
'''
import asyncio
import importlib
import typing
task_wait_random = importlib.import_module('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    '''
    Function Doc
    '''
    task = [task_wait_random(max_delay) for _ in range(n)]
    i = await asyncio.gather(*task)
    return sorted(i)
