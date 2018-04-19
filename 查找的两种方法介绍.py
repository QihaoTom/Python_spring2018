#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:09:32 2018

@author: Tom
"""

# 查找的两种方法介绍
## 一是线形查找 sequential
lst=[45,67,23,43,56]
n=len(lst)
m=-1
key=int(input('enter the key'))
for i in range(n):
    if lst[i]==key:
        m=i
        break
if m!=-1:
    print('found!',m)
else:
    print('not found!')
    
## 二是折半查找 binary
lst=[5,23,28,34,43,45,56,60,67,90]
key=int(input('input the key'))
low,high=0,len(lst)-1
while low<=high:
    mid=(low+high)//2
    if lst[mid]==key:
        k=mid
        break
    if key<lst[mid]:
        high=mid-1
    else:low=mid+1
if low<=high:
    print('found',mid)
else:
    print('not found!')
    
    
    
    






















