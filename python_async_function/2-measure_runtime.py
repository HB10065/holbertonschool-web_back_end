#!/usr/bin/env python3
'''
Module Doc
'''
import asyncio
import importlib
import time
wait_n = wait_random = importlib.import_module(
    '1-concurrent_coroutines.py').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Function Doc
    '''
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return ((end - start) / n)
