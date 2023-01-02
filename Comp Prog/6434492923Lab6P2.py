#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 08:05:25 2021

@author: karn
"""

num = int(input('Enter an integer : '))
print(num,'is divisible by :')
for i in range(1,num+1):
    if num%i==0:
        print(i)