#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:59:58 2020

@author: william
"""



def check_input():
    df = pd.read_csv("test_input.txt", sep=" ", skiprows=1, names=['x', 'y'])
    df_out = pd.read_csv("test_output.txt", sep=" ", names=['output'])
    res = []
    for index, row in df.iterrows():
        break
        res.append(df_out.at[index, 'output'] == number_spiral(row['x'], row['y']))
        if index%1000==0:
            print(100*index/len(df), 'status ', 100*sum(res)/len(res))
        
    return sum(res)/len(res)


o = 889344698385097940
o == number_spiral(row['y'], row['x'])