#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 10:59:07 2020

@author: william
"""

A = [[5,4,4],[4,3,4],[3,2,4],[2,2,2],[3,3,4],[1,4,4],[4,1,1]]

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

A = [[1,1,1],
     [1,1,1],
     [1,1,1]]


def solution(A: list) -> int:
    
    def pop_connected(index):
        i = index[0]
        j = index[1]
        v = A[i][j]
        A[i][j] = -1
        v_W = A[i][max(0, j-1)]
        if v == v_W and j!=max(0, j-1):
            A[i][max(0, j-1)] = -1
            indexes.discard((i,max(0, j-1)))
            pop_connected((i, max(0, j-1)))
        v_E = A[i][min(len(A[0])-1, j+1)]
        if v == v_E and j!=min(len(A[0])-1, j+1):
            A[i][min(len(A[0])-1, j+1)] = -1
            indexes.discard((i,min(len(A[0])-1, j+1)))
            pop_connected((i, min(len(A[0])-1, j+1)))
        v_S = A[min(len(A)-1, i+1)][j]
        if v == v_S and i!=min(len(A)-1, i+1):
            A[min(len(A)-1, i+1)][j] = -1
            indexes.discard((min(len(A)-1, i+1),j))
            pop_connected((min(len(A)-1, i+1), j))
        v_N = A[max(0, i-1)][j]
        if v == v_N and i!=max(0, i-1):
            A[max(0, i-1)][j] = -1
            indexes.discard((max(0, i-1),j))
            pop_connected((max(0, i-1), j))
        
        return None
        
        
    n_rows = len(A)
    n_cols = len(A[0])
    countries = 0
    
    indexes = set()
    for i in range(n_rows):
        for j in range(n_cols):
            indexes.add((i, j)) 
    
    while indexes:
        index = indexes.pop()
        countries+=1
        pop_connected(index)
        break
        print(indexes)

    return countries