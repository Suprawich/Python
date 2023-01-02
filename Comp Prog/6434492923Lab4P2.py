#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 08:04:10 2021

@author: karn
"""

weight,unit_w=input('Weight : ').split()
weight=float(weight)
if unit_w=='lbs':
    weight=weight/2.205
    
height,unit_h=input('Height : ').split()
height=float(height)
if unit_h=='cm':
    height=height/100
elif unit_h=='ft':
    height=height/3.2808399

bmi = weight/(height**2)
if bmi>=30.0:
    print('อ้วนระดับ 2')
elif bmi>=25.0 and bmi<30:
    print('อ้วนระดับ 1')
elif bmi>=23.0 and bmi<25:
    print('รูปร่างอ้วน')
elif bmi>=18.5 and bmi<23:
    print('รูปร่างปกติ')
else:
    print('ผอม')
