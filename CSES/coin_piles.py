#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 17:50:59 2020

@author: william
"""

def coin_piles(a, b):
    if a > 0 and b > 0:
        if max(a,b)/min(a, b) > 2:
            res = False
        else:
            num = abs(a - 2*b)
            res = num%3==0
    else:
        res = (a==0 and b==0)
        
    return "YES" if res else "NO"
    
def main():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split(" "))
        res = coin_piles(a, b)
        print(res)
    return None

if __name__=="__main__":
    main()    
