#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 07:35:44 2021

@author: 6434492923 suprawich sakulromvilas
"""

import math as m
r_circle1 = float(input('Enter radius : '))
while r_circle1>0:
    r_circle2 = float(input('Enter radius : '))
    area_circle1 = m.pi*(r_circle1**2)
    area_circle2 = m.pi*(r_circle2**2)
    if r_circle2<r_circle1:
        break
    r_circle1 = r_circle2
    dif_area = round(area_circle2-area_circle1,2) #พื้นที่เทียบกับวงกลมแรกที่รับนอกลูป
    print('difference of area is',dif_area)