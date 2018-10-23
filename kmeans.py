# -*- coding: utf-8 -*-
"""
Created on Tue Oct 09 14:57:40 2018

@author: Student
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2010 Matteo Bertini <matteo@naufraghi.net>
# Licensed as http://creativecommons.org/licenses/BSD/
#
# This is a naive implementation of the k-means unsupervised clustering
# algorithm (http://en.wikipedia.org/wiki/K-means_clustering).

from __future__ import division
import sys
from collections import defaultdict
import random
from pprint import pprint

import numpy as np

# Get iris dataset from http://archive.ics.uci.edu/ml/datasets/Iris
def load_data():
    data = [l.strip() for l in open('iris.data.txt') if l.strip()]
    features = [tuple(map(float, x.split(',')[:-1])) for x in data]
    labels = [x.split(',')[-1] for x in data]
    return dict(zip(features, labels))

def dist2(f1, f2):
    a = np.array
    d = a(f1)-a(f2)
    return np.sqrt(np.dot(d, d))

def mean(feats):
    return tuple(np.mean(feats, axis=0))

def assign(centers):
    new_centers = defaultdict(list)
    for cx in centers:
        for x in centers[cx]:
            best = min(centers, key=lambda c: dist2(x,c))
            new_centers[best] += [x]
    return new_centers

def update(centers):
    new_centers = {}
    for c in centers:
        new_centers[mean(centers[c])] = centers[c]
    return new_centers

def kmeans(features, k, maxiter=100):
    centers = dict((c,[c]) for c in features[:k])
    centers[features[k-1]] += features[k:]
    for i in xrange(maxiter):
        new_centers = assign(centers)
        new_centers = update(new_centers)
        if centers == new_centers:
            break
        else:
            centers = new_centers
    return centers

def counter(alist):
    count = defaultdict(int)
    for x in alist:
        count[x] += 1
    return dict(count)

def demo(seed=123):
    """
    The Iris dataset used in the demo is known to have a linearly separable
    class 'setosa' and 2 non linearly separable one each other.
    >>> demo()
    {'Iris-virginica': 1, 'Iris-versicolor': 29}
    {'Iris-virginica': 23}
    {'Iris-virginica': 25, 'Iris-versicolor': 21}
    {'Iris-setosa': 48}
    """
    try:
        data = load_data()
    except IOError:
        print "Missing dataset! Run:"
        print "wget http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
        sys.exit(1)
    features = data.keys()
    random.seed(seed)
    random.shuffle(features)
    clusters = kmeans(features, 4)
    print(len(clusters))
    for c in clusters:
        print counter([data[x] for x in clusters[c]])
        

if __name__ == "__main__":
    demo()