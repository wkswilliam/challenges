#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:50:05 2020

@author: william
"""

def two_sets(n):
    if (n+1)%4==0 or n%4==0 or n==3:
        print("YES")
        th1 = 0
        th2 = 1 if n%4==0 else 3
        seq_1 = []
        seq_2 = []
        for i in range(n+1):
            if i>0:
                if i%4 == th1 or i%4 == th2:
                    seq_1.append(str(i))
                else:
                    seq_2.append(str(i))
        print(len(seq_1))
        print(' '.join(seq_1))
        print(len(seq_2))
        print(' '.join(seq_2))
    else:
        print("NO")
    return None
     
def main():
    n = int(input())
    res = two_sets(n)
    print(res)
    return None

if __name__=="__main__":
    main()    
