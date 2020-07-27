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


class TicTacToe():
    
    def __init__(self, player=False):
        self.player = player
        self.board = [[None,None,None],
                     [None,None,None],
                     [None,None,None]]
        self.available = [(0,0),(0,1),(0,2),
                         (1,0),(1,1),(1,2),
                         (2,0),(2,1),(2,2)]
    
    def check_valid_player_input(self, p):
        try:
            m = tuple(map(int, p.split(',')))
        except:
            print("Please Provide a valid input.")
            return True
        if m in self.available:
            self.board[m[0]][m[1]] = True
            self.available.remove(m)
            return False
        else:
            return True
    
    def check_winner(self):
        def winner(arr):
            arr = np.array(arr)
            return (arr==False).all() or (arr==True).all()
        # Line and Column
        for i in range(3):
            line = self.board[i]
            column = []
            for j in range(3):
                column.append(self.board[j][i])
            if winner(line) or winner(column):
                print("Winner")
                return True
        # Diagonals
        d_1 = [self.board[0][0],self.board[1][1],self.board[2][2]]
        d_2 = [self.board[0][2],self.board[1][1],self.board[2][0]]
        
        return winner(d_1) or winner(d_2)
    
    def play(self):
        self.reset_board()
        while self.available:
            while self.player:
                print("Moves available: ", self.available)
                p = input('Give a valid cordinate, ex: "1, 1" (if available)')
                self.player = self.check_valid_player_input(p)
                if self.check_winner():
                    return "player O wins"
                elif not self.available:
                    return "Draw"
            m = random.choices(self.available)[0] 
            self.available.remove(m)
            self.board[m[0]][m[1]] = self.player
            self.player = not self.player
            self.print_board()
            if self.check_winner():
                return "player X wins"
            
        return "Draw"
    
    def print_board(self):
        for line in self.board:
            line_str = str(line)
            line_str = line_str.replace('False', 'X')
            line_str = line_str.replace('True', 'O')
            line_str = line_str.replace('None', '_')
            print(line_str)
        return None
    
    def reset_board(self):
        self.board = [[None,None,None],
                     [None,None,None],
                     [None,None,None]]
        self.available = [(0,0),(0,1),(0,2),
                         (1,0),(1,1),(1,2),
                         (2,0),(2,1),(2,2)]
        

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


def main():
    ttt = TicTacToe()
    p_input  = 'yes'
    while p_input == 'yes':
        result = ttt.play()
        print(result)
        print("-"*20)
        p_input = input("Play again? (yes, no)").lower()
        print("-"*20)
        
    
if __name__=="__main__":
    main()
    