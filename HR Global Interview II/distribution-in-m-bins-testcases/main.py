#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:08:44 2020

@author: william
"""


def maxScore(a, m):
    # Write your code here
    a.sort()
    total = 0
    index = 0
    for container in range(len(a)//m):
        for _ in range(m):
            total +=(container+1)*a[index]
            index+=1
    for v in a[index:]:
        total+=v*(container+1)

    return total%(10**9+7)

if __name__=="__main__":
    for filenumber in range(15):
        with open(f'input/input{str(filenumber).zfill(2)}.txt') as f:
            lines = f.read().split('\n')
            n = int(lines[0].split(' ')[0])
            m = int(lines[0].split(' ')[1])
            line_1 = lines[1].split(' ')
            while '' in line_1:
                line_1.remove('')
            a = list(map(int, line_1))
            
        with open(f'output/output{str(filenumber).zfill(2)}.txt') as f:
            output = int(f.read())
        res = maxScore(a,m)
        print(filenumber, res, output, res==output)
    