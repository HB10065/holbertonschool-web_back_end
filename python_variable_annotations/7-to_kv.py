#!/usr/bin/env python3
'''Module Doc'''
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    '''returns tuple of the given string and the square of the given number'''
    return (k, v ** 2.0)
