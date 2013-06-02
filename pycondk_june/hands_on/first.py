#!/usr/bin/env

import numpy as np
import sklearn
from sklearn.svm import LinearSVC
from numpy import genfromtxt


testSet = genfromtxt('test.csv', delimiter=',')
trainingSet = genfromtxt('train.csv', delimiter=',')
trainingLabels = genfromtxt('trainLabels.csv', delimiter=',')

clf = LinearSVC()
clf.fit(trainingSet, trainingLabels)
prediction = clf.predict(testSet)

np.savetxt('result.csv', prediction, fmt='%i', delimiter=',')



