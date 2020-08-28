#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 12:12:40 2020

@author: william
"""
from math import ceil
from collections import Counter

def dice_combinations(n):
    total=0
    for t in range(ceil(n/6),n+1):
        aux = total
        total+= count(t, 6, n)
        
    return total

triplets_add = set()
def count(n, k, _sum):
    res = 0
    for i in range(1, k + 1):
        if (n-1, k, _sum-i) in triplets_add:
            res+=1
        else:
            if n - 1 == 0 and _sum - i == 0:
                triplets_add.add((n, k, _sum))
                res+=1
                break
            elif _sum-i > 0 and n-1 > 0:# and n - 1 > _sum -i:
                if not (n-1 > _sum-i):
                    res += count(n - 1, k, _sum - i)

    return res



def Solution(n):
    arr = [0]*(n+1)
     
    for i in range(0,n+1):
    	if i == 0:
    		arr[0] = 1
    	
    	elif i<6:
    		for j in range(0,i):
    			arr[i]+=arr[j]
    	
    	else:
    		arr[i] = (arr[i-1]+arr[i-2]+arr[i-3]+arr[i-4]+arr[i-5]+arr[i-6])%(10**9+7)
     
    return arr[n]%(10**9+7)

def main():
    n = int(input())
    res = dice_combinations(n)
    print(res)
    return None

if __name__ == '__main__':
   main()