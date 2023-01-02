#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 07:35:43 2021

@author: 6434492923 suprawich sakulromvilas
"""

name = input('Enter name of goods : ')
if name == 'pineapple':
    price = float(input('Enter price : '))
    if price>0:
        print('The price of',name,'is',price,'Baht.')
    else:
        print('Invalid price.')
elif name == 'strawberry':
    price = float(input('Enter price : '))
    if price>0:
        print('The price of',name,'is',price,'Baht.')
    else:
        print('Invalid price.')
else:
    print('Invalid goods.')