# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:16:39 2021

"""
 def sockMerchant(n, ar):
    dictnocolor = {}
    pairs = []
    total = 0
    for x in ar:
        if x not in dictnocolor:
            dictnocolor[x] = 1
        else:
            dictnocolor[x] = dictnocolor[x] + 1
    for pair in dictnocolor:
        pairs.append(dictnocolor[pair]//2)
    for i in pairs:
        total += i 
    return total
