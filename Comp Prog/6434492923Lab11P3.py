#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:25:10 2021

@author: karn
"""

score = {}
sum_score = []
f = open('score.txt')
for line in f:
    line = line.strip()
    line = line.split()
    sum_score = [line[e] for e in range(1,len(line))]
    sum_score = [int(e) for e in sum_score]
    summary = sum(sum_score)
    score[line[0]] = summary
    sum_score = []
    
def order(key):
    summary = score[key[0]]
    return(summary)

sort = sorted(score.items(),reverse=True,key=order)

print('The winners are :')
for i in range(3):
    print(i+1,':',sort[i][0],sort[i][1])
