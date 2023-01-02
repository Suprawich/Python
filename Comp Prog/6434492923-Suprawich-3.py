#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 08:10:45 2021

@author: 6434492923 สุประวิชญ์ สกุลโรมวิลาส
"""

patient = {'UdonThani':17657,'SakonNakhon':7692,'NakhonPhanom':4974,
           'Loei':3614,'NongKhai':3901,'NongBuaLumphu':4204,'BuengKan':2014}


for i in range(len(patient)):
    add_patient = input('Enter patients in each of 7 province: ')
    province,pat = add_patient.split()
    pat = int(pat)
    for k in patient:
        if province == k:
            pat += patient[province]
            patient[province] = pat
    
print('Report')
for k in patient:
    print(k,patient[k])