#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:09:32 2018

@author: Tom
"""

def gcd(x,y):
    if x<y:
        x,y=y,x
    while x%y!=0:
        r=x%y
        x=y
        y=r
    return r
x=eval(input('Enter the first number:'))
y=eval(input('Enter the second number:'))
    
gcdxy=gcd(x,y)
print('GCD({0:d},{1:d})={2:d}'.format(x,y,gcdxy))
    
    






















