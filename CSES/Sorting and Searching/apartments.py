#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:32:50 2020

@author: william
"""
def apartments(clients, ap, k):
    count = 0
    for c in clients:
        for a in ap:
            if a+k>=c and a-k<=c:
                count+=1
                ap.remove(a)
    return count
    
    


def main():
    n, m, k = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    res = apartments(a, b, k)
    print(res)
    return None

if __name__=="__main__":
    main()