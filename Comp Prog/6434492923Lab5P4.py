#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:07:01 2021

@author: karn
"""

num_stu = int(input('Number of student : '))
if num_stu>0:
    total = 0
    total_pass = 0
    total_fail = 0
    count_pass = 0
    count_fail = 0
    score_hight = 0
    for i in range(1,num_stu+1):
        stu_score = float(input('Student '+str(i)+' : '))
        if stu_score>=0:
            total += stu_score
            avg = total/num_stu
        if stu_score>=5:
            count_pass += 1
            if count_pass==0:
                avg_pass=0
            else:
                total_pass += stu_score
                avg_pass = total_pass/count_pass
        if stu_score<5:
            count_fail += 1
            if count_fail==0:
                avg_fail = 0
            else:
                total_fail += stu_score
                avg_fail = total_fail/count_fail
        if stu_score>score_hight:
            score_hight=stu_score
else:
    avg=0
    avg_fail=0
    avg_pass=0
    score_hight=0
print('Average score : ',avg)    
print('Average passing score : ',avg_pass)        
print('Average failing score : ',avg_fail)
print('Highest score : ',score_hight)