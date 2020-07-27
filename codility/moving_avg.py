#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:54:17 2020

@author: william
"""

import random
import math

A = [random.randint(-10000, 10000) for _ in range(100000)]

def moving_avg(A, w):
    mean_min = math.inf
    index = 0
    for i, _ in enumerate(A[0:-w + 1]):
        new_mean = sum(A[i:i+w])/w
        if new_mean < mean_min:
            mean_min = new_mean
            index = i
    return mean_min, index

abs_min = math.inf
index = 0
for w in range(2, len(A)+1):
    v = moving_avg(A, w)
    print(w, v)
    if v[0] < abs_min:
        abs_min = v[0]
        index = v[1]