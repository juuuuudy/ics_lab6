#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 09:11:09 2018

@author: juuuuudy
"""



def sort(number):
    number.sort()
    return number

def arrange(number,order):
    new_list=[]
    for i in order:
        if i == '>':
            new_list.append(number.pop(-1))
            new_list.append('>')
        else:
            new_list.append(number.pop(0))
            new_list.append('<')

    new_list.append(number.pop(0))
    return new_list

number = [1,3,5,2,8]
order=['<','>','>','>']    
numerb = sort(number)
print(arrange(number,order))


