#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 08:09:41 2021

@author: karn
"""

def sum_digits(n):
    sum1 = 0
    for i in range(len(n)):
        if n[i].isdigit():
            sum1 += int(n[i])
    return(sum1)          

n = input('Enter string : ')
print(sum_digits(n))