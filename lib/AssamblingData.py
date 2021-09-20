#!/usr/bin/python3

# -*- coding:utf-8 -*-

import os 

'''Changing pathway to data pathway'''

os.chdir("../data")

''' Opening labels file '''

fichier_labels = open('labels.csv', 'r')
counter_fichier_labels = 0
final_file = '../output/CompleteData.csv'
openingFinalFile = open(final_file, 'w')
openingFinalFile.close()

''' Counting the number of rows in the file'''

while(fichier_labels.readline()):
    counter_fichier_labels += 1

fichier_labels.close()


''' Reopening the labels file '''

fichier_labels = open('labels.csv', 'r')

''' Opening data file '''

fichier_data = open('data.csv', 'r')

"""Assambling data in the destination file"""

for i in range(0, counter_fichier_labels):
    if (i == 0):
        fichier_labels.readline()
        lineData = fichier_data.readline().replace('\n', '')
        lineData = lineData.split(',')
        lineData.append('Labels')
        lineData = ','.join(lineData)
        open(final_file, 'a').write(lineData + '\n')

    
    else:
        lineLabels = fichier_labels.readline().replace('\n', '')
        lineData = fichier_data.readline().replace('\n', '')
        lineLabels = lineLabels.split(',')
        lineData = lineData.split(',')
        lineData.append(lineLabels[1])
        lineData = ','.join(lineData)
        open(final_file, 'a').write(lineData + '\n')


"""Closing data files"""

fichier_data.close()
fichier_labels.close()
