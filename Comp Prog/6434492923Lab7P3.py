#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:01:22 2021

@author: karn
"""

def f(x):
    fac = 1
    for i in range(1,x+1):
        fac = fac*i
    func = 1/fac
    return func

def summation(m,n):
    summa = 0
    if m<n:
        for i in range(m,n+1):
            summa = summa+f(i)
    else:
        for i in range(m,n-1,-1):
            summa = summa+f(i)
    return summa

m = int(input('Enter m : '))
n = int(input('Enter n : '))
print(summation(m, n))