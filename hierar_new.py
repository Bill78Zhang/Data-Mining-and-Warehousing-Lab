# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:37:12 2018

@author: Student
"""

import matplotlib.pyplot as plt  
import pandas as pd  
import scipy.cluster.hierarchy as shc
import numpy as np  
from sklearn.cluster import AgglomerativeClustering  
iris_data = pd.read_csv('Iris_1.csv')  
#print(customer_data.shape )
#print(customer_data.head()) 
iris_data = iris_data.iloc[:, 1:5].values  
print(iris_data)  
plt.figure(figsize=(10, 7))  
plt.title("Iris Dendograms")  
dend = shc.dendrogram(shc.linkage(iris_data, method='ward')) 
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')  
cluster.fit_predict(iris_data) 
print(cluster.labels_)
plt.figure(figsize=(10, 7))  
plt.scatter(iris_data[:,0], iris_data[:,1], c=cluster.labels_, cmap='rainbow')  