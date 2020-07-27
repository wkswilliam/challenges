#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:28:19 2020

@author: william
"""
from collections import Counter
import random

A = [random.randint(0, 1) for _ in range(100)]
MAX_PAIRS = 1000000
A = [0,1,0,1,1]
solution(A)
solution_2(A)
def solution_2(A):
    """
    :param A: array of int (0 or 1 which are actually booleans)
    :return: integer count of pairs of passing cars, or -1 if more than 1e9 pairs
    """
    cnt = Counter()
    for i, car in enumerate(A):
        if not bool(car):
            cnt[i] = 0
        else:
            cnt.update(cnt.keys())
            cnt
        if sum(cnt.values()) > MAX_PAIRS:
            return -1
        
    return sum(cnt.values())



def solution(A):
    """
    :param A: array of int (0 or 1 which are actually booleans)
    :return: integer count of pairs of passing cars, or -1 if more than 1e9 pairs
    """
    east = 0
    pairs = 0
    for car in A:
        if not bool(car):
            east += 1
        else:
            pairs += east
        if pairs > MAX_PAIRS:
            return -1
    return pairs