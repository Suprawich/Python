#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 08:11:32 2021

@author: karn
"""

sol = open('sol.txt')
exam = open('exam.txt')
sol_1 = sol.readline().split()
s = [line.split() for line in exam]
sol.close()
exam.close()

stu_score = []
score = 0
    
for main in range(len(s)):
    for sub in range(len(sol_1)):
        if s[main][sub]==sol_1[sub]:
            score += 1
    stu_score.append(score)
    score = 0
print('Student score : ',stu_score)

count = 0
frequency = []
for sub in range(len(sol_1)):
    for main in range(len(s)):
        if s[main][sub]==sol_1[sub]:
            count += 1
    avg_count = count/len(s)
    count = 0
    frequency.append(avg_count)
for num in range(len(sol_1)):
    print('Question',num+1,':',frequency[num])
    
max_ = ''
min_ = ''
for ind in range(len(frequency)):
    if frequency[ind] == max(frequency):
        max_ += str(ind+1) + ' '
    elif frequency[ind] == min(frequency):
        min_ += str(ind+1) + ' '
for i in range(len(frequency)):
    print(min_+'is the hardest question.')
    print(max_+'is the easiest question.')
    break