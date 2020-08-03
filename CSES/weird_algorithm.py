#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:47:25 2020

@author: william
"""

def weird_algorithm(n):
    if n == 1:
        print(f'{int(n)}', end=' ')
        return None
    if n%2==0:
        #even
        print(f'{int(n)}', end=' ')
        weird_algorithm(n/2)
    else:
        #odd
        print(f'{int(n)}', end=' ')
        weird_algorithm(n*3 +1)

def main():
    n = int(input())
    weird_algorithm(n)
    
    return None

if __name__=="__main__":
    main()    