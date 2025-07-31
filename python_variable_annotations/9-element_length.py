#!/usr/bin/env python3
'''
Module Doc
'''
import typing


def element_length(lst: typing.Iterable[typing.Sequence]
                   ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    '''
    Function Doc
    '''
    return [(i, len(i)) for i in lst]
