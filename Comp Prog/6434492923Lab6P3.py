#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 08:05:25 2021

@author: karn
"""

num = int(input('Enter an integer : '))
cnt = 0
if num==1:
    print(num,'is not a prime number.')
for i in range(2,num):
    if num%i==0:
        cnt+=1
        if cnt==1:
            print(num,'is not a prime number.')
            break
if cnt==0:
    print(num,'is prime number.')
