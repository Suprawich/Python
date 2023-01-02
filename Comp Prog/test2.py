#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 20:51:38 2021

@author: karn
"""

village = [('zone1', 'S', 20), ('zone1', 'M', 10), ('zone1', 'L', 5), 
           ('zone2', 'S', 20), ('zone2', 'M', 25), ('zone3', 'L', 20)]

list_house = []
zone = [village[i][0] for i in range(len(village))]
name_of_zone = input('Enter a zone name to view data : ')
if name_of_zone in zone:
    for i in range(len(village)):
        if name_of_zone==village[i][0]:
            size = village[i][1]
            number = village[i][2]
            tuple_house = tuple([size,number])
            list_house.append(tuple_house)
            
    sum_list = [list_house[i][1] for i in range(len(list_house))]
    
    print('List of house in',name_of_zone,':',list_house)
    print('There are',len(list_house),'sizes of house in',name_of_zone)
    print('There are',sum(sum_list),'houses in',name_of_zone)
else:
    print('Not found')