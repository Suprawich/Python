#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:01:21 2021

@author: karn
"""

x,y = input('Innitial position : ').split(',')
x,y = int(x),int(y)
f = open('move.txt')
for line in f:
    line = line.strip()
    if line in ['L','R','U','D']:
        if -9<x<9:
            if line == 'L':
                x -= 1
            elif line == 'R':
                x += 1
        if -9<y<9:
            if line == 'U':
                y += 1
            elif line == 'D':
                y -= 1
        point = str(x)+','+str(y)
    else:
        point = 'Invalid command'
        break
f.close()
print('Robot stops at',point)