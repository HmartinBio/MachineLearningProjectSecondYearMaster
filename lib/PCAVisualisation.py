#!/bin/python3

# -*- coding:utf-8 -*- 

""" Importing librairies """

import os 
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

"""Creating filename of the file"""

dataFile = "../output/CompleteData.csv"

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

"""Creating a dictionnary of data"""

dictionnaryData = {}

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

"""Creating dataframe from data"""

dataFrameOfData = pd.DataFrame(listOfData, columns= listOfHeaders)

"""Deleting unused variables"""

del(listOfData)
del(listOfHeaders)

"""Creating a list of labels"""

columnLabels = dataFrameOfData["Labels"]
uniqColumnLabels = list(columnLabels.drop_duplicates())

"""Selecting data from dataframe"""

dataFrameOfData = dataFrameOfData.iloc[:, 1:len(dataFrameOfData.columns) - 1]


"""Standardise data"""

dataFrameOfData = StandardScaler().fit_transform(dataFrameOfData)


"""Making PCA, Selecting the 10 first Principal Components"""

pca = PCA(n_components = 10)

principalComponents = pca.fit_transform(dataFrameOfData)

pcaColumns = []

for i in range(0, 10):
    pcaColumns.append("PCA{}".format(i))

"""Creating a new dataframe with PCA values"""

principalComponents = pd.DataFrame(data = principalComponents, columns=pcaColumns)

"""Concatening PCA values with Patients labels"""

principalComponents = pd.concat([principalComponents, columnLabels], axis = 1)


"""Drawing figure"""

listOfColors = ['b', 'g', 'r', 'c', 'm']

plt.style.use("ggplot")
plt.xlabel('Principal Component 0', fontsize = 15)
plt.ylabel('Principal Component 1', fontsize = 15)
plt.title('PCA', fontsize = 20)

for target, color in zip(uniqColumnLabels,listOfColors):
    indicesToKeep = principalComponents['Labels'] == target
    
    plt.scatter(principalComponents.loc[indicesToKeep, "PCA0"], 
                    principalComponents.loc[indicesToKeep, "PCA1"], 
                    c = color, 
                    s = 50)

plt.legend(uniqColumnLabels)
plt.grid()

"""Saving figure"""

plt.savefig("../figures/PCAFigure.eps", dpi = 600, format="eps", bbox_inches="tight")
