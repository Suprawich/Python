#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 08:11:32 2021

@author: karn
"""

f = open('vectors.txt')
v1 = f.readline().split()
v2 = f.readline().split()
f.close()
v1_f = []
for i in v1:
    i = float(i)
    v1_f.append(i)
v2_f = []
for i in v2:
    i = float(i)
    v2_f.append(i)
dot = 0
if len(v1) == len(v2):
    for i in range(len(v1_f)):
        multiply = v1_f[i]*v2_f[i]
        dot += multiply
    print('v1 =',v1_f)
    print('v2 =',v2_f)
    print('v1*v2 =',dot)
else:
    print('v1 =',v1_f)
    print('v2 =',v2_f)
    print('Incompatible size')