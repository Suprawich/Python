#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 08:08:50 2021

@author: karn
"""

menu = {'Cappuccino':{'S':60,'L':70},
        'Espresso':{'S':45,'L':50},
        'Latte':{'S':65,'L':75}}
        
order = input('Enter drink, size and number : ')
drink,size,number = order.split()

menu_drink = list(menu.keys())
if drink in menu_drink:
    menu_size = list(menu[drink].keys())
    if size in menu_size:
        total = menu[drink][size]*int(number)
        print('Total :',total)
    else:
        print('Incorrect size')
else:
    print('Drink not available')