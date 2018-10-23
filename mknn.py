# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:58:57 2018

@author: Student
"""


import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('car.csv')

#assign name to the columns
dataset.columns = ['buying','maint','doors','persons','lug_boot','safety','classes']

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

#Categorical values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
X = X.apply(LabelEncoder().fit_transform)
onehotencoder = OneHotEncoder(categorical_features=[2,3])
X = onehotencoder.fit_transform(X).toarray()

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
y_train = y_train.ravel()
y_test = y_test.ravel()

for K in range(25):
 K_value = K+1
 neigh = KNeighborsClassifier(n_neighbors = K_value, weights='distance', algorithm='auto')
 neigh.fit(X_train, y_train) 
 y_pred = neigh.predict(X_test)
 print "Accuracy is ", accuracy_score(y_test,y_pred)*100,"% for K-Value:",K_value
'''plt.plot(neighbors, MSE)
plt.xlabel('Number of Neighbors K')
plt.ylabel('Misclassification Error')
plt.show()'''