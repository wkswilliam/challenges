#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:17:30 2020

@author: william
"""
from collections import Counter

a = '??????R??????U??????????????????????????LD????D?'
s = 'DRURRRRRDDDLUULDDDLDRRURDDLLLLLURULURRUULDLLDDDD'

available_moves = {'D': 15, 'R': 12, 'U': 9, 'L': 12} # Starting from i=j=0
directions =['U', 'R', 'D', 'L']
cnt = Counter(a)

for k in directions:
    available_moves[k]-=cnt[k]
    
grid =[]
for i in range(7):
    line = []
    for j in range(7):
        line.append(a[6*i+j])
    grid.append(line)
    

i = j = 0

def choices(i, j):
    global available_moves
    U = (i-1,j, 'U')
    D = (i+1,j, 'D')
    L = (i,j-1, 'L')
    R = (i,j+1, 'R')
    arr = set([D, U, L, R])
    res = set()
    for a in arr:
        print(grid[a[0]][a[1]])
        if not(min(a[0:2])<0 or max(a[0:2])>6):
            res.add(a[2])
    _res = list(res)
    for k in _res:
        print(available_moves)
        if not available_moves[k]>0:
           res.discard(k)
    return res
    
def solve():
    pass