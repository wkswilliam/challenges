#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:15:45 2020

@author: william
"""
from itertools import combinations

def apple_division(n, weights):
    total_sum = sum(weights)
    _min = total_sum
    for r in range(1,n//2 +1):
        for elem in combinations(weights, r):
            aux = abs(total_sum-2*sum(elem))
            if aux <= _min:
                _min = aux
    return _min

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    res = apple_division(n, weights)
    print(res)
    return None
    
if __name__=="__main__":
    main()