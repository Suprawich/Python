#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 08:08:47 2021

@author: karn
"""


stu_score = {}
f = open('studentscore.txt')
for line in f:
    line = line.strip()
    name,score = line.split()
    stu_score[name] = score
f.close()

def order(key):
    score = stu_score[key[0]]
    return(score)    

sort = sorted(stu_score.items(),key=order,reverse=True)
for i in sort:
    print(i[0])