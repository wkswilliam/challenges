#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:42:12 2020

@author: william
"""

import random

N = 1000
M = 1000
T = 5
A = [[random.randint(1, T) for _ in range(M)] for _ in range(N)]


for t in range(1, T+1):
    print("##############")
    print(t)
    print('\n')
    for r in A:
        aux = []
        for v in r:
             if v == t:
                 aux.append('#')
             else:
                 aux.append('O')
        print(''.join(aux))

A = [[5,4,4],
     [4,3,4],
     [3,2,4],
     [2,2,2],
     [3,3,4],
     [1,4,4],
     [4,1,1]]

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]


A = [[1,2,1],
     [1,2,2],
     [1,1,1]]

A = [[1,2,1],
     [1,2,1],
     [1,2,3],
     [1,2,1],
     [1,2,3],
     [1,2,1],
     [1,2,1],
     [1,1,1],
     [1,1,1],
     [1,1,1],
     [1,1,1],
     [1,1,1],
     [1,1,1],
     [1,1,1],
     [1,1,1]]

solution(A)


def solution(A: list) -> int:
    def get_all_nodes(v, i, j):
        visited_indexes.add((i, j))
        try:
            if i<(n_rows -1) and not (i+1, j) in visited_indexes:
                v_n = A[i+1][j]
                if v == v_n:
                    get_all_nodes(v, i+1, j)
        except IndexError:
            pass
        try:
            if j<(n_cols - 1) and not (i, j+1) in visited_indexes:
                v_n = A[i][j+1]
                if v == v_n:
                    get_all_nodes(v, i, j+1)
        except IndexError:
            pass
        
        try:
            if i>0 and not (i-1, j) in visited_indexes:
                v_n = A[i-1][j]
                if v == v_n:
                    get_all_nodes(v, i-1, j)
        except IndexError:
            pass
        try:
            if j>0 and not (i, j-1) in visited_indexes:
                v_n = A[i][j-1]
                if v == v_n:
                    get_all_nodes(v, i, j-1)
        except IndexError:
            pass
    
    n_rows = len(A)
    n_cols = len(A[0])
    countries = 0
    visited_indexes = set()
    
    for i, row in enumerate(A):
        for j, v in enumerate(row):
            if not (i, j) in visited_indexes:
                get_all_nodes(v, i, j)
                countries+=1
    return countries
            
            
            
            
            
            
            
            
            
            
            
            