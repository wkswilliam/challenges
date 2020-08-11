#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:18:54 2020

@author: william
"""
def ferris_wheel(n, x, weight):
    weight.sort(reverse=True)
    # x maximum wei
    head = 0
    tail = n -1
    count = 0
    while head <= tail:
        if weight[head] + weight[tail]<=x:
            count+=1
            head+=1
            tail-=1
        else:
            count+=1
            head+=1
    return count
            
def main():
    n, x = map(int, input().split(" "))
    p = list(map(int, input().split(" ")))
    res = ferris_wheel(n, x, p)
    print(res)
    return None

if __name__=="__main__":
    main()