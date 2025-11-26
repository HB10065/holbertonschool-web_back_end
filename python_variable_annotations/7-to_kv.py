#!/usr/bin/env python3
'''Module Doc'''
import typing
import math


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    sq: float = math.sqrt(v)
    return (k, sq)
