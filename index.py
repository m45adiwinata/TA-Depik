#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:50:46 2019

@author: mas
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
#df = pd.DataFrame(normalized)
#df.to_excel('Data Normalisasi.xlsx')
for i in range(target.size):
    if target[i].lower() == 'narko':
        target[i] = 1
    elif target[i].lower() == 'psiko':
        target[i] = 2
    elif target[i].lower() == 'zat adiktif':
        target[i] = 3

w = np.random.random((3, 17))
learning_rate = 0.1
penurun = 0.1
window = 0.3
max_epoh = 10

akurasies = []
for e in range(max_epoh):
    jml_benar = 0
    for i in range(normalized.shape[0]):
        X = normalized[i]
        f1 = np.sqrt(np.sum(np.square(X - w[0])))
        f2 = np.sqrt(np.sum(np.square(X - w[1])))
        f3 = np.sqrt(np.sum(np.square(X - w[2])))
        distances = [f1, f2, f3]
        result = np.argmin(distances) + 1
        if target[i] == result:
            jml_benar += 1
    
    akurasi = jml_benar / target.size * 100
    print("akurasi: %.3f" % akurasi)
    akurasies.append(akurasi)
    
    for i in range(normalized.shape[0]):
        X = normalized[i]
        f1 = np.sqrt(np.sum(np.square(X - w[0])))
        f2 = np.sqrt(np.sum(np.square(X - w[1])))
        f3 = np.sqrt(np.sum(np.square(X - w[2])))
        distances = [f1, f2, f3]
        result = np.argmin(distances) + 1
        if target[i] == result:
            j = result - 1
            w[j] = X + learning_rate * (X - w[j])
        else:
            temp = np.argsort(distances)
            if distances[temp[0]] > (1-window) * distances[temp[1]] and distances[temp[1]] < (1+window) * distances[temp[0]]:
                w[temp[0]] = w[temp[0]] - learning_rate * (X - w[temp[0]])
                w[temp[1]] = w[temp[1]] + learning_rate * (X - w[temp[1]])
        learning_rate -= penurun * learning_rate

plt.title("Grafik Akurasi")
plt.xlabel("Epoh")
plt.ylabel("Akurasi")
plt.plot(akurasies)