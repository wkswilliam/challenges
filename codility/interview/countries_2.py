#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 10:59:07 2020

@author: william
"""

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
     [1,2,1],
     [1,2,1],
     [1,2,1],
     [1,1,1],
     [1,1,1],
     [1,1,1],
     [1,1,1],
     [1,1,1],
     [1,1,1],
     [1,1,1],
     [1,1,1],
     [1,1,1],
     [1,1,1],
     [1,1,1]]



def solution(A: list) -> int:
    n_rows = len(A)
    n_cols = len(A[0])
    countries = 0
    
    prev_row = [0]*n_cols
    

    i = -1
    
    
    i+=1
    row = A[i]
    
    for i, row in enumerate(A):
        new_countries = list(row)
        for j, v in enumerate(row):
            if v == prev_row[j]:
                new_countries[j] = 0
                _j = j
                while new_countries[max(0, _j-1)]==v:
                    new_countries[_j-1]=0
                    _j-=1
                _j = j
                while new_countries[min(n_cols - 1, _j+1)]==v:
                    new_countries[_j+1]=0
                    _j+=1
                    
        new_countries = set(new_countries)
        new_countries.discard(0)
        prev_row = row
        countries += len(new_countries)
        print(i, countries)
        break