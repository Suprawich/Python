#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 20:51:37 2021

@author: karn
"""

mounth_list = []
income_list = []
expend_list = []
f = open('inc_exp.txt')
for line in f:
    line.strip()
    mounth,income,expend = line.split()
    mounth = int(mounth)
    income = int(income)
    expend = int(expend)
    mounth_list.append(mounth)
    income_list.append(income)
    expend_list.append(expend)
f.close()

input_mounth = int(input('Enter month number to get income and expend : '))
if input_mounth in mounth_list:
    balance = income_list[input_mounth-1]-expend_list[input_mounth-1]
    print('Month',input_mounth,'income =',income_list[input_mounth-1],'expend =',
          expend_list[input_mounth-1],'balance =',balance)

max_list = []
for i in range(12):
    balance_max = income_list[i]-expend_list[i]
    max_list.append(balance_max)

print('Max balance =',max(max_list),'is in month',max_list.index(max(max_list))+1)