#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 18:33:02 2020

@author: william
"""
def increasing_array(size, array):
    n = 0
    for i in range(1, size):
        v = max(array[i-1]-array[i], 0)
        n+= v
        array[i] += v 
    return n

def main():
    size = int(input())
    array = list(map(int, input().split()))
    res = increasing_array(size, array)
    print(res)
    return None
    
if __name__=="__main__":
    main()
        
    