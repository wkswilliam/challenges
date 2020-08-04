#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:17:23 2020

@author: william
"""

def trailing_zeros(n):
    v = 5
    res = 0
    while v <= n:
        res += n//v
        v*=5
    return res

       
def main():
    n = int(input())
    res = trailing_zeros(n)
    print(res)
    return None

if __name__=="__main__":
    main()    
            
    