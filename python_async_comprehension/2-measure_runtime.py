#!/usr/bin/env python3
'''Module Doc'''
import asyncio
import time
import importlib
async_comprehension = (
    importlib.import_module('1-async_comprehension').async_comprehension
)


async def measure_runtime() -> float:
    '''Function Doc'''
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    total = end - start
    return total
