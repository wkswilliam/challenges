#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 19:36:02 2020

@author: william
"""
from collections import Counter

def palindrome(string):
    string = sorted(string)
    cnt = Counter()
    for s in string:
        cnt[s]+=1
    res = ''
    odd = False
    odd_char = ''
    for s in cnt:
        if cnt[s]%2==1:
            res += s*int(cnt[s]//2)
            if odd:
                return "NO SOLUTION"
            else:
                odd = True
                odd_char = s
        else:
            res += s*int(cnt[s]/2)
    
    return res+odd_char+res[-1::-1]

      
def main():
    string = input()
    res = palindrome(string)
    print(res)
    return None

if __name__=="__main__":
    main()    
