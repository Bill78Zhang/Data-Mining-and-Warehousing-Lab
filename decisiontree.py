# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 13:35:58 2018

@author: Student
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:18:25 2018

@author: Student
"""

import os
import numpy as np
import pandas as pd
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn import tree, metrics

data = pd.read_csv('car.data.txt',names=['buying','maint','doors','persons','lug_boot','safety','class'])
data['class'],class_names = pd.factorize(data['class'])
data['buying'],_ = pd.factorize(data['buying'])
data['maint'],_ = pd.factorize(data['maint'])
data['doors'],_ = pd.factorize(data['doors'])
data['persons'],_ = pd.factorize(data['persons'])
data['lug_boot'],_ = pd.factorize(data['lug_boot'])
data['safety'],_ = pd.factorize(data['safety'])
X = data.iloc[:,:-1]
y = data.iloc[:,-1]
X_train, X_test, y_train, y_test = sk.cross_validation.train_test_split(X, y, test_size=0.2, random_state=0)

dtree = tree.DecisionTreeClassifier(criterion='gini', splitter='best')
dtree.fit(X_train, y_train)

# use the model to make predictions with the test data
y_pred = dtree.predict(X_test)
# how did our model perform?
count_misclassified = (y_test != y_pred).sum()
print('Misclassified samples: {}'.format(count_misclassified))
accuracy = metrics.accuracy_score(y_test, y_pred)
print('Accuracy: {:.2f}'.format(accuracy))

