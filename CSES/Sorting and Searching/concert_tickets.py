#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:50:24 2020

@author: william
"""
from collections import Counter
from bisect import bisect_right
from sortedcontainers import SortedSet

def binary_search(arr, v):
    n = len(arr)
    L = 0
    R = n - 1
    while L <= R:
        m = int((L + R) / 2)
        if arr[m] < v:
            L = m + 1
        elif arr[m] > v:
            R = m - 1
        else:
            return arr[m]
    return arr[m]

def concert_tickets(n, m, tickets, c_price):
    tickets.sort()
    cnt = Counter(tickets)
    res = ''
    for c in c_price:
        p = binary_search(list(cnt.keys()), c)
        if cnt[p] == 0 or p > c:
            res+='-1\n'
        else:
            res+= str(p) + '\n'
            cnt[p]-=1
            if cnt[p] == 0:
                cnt.pop(p)
    return res


def concert_tickets(n, m, tickets, c_price):
    tickets.sort()
    cnt = Counter(tickets)
    t_values = SortedSet(cnt.keys())
    t_values.add(-1)
    res = ''
    for c in c_price:
        i = t_values.bisect_right(c) - 1
        if t_values[i] <= c:
            p = t_values[i]
        else:
            i = i-1
            p = t_values[i]
        if cnt[p] == 0:
            res+='-1\n'
        else:
            res+= str(p) + '\n'
            cnt[p]-=1
            if cnt[p] == 0:
                cnt.pop(p)
                t_values.pop(i)
    return res


 
def price_concert_tickets(ticket_price, customer_price):
    prices = []
    ticket_price.sort()
    ticket_dsu = list(range(len(ticket_price) + 1))
    for price in customer_price:
        break
        i = j = bisect_right(ticket_price, price)
        while ticket_dsu[i] != i:
            i = ticket_dsu[i]
        while j != i:
            ticket_dsu[j], j = i, ticket_dsu[j]
        if i:
            prices.append(str(ticket_price[i - 1]))
            ticket_dsu[i] = i - 1
        else:
            prices.append(str(-1))
    return prices

def main():
    n, m = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    res = concert_tickets(n, m, a, b)
    print(res)
    return None

if __name__=="__main__":
    main()