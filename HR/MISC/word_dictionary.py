#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:22:29 2020

@author: william
"""
import random
from collections import Counter
N = 20000
k = 10
force_bad = True
alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
#alphabet = 'a b c d e f'.split()
cnt = Counter()

random.seed(1)
words = [''.join(random.choices(alphabet, k=random.randint(3, k))) for _ in range(N)]
if force_bad:
    max_word = max(words, key=len)
    words.insert(0, max_word[0:3])
min_len = len(min(words, key=len))
for word in words:
    for i in range(min_len, len(word)+1):
        cnt[word[0:i]]+=1
        if cnt[word[0:i]]>1:
            print(word)
