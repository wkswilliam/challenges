#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:54:18 2020

@author: william
"""

# Needs brute force

string = """........
........
..*.....
........
........
.....**.
...*....
........"""
from collections import Counter

def build_chessboard(string):
    chessboard = []
    for line in string.split():
        chessboard.append(list(line))
    
    return chessboard

chessboard = build_chessboard(string)

cnt = Counter()
for line in chessboard:
    cnt += Counter(line)

# q1 = 0 0 
# q2 = 1 2  
# q3 = 2 1
# q4 = 5 3
# q5 = 7 4
# q6 = 3 5
i = 3
j = 5
q = 'q6'
place_queen(q,i,j)
chessboard[i][j] = q.upper()
chessboard
def place_queen(q,i,j):
    b = i-j
    for ii in range(8):
        chessboard[i][ii] = q
        chessboard[ii][j] = q
        if ii+b<8 and ii+b>0:
            chessboard[ii+b][ii] = q
        for line in chessboard:
            print(line)
             
all_sets = set()
for line in chessboard:
    aux_set = set(line)
    all_sets = all_sets.union(aux_set)
    