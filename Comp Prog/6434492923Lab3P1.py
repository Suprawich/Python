#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 08:02:13 2021

@author: karn
"""

import math as m
a,b,c = input('Enter coefficients a, b, c : ').split(',')
a = float(a)
b = float(b)
c = float(c)
if 2*a!=0 and b**2-(4*a*c)>0:
    x1 = (-b+m.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-m.sqrt(b**2-4*a*c))/(2*a)
    print('x = ',x1,', ',x2,sep="")
else:
    print('No real so;ution.')