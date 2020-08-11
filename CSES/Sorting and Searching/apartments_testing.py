#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:31:25 2020

@author: william
"""
from apartments import *

with open("test_input.txt") as f:
    txt = f.read()
    lines = txt.split('\n')

n, m, k = map(int, lines[0].split(" "))
a = list(map(int, lines[1].split(" ")))
b = list(map(int, lines[2].split(" ")))
res = apartments(a, n, b, m, k)

with open("test_output.txt") as f:
    txt = f.read()
    output = int(txt.split('\n')[0])

assert res==output
   
