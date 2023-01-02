#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 08:00:25 2021

@author: karn
"""

import math as m
a,b,c = input('Enter coefficients a, b, c : ').split(',')
a = float(a)
b = float(b)
c = float(c)
x1 = (-b+m.sqrt(b**2-4*a*c))/(2*a)
x2 = (-b-m.sqrt(b**2-4*a*c))/(2*a)
print('x','=',x1,',',x2)