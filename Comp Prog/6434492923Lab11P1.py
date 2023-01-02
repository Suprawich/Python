#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 08:09:11 2021

@author: karn
"""

stock = {}
count = 0
while count<10:
    product = input('Enter product ID, size, number of items : ')
    ID,size,number = product.split()
    number = int(number)
    if ID in stock:
        if size in stock[ID]:
            stock[ID][size] += number
        else:
            stock[ID][size] = number
    else:
        stock[ID] = {}
        if size in stock[ID]:
            stock[ID][size] += number
        else:
            stock[ID][size] = number
    count += 1

print('Stocks :')
for ID in sorted(stock):
    for size in sorted(stock[ID]):
        print(ID,size,stock[ID][size])