#!/bin/python3

# -*- coding:utf-8 -*- 

""" Importing librairies """

import os 
import pandas as pd
import umap
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

"""Creating Dataframe"""

dataFrameOfData = pd.DataFrame(listOfData, columns= listOfHeaders)

"""Deleting variables which one don't serve anymore"""

del(listOfData)
del(listOfHeaders)

"""Saving name of Labels in a list"""

columnLabels = dataFrameOfData["Labels"]
uniqColumnLabels = list(columnLabels.drop_duplicates())

"""Selecting only data and not labels in the dataframe"""

dataFrameOfData = dataFrameOfData.iloc[:, 1:len(dataFrameOfData.columns) - 1]


"""Standardise data"""

dataFrameOfData = StandardScaler().fit_transform(dataFrameOfData)


"""Making UMAP"""

reducer = umap.UMAP()


embedding = reducer.fit_transform(dataFrameOfData)

"""Creating a new dataframe after the use of UMAP"""

dataFrameOfData = pd.DataFrame(data = embedding, columns = ["UMAP0", "UMAP1"])

"""Concatening UMAP values with Labels for each patient"""

dataFrameOfData = pd.concat([dataFrameOfData, columnLabels] , axis = 1)


"""Drawing figure"""

listOfColors = ['b', 'g', 'r', 'c', 'm']

plt.style.use("ggplot")
plt.xlabel('UMAP0', fontsize = 15)
plt.ylabel('UMAP1', fontsize = 15)
plt.title('UMAP', fontsize = 20)

for target, color in zip(uniqColumnLabels,listOfColors):
    indicesToKeep = dataFrameOfData['Labels'] == target
    
    plt.scatter(dataFrameOfData.loc[indicesToKeep, "UMAP0"], 
                    dataFrameOfData.loc[indicesToKeep, "UMAP1"], 
                    c = color, 
                    s = 50)

plt.legend(uniqColumnLabels)
plt.grid()

"""Saving figure"""

plt.savefig("../figures/UMAPFigure.eps", dpi = 600, format = "eps", bbox_inches='tight')
