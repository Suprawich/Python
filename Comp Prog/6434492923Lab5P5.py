#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:07:01 2021

@author: karn
"""

money = 50000.0
while money>0:
    withdraw = float(input('withdraw : '))
    if withdraw<=money:
        money = money-withdraw
    else:
        print('Insufficient fund.')
print('Balance is 0.')