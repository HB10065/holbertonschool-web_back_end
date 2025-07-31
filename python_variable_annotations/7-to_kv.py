#!/usr/bin/env python3
'''
Module Doc
'''
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    '''
    Function Doc
    '''
    return (k, float(v))
