#!/bin/python3

# -*- coding:utf-8 -*-

"""Loading librairies"""

import os 
import subprocess

"""Changing Folder"""

os.chdir("lib")

"""Executing scripts"""

subprocess.call("python3 AssamblingData.py", shell=True)
subprocess.call("./VarianceGenes.R", shell=True)
subprocess.call("python3 PCAVisualisation.py", shell=True)
subprocess.call("python3 UMAPVisualisation.py", shell=True)
subprocess.call("python3 NeuronalNetworkOnSubsetOfData.py", shell=True)
subprocess.call("python3 SimpleNeuronalNetwork.py" , shell = True)
