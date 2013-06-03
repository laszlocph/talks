#!/usr/bin/env

import numpy as np
import sklearn
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from numpy import genfromtxt


testSet = genfromtxt('test.csv', delimiter=',')
trainingSet = genfromtxt('train.csv', delimiter=',')
trainingLabels = genfromtxt('trainLabels.csv', delimiter=',')


