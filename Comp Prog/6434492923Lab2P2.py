#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 08:00:26 2021

@author: karn
"""

a,b,c = input('Enter coefficients a, b, c : ').split(',')
a = float(a)
b = float(b)
c = float(c)
check = b**2-4*a*c>=0 and a!=0
print('Can use quadratic formula:',check)