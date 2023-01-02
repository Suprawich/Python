#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 08:29:42 2021

@author: karn
"""

name = input('Enter your name. : ').strip()
age = int(input('Enter your age. : '))
b_year = (2564-age)%100
print(name,b_year,'@chula.ac.th',sep="")