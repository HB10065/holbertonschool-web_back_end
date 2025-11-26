#!/usr/bin/env python3
'''Module Doc'''
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    '''takes a number and returns a function that multiplies a
    number by the given number'''
    def inner(x: float) -> float:
        return x * multiplier
    return inner
