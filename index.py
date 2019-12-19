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

akurasies = []
p = np.random.permutation(normalized.shape[0])
normalized = normalized[p]
target = target[p]

val_w = []
for val in range(3):
    learning_rate = 0.02
    penurun = 0.2
    window = 0.3
    max_epoh = 10
    min_lr = 0.01
    if val == 0:
        Xval = normalized[:20]
        yval = target[:20]
        Xtrain = normalized[20:]
        ytrain = target[20:]
    elif val == 1:
        Xval = normalized[94:124]
        yval = target[94:124]
        Xtrain = np.append(normalized[:94], normalized[124:], axis=0)
        ytrain = np.append(target[:94], target[124:], axis=0)
    else:
        Xval = normalized[-40:]
        yval = target[-40:]
        Xtrain = normalized[:-40]
        ytrain = target[:-40]
    val_accs = []
    w = np.random.random((3, 17))
    continue_training = True
    min_e = 0
    min_i = 0
    for e in range(max_epoh):
        jml_benar = 0
        for i in range(Xval.shape[0]):
            X = Xval[i]
            f1 = np.sqrt(np.sum(np.square(X - w[0])))
            f2 = np.sqrt(np.sum(np.square(X - w[1])))
            f3 = np.sqrt(np.sum(np.square(X - w[2])))
            distances = [f1, f2, f3]
            result = np.argmin(distances) + 1
            if yval[i] == result:
                jml_benar += 1
        
        akurasi = jml_benar / yval.size * 100
        print("akurasi fold %s: %.3f" % (val, akurasi))
        val_accs.append(akurasi)
        if continue_training == True:
            for i in range(Xtrain.shape[0]):
                X = Xtrain[i]
                f1 = np.sqrt(np.sum(np.square(X - w[0])))
                f2 = np.sqrt(np.sum(np.square(X - w[1])))
                f3 = np.sqrt(np.sum(np.square(X - w[2])))
                distances = [f1, f2, f3]
                result = np.argmin(distances) + 1
                if ytrain[i] == result:
                    j = result - 1
                    w[j] = X + learning_rate * (X - w[j])
                else:
                    temp = np.argsort(distances)
                    if distances[temp[0]] > (1-window) * distances[temp[1]] and distances[temp[1]] < (1+window) * distances[temp[0]]:
                        w[temp[0]] = w[temp[0]] - learning_rate * (X - w[temp[0]])
                        w[temp[1]] = w[temp[1]] + learning_rate * (X - w[temp[1]])
                learning_rate -= penurun * learning_rate
                if learning_rate < min_lr:
                    continue_training = False
                    min_e = e
                    min_i = i
                    break
        else:
            print("Training dihentikan pada epoh = %s dan i = %s karena learning rate mencapai minimum." % (min_e, min_i))
            
    val_w.append(w)
    akurasies.append(val_accs)

plt.title("Grafik Akurasi")
plt.xlabel("Epoh")
plt.ylabel("Akurasi")
plt.plot(akurasies[0])
plt.plot(akurasies[1])
plt.plot(akurasies[2])
plt.show()