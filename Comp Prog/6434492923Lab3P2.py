#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 08:02:14 2021

@author: karn
"""

weight = float(input('Weight (kg.) : '))
height = float(input('Height (m.) : '))
bmi = weight/(height**2)
if bmi<18.5:
    print('ผอม')
elif bmi>=18.5 and bmi<23:
    print('รูปร่างปกติ')
elif bmi>=23 and bmi<25:
    print('รูปร่างอ้วน')
elif bmi>=25 and bmi<30:
    print('อ้วนระดับ1')
elif bmi>=30:
    print('อ้วนระดับ2')