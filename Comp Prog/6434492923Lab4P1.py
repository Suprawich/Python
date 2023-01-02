#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 08:04:10 2021

@author: karn
"""

import math as m
shape = input('Choose circle, square or rectangle : ')

if shape=='circle':
    radius=float(input('Length of the radius of the circle : '))
    area=m.pi*m.pow(radius, 2)
    print('Area is',area)
elif shape=='square':
    side=float(input('Length of the side of the square : '))
    area=m.pow(side, 2)
    print('Area is',area)
elif shape=='rectangle':
    length1,length2=input('Length of the two side of the rectangle : ').split(',')
    length1=float(length1)
    length2=float(length2)
    area=length1*length2
    print('Area is',area)
else:
    print('Invalid choice.')
