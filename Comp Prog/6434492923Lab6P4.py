#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 08:05:26 2021

@author: karn
"""

temp_yd = float(input('Day 1 : '))
for i in range(2,8):
    temp_td = input('Day '+str(i)+' : ')
    temp_td = float(temp_td)
    if temp_td<temp_yd:
        print('Temperature dropped on day',i)
    temp_yd=temp_td
        
    