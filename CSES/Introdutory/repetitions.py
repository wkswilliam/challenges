#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 18:20:13 2020

@author: william
"""
def repetitions(s):
    prev = ''
    n_max = 0
    n = 0
    for c in s:
        if c == prev:
            n+=1
        else:
            prev = c
            n = 1
        if n > n_max:
            n_max = n
            
    return n_max

def main():
    s = input()
    res = repetitions(s)
    print(res)
    return None
    
if __name__=="__main__":
    main()