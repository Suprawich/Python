#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 20:23:39 2021

@author: karn
"""

num = input('Enter number between [0,9]: ')
value = [value for value in range(1,100) if str(num) in str(value) if int(value)>=2]
print(value)