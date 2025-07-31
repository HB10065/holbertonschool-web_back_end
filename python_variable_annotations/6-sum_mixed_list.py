#!/usr/bin/env python3
'''
Module Doc
'''
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    '''
    Function Doc
    '''
    sum: float = 0.00
    for element in mxd_lst:
        sum += element

    return sum
