#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 08:05:22 2021

@author: karn
"""

nw = input('Next word : ')
st = ""
while nw!='.':
    st = st+' '+nw
    st = st.strip()
    nw = input('Next word : ')
print('Sentence :',st)