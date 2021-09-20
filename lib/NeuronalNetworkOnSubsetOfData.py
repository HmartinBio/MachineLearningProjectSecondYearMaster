#!/bin/python3

# -*-coding:utf-8 -*-

"""Importing librairies"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from numpy import *
import math
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

from keras.utils import to_categorical
from keras.models import Model
from keras.layers import Dense, Input

"""Creating filename of the file"""

dataFile = "../output/2264GenesDataframe/newDataFrame.csv"

""" Creating a counter Line"""

counterLine = 0

"""Reading the file"""

openingDataFile = open(dataFile, 'r')

"""Counting the lines"""

while(openingDataFile.readline()):
    counterLine += 1

"""Closing the file"""

openingDataFile.close()

"""ReOpening the file"""

openingDataFile = open(dataFile, 'r')

"""Creating a dictionnary of Labels"""

dictionnaryLabels = {}

""" Reading header line and creating items of dictionnary"""

line = openingDataFile.readline().replace('\n', '')
lineSplitted = line.split(',')
lineSplitted[0] = "X"

listOfHeaders = lineSplitted
listOfData = []


"""Reading file and assigning data to item"""

for i in range(0, counterLine - 1):
    line = openingDataFile.readline().replace('\n', '')
    lineSplitted = line.split(',')
    listOfData.append(lineSplitted)

openingDataFile.close()

"""Creating a dataframe of data """

dataFrameOfData = pd.DataFrame(listOfData, columns= listOfHeaders)

"""Deleting unused variables"""

del(listOfData)
del(listOfHeaders)

"""Creating a list of labels"""

columnLabels = dataFrameOfData["Labels"]
uniqColumnLabels = list(columnLabels.drop_duplicates())

"""Selecting only data from the dataframe"""

dataFrameOfData = dataFrameOfData.iloc[:, 1:len(dataFrameOfData.columns) - 1]

"""Assigning numbers to labels to categorize Labels"""

for i,j in zip(uniqColumnLabels, range(0, len(uniqColumnLabels))):
    dictionnaryLabels[i] = j


"""Categorisating Labels"""

listOfLabels = []

for i in columnLabels:
    listOfLabels.append(dictionnaryLabels[i])

listOfLabels = to_categorical(listOfLabels)


"""Splitting data in training and testing datasets"""

X_train, X_test, Y_train, Y_test = train_test_split(dataFrameOfData, listOfLabels, test_size=0.33, random_state=42, stratify = columnLabels)

"""Deleting unused variables"""

del(dataFrameOfData)
del(columnLabels)
del(dictionnaryLabels)
del(listOfLabels)


"""Importing Lasso Regularization Term"""

from keras.regularizers import l1

"""Creating Neural Network models"""

def initModel(numberOfLayers = 3, regularizationTerm = 0):
    init = 'random_uniform'
    input_layer = Input(shape=(2264,))

    if (numberOfLayers == 3):
        if (regularizationTerm != 0):
            mid_layer = Dense(555, activation = 'relu', kernel_initializer = init, activity_regularizer=l1(regularizationTerm))(input_layer)
            output_layer = Dense(5, activation = 'softmax', kernel_initializer = init)(mid_layer)
        
        else:
            mid_layer = Dense(555, activation = 'relu', kernel_initializer = init)(input_layer)
            output_layer = Dense(5, activation = 'softmax', kernel_initializer = init)(mid_layer)

    else:
        if (regularizationTerm != 0):
            mid_layer = Dense(1064, activation = 'relu', kernel_initializer = init)(input_layer)
            mid_layer_2 = Dense(555, activation = 'relu', kernel_initializer = init, activity_regularizer=l1(regularizationTerm))(mid_layer)
            output_layer = Dense(5, activation = 'softmax', kernel_initializer = init)(mid_layer_2)
        else:
            mid_layer = Dense(1064, activation = 'relu', kernel_initializer = init)(input_layer)
            mid_layer_2 = Dense(555, activation = 'relu', kernel_initializer = init)(mid_layer)
            output_layer = Dense(5, activation = 'softmax', kernel_initializer = init)(mid_layer_2)


    model = Model(input = input_layer, output = output_layer)
    model.compile(optimizer='sgd',loss='binary_crossentropy',metrics=['accuracy'])
    return(model)


""" Saving values for Learning Curve"""

training_accuracy = []
testing_accuracy = []
index = []

"""Creating a function to draw accuracy curves"""

def tracingPlots(epochsNumber = 100, numberOfLayers = 3, regularizationTerm = 0, figureName = "False"):

    for i in range(50, X_train.shape[0], 20):
        # Model initialization
        model = initModel(numberOfLayers, regularizationTerm)
        # Model fit
        model.fit(X_train.iloc[1:i,:],Y_train[1:i,:], batch_size=32, epochs=epochsNumber, verbose=2, validation_split=0.1)
        # Prediction with training dataset
        Z_train = model.predict(X_train.iloc[1:i,:])
        # Prediction with testing dataset
        Z_test = model.predict(X_test)
        prediction_train = np.argmax(Z_train, axis = 1)
        prediction_test = np.argmax(Z_test, axis = 1)
        # Accuracy
        training_accuracy.append(accuracy_score(np.argmax(Y_train[1:i,:], axis = 1), prediction_train))
        testing_accuracy.append(accuracy_score(np.argmax(Y_test, axis = 1), prediction_test))
        index.append(i)

    """Drawing Accuracy Curve"""
    
    figure = plt.figure()
    plt.plot(index, training_accuracy, label = 'Training')
    plt.plot(index, testing_accuracy, label = 'Testing')
    plt.legend()
    
    if (figureName != "False"):
        plt.savefig("../figures/{}.eps".format(figureName), dpi = 600, format = "eps", bbox_inches='tight')

    else:
        plt.show()

    plt.close()

"""Constructing a function to draw the loss curves"""

def tracingLearningCurve(epochsNumber = 100, numberOfLayers = 3, regularizationTerm = 0, figureName = "False"):
    model = initModel(numberOfLayers, regularizationTerm)
    history = model.fit(X_train,Y_train, batch_size=32, epochs=epochsNumber, verbose=2, validation_split=0.1)
    figure = plt.figure()
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    
    if (figureName != "False"):
        plt.savefig("../figures/{}.eps".format(figureName), dpi = 600, format = "eps", bbox_inches='tight')
    
    else:
        plt.show()

    plt.close()


"""Saving curves"""

tracingLearningCurve(numberOfLayers=4, figureName = "LearningCurveWithFourLayers")
tracingLearningCurve(numberOfLayers=4, regularizationTerm=0.01, figureName = "LearningCurveWithFourLayersAndL1Equal0.01")
tracingLearningCurve(numberOfLayers=4, regularizationTerm=0.1, figureName = "LearningCurveWithFourLayersAndL1Equal0.1")

tracingLearningCurve(numberOfLayers=3, figureName = "LearningCurveWithThreeLayers")
tracingLearningCurve(numberOfLayers=3, regularizationTerm=0.01, figureName = "LearningCurveWithThreeLayersAndL1Equal0.01")
tracingLearningCurve(numberOfLayers=3, regularizationTerm=0.1, figureName= "LearningCurveWithThreeLayersAndL1Equal0.1")

tracingPlots(epochsNumber=100, numberOfLayers=4, figureName = "AccuracyCurveWith4Layers100Epochs4Layers")
tracingPlots(epochsNumber = 50, numberOfLayers=4, figureName = "AccuracyCurveWith4Layers50Epochs4Layers")
tracingPlots(epochsNumber = 20, numberOfLayers=4, figureName = "AccuracyCurveWith4Layers20Epochs4Layers")

tracingPlots(epochsNumber = 20, numberOfLayers=4, regularizationTerm=0.01, figureName = "AccuracyCurveWith4Layers20EpochsAndL1Equal0.01")
tracingPlots(epochsNumber = 20, numberOfLayers=4, regularizationTerm=0.1, figureName = "AccuracyCurveWith4Layers20EpochsAndL1Equal0.1")

tracingPlots(epochsNumber=100, numberOfLayers=3, figureName = "AccuracyCurveWith3Layers100Epochs")
tracingPlots(epochsNumber=50, numberOfLayers=3, figureName = "AccuracyCurveWith3Layers50Epochs")
tracingPlots(epochsNumber=20, numberOfLayers=3, figureName = "AccuracyCurveWith3Layers2OEpochs")

tracingPlots(epochsNumber=20, numberOfLayers=3, regularizationTerm=0.01, figureName = "AccuracyCurveWith3Layers20EpochsL1Equal0.01")
tracingPlots(epochsNumber=20, numberOfLayers=3, regularizationTerm=0.1, figureName = "AccuracyCurveWith3Layers20EpochsL1equal0.1")

tracingPlots(epochsNumber=100, numberOfLayers=4, figureName = "AccuracyCurveWith4Layers100EpochsL1Equal0.01", regularizationTerm=0.01)
tracingPlots(epochsNumber=100, numberOfLayers=4, figureName = "AccuracyCurveWith4Layers100EpochsL1Equal0.1", regularizationTerm=0.1)
tracingPlots(epochsNumber = 50, numberOfLayers=4, figureName = "AccuracyCurveWith4Layers50EpochsL1Equal0.01", regularizationTerm=0.01)
tracingPlots(epochsNumber = 50, numberOfLayers=4, figureName = "AccuracyCurveWith4Layers50EpochsL1Equal0.1", regularizationTerm=0.1)

tracingPlots(epochsNumber=100, numberOfLayers=3, figureName = "AccuracyCurveWith3Layers100EpochsL1Equal0.01", regularizationTerm=0.01)
tracingPlots(epochsNumber=100, numberOfLayers=3, figureName = "AccuracyCurveWith3Layers100EpochsL1Equal0.1", regularizationTerm=0.1)
tracingPlots(epochsNumber=50, numberOfLayers=3, figureName = "AccuracyCurveWith3Layers50EpochsL1Equal0.01", regularizationTerm=0.01)
tracingPlots(epochsNumber=50, numberOfLayers=3, figureName = "AccuracyCurveWith3Layers50EpochsL1Equal0.1", regularizationTerm=0.1)
