# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 15:17:04 2018

@author: Student
"""

from __future__ import division
import csv
import math
print('--------------asymmetric-Measures-----------------')
#Goodman-Kruskal
print('-----------------Goodman-Kruskal------------------')
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        corr = ((row_9*row_1) - (row_5*row_7))/math.sqrt(row_5*row_6*row_7*row_8)
        print(corr)
print('--------------------Odds Ratio---------------------')
 #Odds Ratio 
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        ora = (row_1*row_4)/(row_2*row_3)
        print(ora)
print('--------------------Kappa---------------------')
#kappa
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        ka = ((row_9*row_1)+(row_9*row_4)-(row_5*row_7)-(row_6*row_8))/((row_9*row_9)-(row_5*row_7)-(row_6*row_8))
        print(ka)
print('--------------------Interest---------------------')
#interest
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        inte = (row_9*row_1)/(row_5*row_7)
        print(inte)
print('--------------------Cosine---------------------')
#cosine
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        cosi = row_1/math.sqrt(row_5*row_7)
        print(cosi)
print('--------------------Piatetsky-Shapiro---------------------')
#Piatetsky-Shapiro
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        ps = (row_1/row_9)-((row_5*row_7)/(row_9*row_9))
        print(ps)
print('--------------------Collective-Strength---------------------')
#Collective_Strength
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        ps = ((row_1+row_4)/((row_5*row_7)+(row_6*row_8)))*((row_9-(row_5*row_7)-(row_6*row_8))/(row_9-row_1-row_4))
        print(ps)
print('--------------------Jaccard---------------------')
#Jaccard
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        ja = (row_1)/(row_5+row_7-row_1)
        print(ja)
print('--------------------All-Confidence---------------------')
#all_confidence
with open('assym_sym.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    row = next(spamreader)
   
    for row in spamreader:
        row_1 = int(row[1])
        row_2 = int(row[2])
        row_3 = int(row[3])
        row_4 = int(row[4])
        row_5 = int(row[5])
        row_6 = int(row[6])
        row_7 = int(row[7])
        row_8 = int(row[8])
        row_9 = int(row[9])
        ac = min((row_1/row_5),(row_1/row_7))
        print(ac)