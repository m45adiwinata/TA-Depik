#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:57:55 2019

@author: mas
"""

import pandas as pd
import numpy as np

read_file = np.array(pd.read_excel('Data Skripsi.xlsx'))
data = read_file[:, 1:-1]
target = read_file[:,-1]

data_narko = []
target_narko = []
data_berurut = []
for i in range(len(target)):
    if target[i].lower() == 'narko':
        data_narko.append(data[i])
        target_narko.append(target[i])
        data_berurut.append(read_file[i])

data_psiko = []
target_psiko = []
for i in range(len(target)):
    if target[i].lower() == 'psiko':
        data_psiko.append(data[i])
        target_psiko.append(target[i])
        data_berurut.append(read_file[i])
        
data_za = []
target_za = []
for i in range(len(target)):
    if target[i].lower() == 'zat adiktif':
        data_za.append(data[i])
        target_za.append(target[i])
        data_berurut.append(read_file[i])

data_berurut = np.array(data_berurut)
df = pd.DataFrame(data_berurut)
df.to_excel('Data Skripsi berurut.xlsx')
