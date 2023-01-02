#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:06:55 2021

@author: karn
"""

name = input('Enter username : ')
count = 1
if name=='Suprawich':
    print('Hello,',name)
else:
    while name != 'Suprawich':
        name = input('Incorrect. Enter again : ')
        count += 1
        if name=='Suprawich':
            print('Hello,',name)
            break
        if count==3:
            print('Not allowed. Incorrect name.')
            break