#!/usr/bin/env python3
'''
Module Doc
'''
import typing


def element_length(lst: typing.List) -> typing.Tuple[typing.Any, int]:
    '''
    Function Doc
    '''
    return [(i, len(i)) for i in lst]
