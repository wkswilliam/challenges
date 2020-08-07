#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 18:09:47 2020

@author: william
"""


def missing_number(n, numbers):
    res = (set(range(1, n+1))-numbers).pop()
    print(res)
    return None

def main():
    n = int(input())
    numbers = set(map(int, input().split()))
    missing_number(n, numbers)
    return None
    
if __name__=="__main__":
    main()