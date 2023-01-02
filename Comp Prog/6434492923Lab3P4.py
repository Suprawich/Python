#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 08:02:15 2021

@author: karn
"""

stu_id = input('Enter student ID : ')
check1 = len(stu_id)==10
stu_id = int(stu_id)
check2 = stu_id//(10**8)>=50 and stu_id//(10**8)<=64
check3 = (stu_id//(10**7))%10 in [3,4,7]
check4 = stu_id%100 in [21,22,23,24,25,26,27,28]
if check1 and check2 and check3 and check4:
    print('Valid ID')
else:
    print('Invalid ID')