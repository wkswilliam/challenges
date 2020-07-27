#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:54:40 2020

@author: william
"""
import math
import numpy as np
import random
from itertools import combinations



def play():
    board = [['','',''],
             ['','',''],
             ['','','']]
    available = [(0,0),(0,1),(0,2),
                 (1,0),(1,1),(1,2),
                 (2,0),(2,1),(2,2)]
    random.choices(available) 

def winner(arr):
    arr = np.array(arr)
    return (arr=='X').all() or (arr=='O').all()
    

def check_winner(board):
    # Line and Column
    for i in range(3):
        line = board[i]
        column = []
        for j in range(3):
            column.append(board[j][i])
        if winner(line) or winner(column):
            return True
    # Diagonals
    d_1 = [board[0][0],board[1][1],board[2][2]]
    d_2 = [board[0][2],board[1][1],board[2][0]]
    
    return winner(d_1) or winner(d_2)


def rotate_board(board):
    sequece = [(0,0),(0,1),(0,2),
               (1,2),(2,2),(2,1),
               (2,0),(1,0),(0,0)]
    _board = [['','',''],
              ['',board[1][1],''],
              ['','','']]
    for i, v in enumerate(sequece[0:-1]):
        _v = sequece[i+1]
        _board[_v[0]][_v[1]] = board[v[0]][v[1]]
        
    return _board

def flip_horizontal(board):
    # line
    _board = [board[2],
              board[1],
              board[0]]
    return _board
    
def flip_vertical(board):
    _board = [[board[0][2],board[0][1],board[0][0]],
              [board[1][2],board[1][1],board[1][0]],
              [board[2][2],board[2][1],board[2][0]]]    
    return _board

if __name__=="__main__":
    all_boards = []
    flip_switch = {1:flip_horizontal,
                   0:flip_vertical}
    
    board_init = [['1','2','3'],
                 ['4','5','6'],
                 ['7','8','9']]
    all_boards.append(board_init)
    board = board_init
    for n_rotations in range(8):
        board = rotate_board(board)
        if not board in all_boards:
            all_boards.append(board)
    
        for n_flip in range(4):
            board = flip_switch[n_flip%2](board)
            if not board in all_boards:
                all_boards.append(board)

