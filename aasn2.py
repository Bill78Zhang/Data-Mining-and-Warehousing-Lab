# -*- coding: utf-8 -*-
"""
Created on Tue Aug 07 14:04:17 2018

@author: Jijnasa
"""
import math
from math import *
from decimal import Decimal
def p_root(value, root):
     
    root_value = 1 / float(root)
    return round (Decimal(value) **
             Decimal(root_value), 3)
 
def minkowski_distance(x, y, p_value):
     
    return (p_root(sum(pow(abs(a-b), p_value)
            for a, b in zip(x, y)), p_value))
x = (5, 6, 7, 17)
y = (8, 9, 9, 13)
euc_distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print("Euclidean distance from x to y: ",euc_distance)
man_distance = sum(abs(e - s) for s,e in zip(x, y))
print("Manhattan distance from x to y: ",man_distance)
p = 3
print("Minkowski distance from x to y: ",minkowski_distance(x,y,p))