# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:01:54 2018

@author: Student
"""

from sklearn.cluster import AgglomerativeClustering
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])
clustering = AgglomerativeClustering().fit(X)
#clustering 



print(clustering.labels_)
