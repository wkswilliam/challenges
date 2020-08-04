#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:26:15 2020

@author: william
"""


def bit_strings(n):
    return (2**n)%1000000007
        
def main():
    n = int(input())
    res = bit_strings(n)
    print(res)
    return None

if __name__=="__main__":
    main()    
