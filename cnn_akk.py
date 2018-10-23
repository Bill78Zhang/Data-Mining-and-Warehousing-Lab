# -*- coding: utf-8 -*-
"""
Created on Tue Oct 09 13:28:58 2018

@author: Student
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:04:25 2018
@author: Student
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:02:25 2018
@author: Student
"""

filename='C:/Users/Student/Desktop/115cs0227/iris.csv'

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs
 

ds=pd.read_csv(filename)
#print ds
ds['flower'],class_names = pd.factorize(ds['flower'])


###different classes division#####

prop_amt=0.80
print 'train:test '+str(prop_amt)+':'+str(1-prop_amt)

X = ds.values[:, 0:4]
Y = ds.values[:,-1]
values=np.unique(Y)
c=len(values)

X, X_test, Y, Y_test = train_test_split( X, Y, test_size = 0.2)
#print(c)
#print (X[0])
#print(X)
###initialization

condensed_x=[]
condensed_x.append(X[1])
condensed_y=[]
condensed_y.append(Y[1])
#print (condensed_x[0], condensed_y[0])


#################distance from each#######
import math
def eDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        #print (instance2[x])
        
        distance += pow((instance1[x] - instance2[x]), 2)
        #print(1)
    return math.sqrt(distance)

########getting neighbor########   
import operator 
def getNearestNeighbor(trainingSet, testInstance,condensed_y):
    distances = []
    length = len(testInstance)
    #print (length)
    for x in range(len(trainingSet)):
        #print trainingSet[x]
        #print (len(trainingSet))
        dist = eDistance(testInstance, trainingSet[x], length)
        distances.append((condensed_y[x], dist))
    distances.sort(key=operator.itemgetter(1))
    #print distances
    
    neighbors = np.nonzero(distances[0][0]==values)[0]
    #print(neighbors)
    return neighbors



for i in range(2, len(X)):
##########main############
    #print('!!!!!!!!!!!')
    #print (X[:][5])
    nb=getNearestNeighbor(condensed_x,X[i],condensed_y)
    
    for w in range(c):
                if nb==w:
                    n=w
    #print(n)
    y=n
    actual=Y[i] 
    if(y!=actual):
        condensed_x.append(np.array(X[i]))
        condensed_y.append(np.array(Y[i]))
        
    #print(len(condensed_x))
    #print 'y,actual=',(y, actual)
print(condensed_x,condensed_y)
l=len(condensed_x)
print('Length of condensed set ',l)

#####testing#####
count=0
for p in range(1,len(X_test )):
    nb=getNearestNeighbor(condensed_x,X_test[p],condensed_y)
    for w in range(c):
                if nb==w:
                    n=w
    y=n
    actual=Y_test[p] 
    if(y!=actual):
        count+=1
accuracy=(len(X_test)-count)*100/len(X_test)
print('Accuracy= ' ,accuracy)