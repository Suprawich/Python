#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 08:08:39 2021

@author: karn
"""

subject = {2301117:('Calculus I',4),
           2301118:('Calculus II',4),
           2301286:('Probability and Statistics',3),
           2301399:('Project Proposal',1),
           2301499:('Senior Project',2),
           2302112:('General Chemistry Lab I',1),
           2302161:('General Chemestry',3)}

ID = int(input('Course ID: '))
key = [key for key in subject]
while ID!=0:
    if ID in key:
        print(subject[ID][0],subject[ID][1])
        ID = int(input('Course ID: '))
    else:
        print('Unknow')
        ID = int(input('Course ID: '))