#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:32:50 2020

@author: william
"""
def apartments(clients, n, ap, m, k):
    clients.sort()
    ap.sort()
    count = 0
    i = 0
    j = 0
    while i<n and j < m:
        if clients[i] + k < ap[j]: 
            i += 1
        elif clients[i] - k > ap[j]:
            j += 1
        else:
            i += 1;
            j += 1;
            count += 1
    return count

def main():
    n, m, k = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    res = apartments(a, n, b, m, k)
    print(res)
    return None

if __name__=="__main__":
    main()