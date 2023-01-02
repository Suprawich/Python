#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 08:09:56 2021

@author: karn
"""

tuition = {'G1':{'bachelor':{'sem_1_2':{'year_48_49':16000,'year_50_55':18000,'year_56_now':21000},
                             'sem_3':{'year_48_49':4000,'year_50_55':4500,'year_56_now':5250}},
                 'master':{'sem_1_2':{'year_48_49':22500,'year_50_55':26000,'year_56_now':31000},
                           'sem_3':{'year_48_49':6000,'year_50_55':7000,'year_56_now':7750}}},
           'G2':{'bachelor':{'sem_1_2':{'year_48_49':12000,'year_50_55':14500,'year_56_now':17000},
                             'sem_3':{'year_48_49':4000,'year_50_55':4500,'year_56_now':5250}},
                 'master':{'sem_1_2':{'year_48_49':16500,'year_50_55':19000,'year_56_now':23000},
                           'sem_3':{'year_48_49':6000,'year_50_55':7000,'year_56_now':7750}}}}

bachelor_degree = [i for i in range(0,10) if i!=7]
master_degree = [7]

G1 = [21,23,25,28,30,31,32,33,35,36,37,38,39,53]
G2 = [22,24,26,27,29,34,40,51]

year_48_49 = [i for i in range(48,50)]
year_50_55 = [i for i in range(50,56)]
year_56_now = [i for i in range(56,65)]

ID = input('Enter student ID : ')
if len(ID) == 10 and 48<=int(ID[0:2]) and 21<=int(ID[8:])<=53:
    ID = int(ID)
    semester = int(input('Enter semester : '))
    if semester in [1,2,3]:
        degree_check = (ID//(10**7))%10
        faculty_check = ID%100
        year_check = ID//(10**8)
        
        if faculty_check in G1:
            group = 'G1'
        elif faculty_check in G2:
            group = 'G2'
            
        if degree_check in bachelor_degree:
            degree = 'bachelor'
        elif degree_check in master_degree:
            degree = 'master'
        
        if semester in [1,2]:
            sem = 'sem_1_2'
        elif semester in [3]:
            sem = 'sem_3'
            
        if year_check in year_48_49:
            year = 'year_48_49'
        elif year_check in year_50_55:
            year = 'year_50_55'
        elif year_check in year_56_now:
            year = 'year_56_now'
            
        print('Registration fee :',tuition[group][degree][sem][year])
    else:
        print('Invalid semester')
else:
    print('Invalid ID')



