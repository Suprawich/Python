#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 08:04:11 2021

@author: karn
"""

stu_id=int(input('Enter student ID : '))

#check stu_id
faculty=stu_id%100 #2 digit from back
degree=(stu_id//(10**7))%10 #3rd from front
year=stu_id//10**8 #2 digit from front

if len(str(stu_id))!=10 or year>64 or year<50:
    print('Invalid ID')
else:
    semester=int(input('Enter semester : '))
    
    if year>=50 and year<=55: #seperate by year
        
        if semester==1 or semester==2: #seperate by semester
            
            if degree in [3,4]: #seperate by degree
                if faculty in [21,23,25,28]: #sepreate by group
                    print('Registration fee : 18,000')
                elif faculty in [22,24,26,27]:
                    print('Registration fee : 14,500')
            elif degree in [7]:
                if faculty in [21,23,25,28]:
                    print('Registration fee : 26,000')
                elif faculty in [22,24,26,27]:
                    print('Registration fee : 19,000')
                    
        elif semester==3:
            if degree in [3,4]: #seperate by degree
                if faculty in [21,23,25,28]: #sepreate by group
                    print('Registration fee : 4,500')
                elif faculty in [22,24,26,27]:
                    print('Registration fee : 4,500')
            elif degree in [7]:
                if faculty in [21,23,25,28]:
                    print('Registration fee : 7,000')
                elif faculty in [22,24,26,27]:
                    print('Registration fee : 7,000')
        else:
            print('Invalid semester')
    
    elif year>=56:
        
        if semester==1 or semester==2: #seperate by semester
            
            if degree in [3,4]: #seperate by degree
                if faculty in [21,23,25,28]: #sepreate by group
                    print('Registration fee : 21,000')
                elif faculty in [22,24,26,27]:
                    print('Registration fee : 17,000')
            elif degree in [7]:
                if faculty in [21,23,25,28]:
                    print('Registration fee : 31,000')
                elif faculty in [22,24,26,27]:
                    print('Registration fee : 23,000')
                    
        elif semester==3:
            if degree in [3,4]: #seperate by degree
                if faculty in [21,23,25,28]: #sepreate by group
                    print('Registration fee : 5,250')
                elif faculty in [22,24,26,27]:
                    print('Registration fee : 5,250')
            elif degree in [7]:
                if faculty in [21,23,25,28]:
                    print('Registration fee : 7,750')
                elif faculty in [22,24,26,27]:
                    print('Registration fee : 7,750')
        else:
            print('Invalid semester')
            
    else:
        print('Invalid ID')