#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 20:51:38 2021

@author: karn
"""

training = {'Mike':{'MO':1, 'TU':2, 'FR':3}, 
            'Got':{'MO':1, 'WE':2, 'FR':1},
            'Jane':{'MO':1, 'TH':2, 'FR':3}}

name_day = input('Enter name and day to get number of training class : ')
while name_day != '0':
    name,day = name_day.split()
    name_trainer = [i for i in training]
    if name in name_trainer:
        day_training = [i for i in training[name]]
        if day in day_training:
            print('Number of training class :',training[name][day])
        else:
            print('Not found')
    else:
        print('Not found')
    name_day = input('Enter name and day to get number of training class : ')

dict_class = {}
list_class = []
for k in training:
    for c in training[k]:
        list_class.append(training[k][c])
        dict_class[k] = sum(list_class)
    list_class = []
print('Dictionary of total number of classes :',dict_class)