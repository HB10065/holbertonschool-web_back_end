#!/usr/bin/env python3
'''Module Doc'''
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    def inner(x: float) -> float:
        return x * multiplier
    return inner()
