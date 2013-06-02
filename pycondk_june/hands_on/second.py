#!/usr/bin/env

import numpy as np
import sklearn
from sklearn.svm import SVC
from numpy import genfromtxt
from sklearn import cross_validation
from sklearn import preprocessing as pp
from sklearn import cross_validation as cv
from sklearn.ensemble import ExtraTreesClassifier

testSet = genfromtxt('test.csv', delimiter=',')
trainingSet = genfromtxt('train.csv', delimiter=',')
trainingLabels = genfromtxt('trainLabels.csv', delimiter=',')

trainingSet, testSet, trainingLabels, testLabels = cross_validation.train_test_split(
	trainingSet, trainingLabels, test_size=0.3, random_state=0)

clf = SVC()
clf.fit(trainingSet, trainingLabels)
prediction = clf.predict(testSet)

np.savetxt('result.csv', prediction, fmt='%i', delimiter=',')


truePos = 0
trueNeg = 0
falsePos = 0
falseNeg = 0
totalPositives = 0

for i in range(len(testLabels)):
	if testLabels[i] == True and prediction[i] == True:
		truePos = truePos + 1
		totalPositives = totalPositives + 1
	if testLabels[i] == True and prediction[i] == False:
		falseNeg = falseNeg + 1
		totalPositives = totalPositives + 1
	if testLabels[i] == False and prediction[i] == True:
		falsePos = falsePos + 1
	if testLabels[i] == False and prediction[i] == False:
		trueNeg += 1


#http://streamhacker.com/2010/05/17/text-classification-sentiment-analysis-precision-recall/
#http://en.wikipedia.org/wiki/Accuracy_and_precision#Accuracy_and_precision_in_binary_classification

print ""
print "total number of positives: " + str(totalPositives)
print "total number of negatives: " + str(len(testSet) - totalPositives)
print "truePos: " + str(truePos)
print "trueNeg: " + str(trueNeg)
print "hit: " + str(truePos + trueNeg) + " out of " + str(len(testSet)) + ", accuracy is: " + str((trueNeg + truePos)*1.0/len(testSet))
print "positive recall is: " + str(truePos) + " out of " + str(totalPositives) + ": " + str(truePos * 1.0 / totalPositives) 
print "negative recall is: " + str(trueNeg) + " out of " + str(len(testSet) - totalPositives) + ": "  + str(trueNeg * 1.0 / (len(testSet) - totalPositives)) 

print ""
print "falsePos: " + str(falsePos)
print "falseNeg: " + str(falseNeg)
print "positive precision is: " + str(truePos) + " out of " + str((truePos + falsePos)) + ": " + str(truePos * 1.0 / (truePos + falsePos))
print "negative precision is: " + str(trueNeg) + " out of " + str((trueNeg + falseNeg)) + ": " + str(trueNeg * 1.0 / (trueNeg + falseNeg))
