#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 18:49:53 2020

@author: william
"""

def permutations(n):
    if n == 1:
        return str(n)
    if n < 4:
        return "NO SOLUTION"
    else:
        lower = [str(i) for i in range(n-1,0,-2)] 
        upper = [str(i) for i in range(n,0,-2)] 
        return " ".join(lower+upper)
        
def main():
    n = int(input())
    res = permutations(n)
    print(res)
    return None

if __name__=="__main__":
    main()    