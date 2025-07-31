#!/usr/bin/env python3
'''
Module Doc
'''
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    '''
    Function Doc
    '''
    def multi(n: float):
        '''
        Function doc
        '''
        return float(n * multiplier)
    
    return multi
