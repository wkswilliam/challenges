#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:44:49 2020

@author: william
"""
def distinct_numbers(arr):
    return len(set(arr))

 
def main():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    res = distinct_numbers(arr)
    print(res)
    return None

if __name__=="__main__":
    main()    