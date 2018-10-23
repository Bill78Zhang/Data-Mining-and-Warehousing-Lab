# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:10:17 2018

@author: Student
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 13:40:44 2018

@author: Student
"""

from sklearn import cluster, datasets
import numpy as np
iris = datasets.load_iris()
X_iris = iris.data
y_iris = iris.target
clustering = cluster.AgglomerativeClustering(n_clusters=3,linkage='complete')
clustering.fit(X_iris) 
print(clustering.labels_)

print(y_iris)