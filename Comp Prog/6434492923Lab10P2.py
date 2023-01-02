#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 08:08:41 2021

@author: karn
"""

f = open('conversation.txt')
count = {}
count_word = 0
list_word = []
l = ''

for line in f:
    line = line.strip()
    l = l + ' ' + line
f.close()
word = l.split()

for i in range(len(word)):
    word1 = word[i].strip(':.,?')
    list_word.append(word1)
    for j in range(len(list_word)):
        if list_word[i] == list_word[j]:
            count_word += 1
            count[list_word[i]] = count_word
    count_word = 0
    
for key,value in count.items():
    print(key,value)