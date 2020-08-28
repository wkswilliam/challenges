#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:40:14 2020

@author: william
"""
import time


for i in range(1,9):
    start = time.time()
    file = str(i)
    with open(f"test_input ({file}).txt") as f:
        inputs = f.read()
        inputs = inputs.split('\n')
        n, m = list(map(int, inputs[0].split(' ')))
        h = list(map(int, inputs[1].split(' ')))
        t = list(map(int, inputs[2].split(' ')))
    tickets = list(h)
    c_price = list(t)
    u_output = concert_tickets(n, m, h, t)
    
    with open(f"test_output ({file}).txt") as f:
        txt = f.read()
        output = txt
    
    print(start-time.time(), file)
    assert output==u_output


for i in range(1,9):
    start = time.time()
    file = str(i)
    with open(f"test_input ({file}).txt") as f:
        inputs = f.read()
        inputs = inputs.split('\n')
        n, m = list(map(int, inputs[0].split(' ')))
        h = list(map(int, inputs[1].split(' ')))
        t = list(map(int, inputs[2].split(' ')))
    tickets = list(h)
    c_price = list(t)
    u_out = '\n'.join(price_concert_tickets(tickets, c_price))
    with open(f"test_output ({file}).txt") as f:
        txt = f.read()
        output = txt
    for o, u, in zip(output.split('\n'), u_out.split('\n')):
        if o!=u:
            print(o,u)
    
    print(start-time.time(), file)
    
    
    
    
    
    
    
    
    
    


