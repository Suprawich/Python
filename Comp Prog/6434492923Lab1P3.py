#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 08:36:13 2021

@author: karn
"""

name,age = input('Enter your name and age. : ').split()
age = int(age)
b_year = 2564-age
print(name+"'s",' year of birth is ',b_year,'.',sep="")