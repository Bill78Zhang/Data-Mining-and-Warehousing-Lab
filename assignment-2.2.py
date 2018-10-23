# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:49:29 2018

@author: Jijnasa
"""
from __future__ import division
import csv
import numpy as np
import pandas as pd

data = pd.read_csv('apriori-2.csv')
milk = list(data.iloc[:,1].values)
bread = list(data.iloc[:,2].values)
butter = list(data.iloc[:,3].values)
maggie = list(data.iloc[:,4].values)



dic =	dict(milk=milk.count(1), bread= bread.count(1), butter=butter.count(1), maggie=maggie.count(1))        
x = len(milk)
dic2 = dict(milk_sup=milk.count(1)/x, bread_sup= bread.count(1)/x, butter_sup=butter.count(1)/x, maggie_sup=maggie.count(1)/x)        

b = { key: value for key, value in dic2.items() if value >= 0.5 }
print(b)
