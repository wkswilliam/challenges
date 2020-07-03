#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 18:34:01 2020

@author: william
"""
from collections import Counter  
import networkx as nx


class QuickUnion():
    def __init__(self, N=1): 
        self.array = [i for i in range(N)]
        self.size = N
        return None
    
    def __str__(self):
        return str(self.array[0:20])
    
    def __repr__(self):
        return '{0}, {1}'.format(self.__class__, self.__dict__)
    
    def root(self, i):
        if not i < self.size:
            raise IndexError('Node must be valid')
        while self.array[i]!=i:
            i = self.array[i]
        
        return i
    
    def distance_to_root(self, i):
        if not i < self.size:
            raise IndexError('Node must be valid')
        size = 0
        while self.array[i]!=i:
            i = self.array[i]
            size+=1
        
        return size
    
    def union(self, p, q):
        if not q < self.size or not p < self.size:
            raise IndexError('Nodes must be valid')

        i = self.root(p)
        j = self.root(q)
        i_size = self.distance_to_root(p)
        j_size = self.distance_to_root(q)
        if i_size > j_size:
            self.array[j] = i
        else:
            self.array[i] = j
        return None
    
    def number_of_roots(self):
        total = 0
        for i, v in enumerate(self.array):
            if i == v:
                total+=1
        
        return total

def getMinConnectionChange(connection):
    # Write your code here
    connection = [i-1 for i in connection]
    quick_union = QuickUnion(len(connection))
    for i, node in enumerate(connection):
        quick_union.union(i, node)
    return quick_union.number_of_roots() - 1

if __name__=="__main__":
    for filenumber in range(0,20):
        with open(f'input/input{str(filenumber).zfill(2)}.txt') as f:
            lines = f.read().split('\n')
            n = int(lines[0].split(' ')[0])
            line_1 = lines[1].split(' ')
            while '' in line_1:
                line_1.remove('')
            connection = list(map(int, line_1))
            
        with open(f'output/output{str(filenumber).zfill(2)}.txt') as f:
            output = int(f.read())
        res = getMinConnectionChange(connection)
        print(filenumber, res, output, res==output)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    