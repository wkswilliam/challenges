#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:50:35 2020

@author: william
"""
'''
home key represented by '<'
end key represented by '>'
backspace key represented by '*'
numeric key represented by '#'
'''

import random

S = "HE*<LL>O#1234<william**>#987#123#888**********<***"
receivedText(S)
def receivedText(S):
    # WRITE DOWN YOUR CODE HERE
    ans = []
    pointer = -1
    numlock = True
    head = False
    for s in S:
        print(pointer)
        if s == '<':
            pointer = 0
            head = True
        elif s == '>':
            pointer = -1
            head = False
        elif s == '*':
            if head:
                if pointer>0:
                    ans.pop(pointer-1)
                    pointer-=1
            else:
                ans.pop(-1)
        elif s == '#':
            numlock = not numlock
        else:
            if head:
                if s.isalpha():
                    ans.insert(pointer, s)
                    pointer+=1
                elif numlock:
                    ans.insert(pointer, s)
                    pointer+=1
            else:
                if s.isalpha():
                    ans.append( s)
                    pointer=-1
                elif numlock:
                    ans.append( s)
                    pointer=-1
            
    return ''.join(ans)
        