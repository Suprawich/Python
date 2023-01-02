#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 08:27:48 2021

@author: karn
"""

price = float(input('Enter price. : '))
ship = float(input('Enter shipping. : '))
total = price+ship
print('Total : ',total,' Bath ','(',ship,' Bath shipping fee.',')',sep="")