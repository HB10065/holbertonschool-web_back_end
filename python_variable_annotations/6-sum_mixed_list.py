#!/usr/bin/env python3
'''Module Doc'''
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    '''
    Takes a list of floats and ints and returns their sum
    '''
    list_sum: float = 0.0
    for num in mxd_lst:
        list_sum = list_sum + num

    return list_sum
