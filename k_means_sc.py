# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 13:56:21 2018

@author: Student
"""

from sklearn import cluster, datasets
iris = datasets.load_iris()
X_iris = iris.data
y_iris = iris.target

k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris) 

#print(k_means.labels_[::10])
print(k_means.labels_)

#print(y_iris[::10])
print(y_iris)

