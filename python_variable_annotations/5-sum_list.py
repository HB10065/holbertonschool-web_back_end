#!/usr/bin/env python3
'''
Module Doc
'''
import typing


def sum_list(input_list: typing.List[float]) -> float:
    '''
    Function Doc
    '''
    sum: float = 0.00
    for element in input_list:
        sum += element

    return sum
