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
from keras.layers import Dropout

"""Creating filename of the file"""

dataFile = "../output/399GenesDataframe/newDataFrame.csv"

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

"""Creating DataFrame of Data"""

dataFrameOfData = pd.DataFrame(listOfData, columns= listOfHeaders)

"""Deleting unused variables"""

del(listOfData)
del(listOfHeaders)

"""Creating a list of labels"""

columnLabels = dataFrameOfData["Labels"]
uniqColumnLabels = list(columnLabels.drop_duplicates())

"""Taking only data from dataframe"""

dataFrameOfData = dataFrameOfData.iloc[:, 1:len(dataFrameOfData.columns) - 1]

"""Creating numbers to categorize labels"""

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


"""Importing the Ridge Regularization term"""


from keras.regularizers import l2


"""Creating Neural Network"""

def initModel():
    init = 'random_uniform'
    input_layer = Input(shape=(397,))
    
    mid_layer = Dense(6, activation = 'relu', kernel_initializer = init, kernel_regularizer=l2(0.001))(input_layer)
    mid_layer2 = Dropout(0.01, input_shape = (6,))(mid_layer)
    output_layer = Dense(5, activation = 'softmax', kernel_initializer = init)(mid_layer2)

    model = Model(input = input_layer, output = output_layer)
    model.compile(optimizer='sgd',loss='binary_crossentropy',metrics=['accuracy'])
    return(model)
        


""" Saving values for Accuracy Curve"""

training_accuracy = []
testing_accuracy = []
index = []

"""Creating a function to draw the Accuracy curves"""

def tracingPlots(figureName = "False"):

    for i in range(50, X_train.shape[0], 20):
        # Model initialization
        model = initModel()
        # Model fit
        model.fit(X_train.iloc[1:i,:],Y_train[1:i,:], batch_size=6, epochs=100, verbose=2, validation_split=0.1)
        # Prediction with training dataset
        Z_train = model.predict(X_train.iloc[i:X_train.shape[0],:])
        # Prediction with testing dataset
        Z_test = model.predict(X_test)
        prediction_train = np.argmax(Z_train, axis = 1)
        prediction_test = np.argmax(Z_test, axis = 1)
        # Accuracy
        training_accuracy.append(accuracy_score(np.argmax(Y_train[i:X_train.shape[0],:], axis = 1), prediction_train))
        testing_accuracy.append(accuracy_score(np.argmax(Y_test, axis = 1), prediction_test))
        index.append(i)

    """Drawing Accuracy curves"""
    
    figure = plt.figure()
    plt.plot(index, training_accuracy, label = 'Training')
    plt.plot(index, testing_accuracy, label = 'Testing')
    plt.legend()

    if (figureName != "False"):
        plt.savefig("../figures/{}.eps".format(figureName), dpi = 600, format = "eps", bbox_inches='tight')

    plt.close()


"""Creating a function to draw loss curves"""


def tracingLearningCurve(figureName = "False"):
    model = initModel()
    history = model.fit(X_train,Y_train, batch_size=6, epochs=100, verbose=2, validation_split=0.1, validation_data=(X_test, Y_test))
    
    """Drawing loss curves"""
    
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


"""Drawing learning curves"""

tracingPlots(figureName="BestNeuralNetworkAccuracyPlot")
tracingLearningCurve(figureName="BestNeuralNetworkLossCurve")
