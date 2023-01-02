#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 08:09:40 2021

@author: karn
"""

item = []
def add_item(item_list):
    item_list = input('Enter item : ')
    if item_list not in item:
        item.append(item_list)
        print('Item has been added.')
    else:
        print('Item is already in the list.')
    return(item)
    
def change_item(item_list):
    item_list = input('Enter item you want to change : ')
    if item_list not in item:
        print('Item is not in the list.')
    else:
        index = item.index(item_list)
        item.remove(item_list)
        new = input('Enter new item : ')
        item.insert(index,new)
    
def insert_item(item_list):
    item_list = input('Enter item : ')
    index = int(input('Enter location that you want to insert : '))
    item.insert(index, item_list)
    print('Item has been inserted.')
    
def remove_item(item_list):
    item_list = input('Enter item you want to remove : ')
    if item_list in item:
        item.remove(item_list)
        print('Item has been removed.')
    else:
        print('This item is not in the list.')

def show_item(item_list):
    if item == []:
        print('This list is currently empty.')
    else:
        print(item)
        
print('What would you like to do?')
print('1: add item')
print('2: change item')
print('3: insert item')
print('4: remove item')
print('5: show item')
print('6: exit')

num = input('Enter a number : ')
while num != '6':
    if num == '1':
        add_item(item)
        num = input('Enter a number : ')
    elif num == '2':
        change_item(item)
        num = input('Enter a number : ')
    elif num == '3':
        insert_item(item)
        num = input('Enter a number : ')
    elif num == '4':
        remove_item(item)
        num = input('Enter a number : ')
    elif num == '5':
        show_item(item)
        num = input('Enter a number : ')
    