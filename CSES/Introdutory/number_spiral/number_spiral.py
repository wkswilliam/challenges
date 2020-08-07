#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 12:12:50 2020

@author: william
"""
import math

def number_spiral(y, x):
    n = (max(x, y)-1)**2
    if y > x:
        if y%2==1:
            n+=x
        else:
            n = max(x, y)**2
            n = n - x + 1
    else:
        if x%2==0:
            n+=y
        else:
            n = max(x, y)**2
            n = n - y + 1
    return int(n)

        
def main():
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split(" "))
        print(number_spiral(x, y))
    return None

if __name__=="__main__":
    main()    
