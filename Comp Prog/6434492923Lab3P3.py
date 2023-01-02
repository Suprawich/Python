#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 08:02:14 2021

@author: karn
"""

x,y = input('x,y : ').split(',')
x = int(x)
y = int(y)
if 0<x<10 and 0<y<20:
    print('(',x,',',y,')','is in','c')
elif 0<x<40 and 0<y<40:
    print('(',x,',',y,')','is in','A')
elif -40<x<10 and -20<y<20:
    print('(',x,',',y,')','is in','B')
else:
    print('(',x,',',y,')','is in','D')
