#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 08:05:26 2021

@author: karn
"""

import random
num = random.randint(1, 9)
guess = int(input('Your guess : '))
while guess!=num:
    guess = int(input('Your guess : '))
print('Correct')