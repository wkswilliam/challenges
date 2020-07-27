#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 21:09:53 2020

@author: william
"""


def prod_int(array:list) -> int:
    p = 1
    for v in array:
        p *= v
        
    return p


A = []
A = [[10,100,10],[1,10,1],[1,10,1]]
A = [[20,300,30],[4,40,6],[7,8,9]]
prod_int(A)

def solution(A: list) -> int:
    n_rows = len(A)
    n_cols = len(A[0])
    
    for i, row in enumerate(A):
        for j, v in enumerate(row):
            
