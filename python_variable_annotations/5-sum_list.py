#!/usr/bin/env python3
'''Module Doc'''
import typing


def sum_list(input_list: typing.List[float] = []) -> float:
    '''
    Takes a list of floats and returns their sum
    '''
    list_sum: float = 0.0
    for num in input_list:
        list_sum = list_sum + num

    return list_sum
