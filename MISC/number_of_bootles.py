#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 20:18:08 2020

@author: william
"""


def number_of_bottles(n, exchange):
    ans = 0 
    ne = 0
    while n >= exchange:
        ne += n
        ans+=n
        n = 0
        n+=ne//exchange
        ne-= n*exchange
    
    return ans + n


number_of_bottles(1123909, 2)