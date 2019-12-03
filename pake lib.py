#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:11:56 2019

@author: mas
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from neupy import algorithms

def normalisasi(x):
    newx = np.copy(x)
    for i in range(x.shape[1]):
        if i == 2:
            nmin = np.min(x[:, i])
            nmax = np.max(x[:, i])
            newx[:, i] = (x[:, i] - nmin) / (nmax - nmin)
    return newx

read_file = np.array(pd.read_excel('Data Skripsi.xlsx'))
data = read_file[:, 1:-1]
target = read_file[:,-1]
normalized = normalisasi(data)

for i in range(target.size):
    if target[i].lower() == 'narko':
        target[i] = 0
    elif target[i].lower() == 'psiko':
        target[i] = 1
    elif target[i].lower() == 'zat adiktif':
        target[i] = 2
        
lvqnet = algorithms.LVQ2(n_inputs=normalized.shape[1], n_classes=3, verbose=True, epsilon=0.3)
lvqnet.train(normalized, target, epochs=100)
#lvqnet.predict(normalized)