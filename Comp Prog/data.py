#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 02:20:49 2022

@author: karn
"""

# HW11_TSD (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)

# - เขียนในเซลล์นี้เท่านั้น 
# - ถ้าต้องการเขียนฟังก์ชันเพิ่ม ก็เขียนในเซลล์นี้

def convert_to_dict(data,column_name):
    ans = []
    d = dict()
    count = 0
    count_none = 0
    while count != len(data):
        for j in data:
            for i in column_name:
                d[i] = None
            for k in range(len(j)):
                if j[k] != None:
                    d[column_name[k]] = j[k]
                else:
                    count_none += 1;
                    del d[column_name[k]]
            if count_none == 4:
                del d
            else:
                count_none = 0
                ans.append(d)
            d = dict()
            count += 1
    return ans

def convert_to_dict_with_key(data,column_name,key):
    d1 = dict()
    l = []
    call = convert_to_dict(data, column_name)
    for i in call:
        for j in i:
            l.append(j)
        if key in l:
            keep = i[key]
            if keep not in d1:
                del i[key]
                d1[keep] = i
                l = []
            else:
                l = []
        else:
            l = []
            
    for i in d1:
        l.append(i)
    for i in l:
        if len(d1[i]) == 0:
            del d1[i]
    
    return d1

def join_data(data1,data2):
    data = data1
    list1 = []
    list2 = []
    for i in data1:
        list1.append(i)
    for i in data2:
        list2.append(i)
    for i in list1:
        if i in list2:
            for j in data2[i]:
                if j in data[i]:
                    data[i][j+"_1"] = data2[i][j]
                else:
                    data[i][j] = data2[i][j]
        else:
            data = {}
    return data

def merge_data(data1,data2):
    data = join_data(data1, data2)
    list1 = []
    list2 = []
    list3 = []
    for i in data1:
        list1.append(i)
    for i in data2:
        list2.append(i)
    for i in data:
        list3.append(i)
    for i in list1:
        if i not in list3:
            data[i] = data1[i]
    for i in list2:
        if i not in list3:
            data[i] = data2[i]
    return data

def subtract_data(data1,data2):
    data = data1
    list1 = []
    list2 = []
    for i in data1:
        list1.append(i)
    for i in data2:
        list2.append(i)
    for i in list2:
        if i in list1:
            for j in data2[i]:
                if j in data[i]:
                    del data[i][j]
            if len(data[i]) == 0:
                del data[i]
    return data