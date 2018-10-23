# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 12:29:01 2018

@author: Student
"""
from __future__ import division
#function to find mean 
def find_mean(mylist):
    s = sum(mylist) #finding sum of list
    print('Mean')
    m = s/len(mylist)
    print(m)
#function to find mode    
def mode(l):
    if len(l)>1:
        d = {}
    for value in l:
        if value not in d:
            d[value] = 1 
        else:
            d[value] += 1
    if len(d) == 1:
        print(value)
    else:
        i = 0
        
        for key,value in d.items():
            if i < value:
                i = value
        
        print('Modes are')
        #If more than one mode is present
        for key,value in d.items(): 
            if i == value:
                print(key)  
#function to find median        
def find_median(l):
    #sort the list
    l = sorted(l)
    n = len(l)
    mid = n//2 #to get integer value as mid as it will be index to the list
    if n%2 == 0:
        return(l[mid] + l[mid-1])/2 
    else:
        return(l[mid])
l = [20, 22, 22, 56, 56,79] #declaring list
#function calls
mode(l)
find_mean(l)
med = find_median(l)
print('Median',med)


