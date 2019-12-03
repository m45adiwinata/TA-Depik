#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 04:27:52 2019

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

def nonlin(x,deriv=False):
	if(deriv==True):
	    return x*(1-x)

	return 1/(1+np.exp(-x))

read_file = np.array(pd.read_excel('Data Skripsi.xlsx'))
data = read_file[:, 1:-1]
target = read_file[:,-1]
normalized = normalisasi(data)
predictions = []
for i in range(target.size):
    if target[i].lower() == 'narko':
        target[i] = 1
        predictions.append([1, 0, 0])
    elif target[i].lower() == 'psiko':
        target[i] = 2
        predictions.append([0, 1, 0])
    elif target[i].lower() == 'zat adiktif':
        target[i] = 3
        predictions.append([0, 0, 1])
predictions = np.array(predictions)
learning_rate = 0.1
max_epoh = 100
jml_neuron = 8

inputlayer = 2*np.random.random((normalized.shape[1], jml_neuron)) - 1
hiddenlayer = 2*np.random.random((jml_neuron, predictions.shape[1])) - 1

losses = []
for i in range(max_epoh):
    flag = False
    for j in range(normalized.shape[0]):
        #ALUR MAJU BACKPROPAGATION
        X = np.array([normalized[j]], dtype=float)
        f1 = nonlin(np.dot(X, inputlayer))
        f2 = nonlin(np.dot(f1, hiddenlayer))
        
        #PERHITUNGAN LOSS PREDICTION
        f2_error = [predictions[j]] - f2
        loss = np.mean(np.abs(f2_error))
        
        if j == 0:
            print("loss:" + str(loss))
            losses.append(loss)
        
        #PERHITUNGAN NILAI PENGUBAH BOBOT
        f2_delta = f2_error*nonlin(f2,deriv=True)
        f1_error = f2_delta.dot(hiddenlayer.T)
        f1_delta = f1_error * nonlin(f1,deriv=True)
        
        #PENGUBAHAN BOBOT
        hiddenlayer += learning_rate * f1.T.dot(f2_delta)
        inputlayer += learning_rate * X.T.dot(f1_delta)

#TESTING
X = np.array(normalized, dtype=float)
f1 = nonlin(np.dot(X, inputlayer))
f2 = nonlin(np.dot(f1, hiddenlayer))
f2_error = predictions - f2
loss = np.mean(np.abs(f2_error))
akurasi = (1 - loss) * 100
print("Akurasi testing : %.2f" % akurasi)
plt.title("Grafik Loss")
plt.xlabel("Epoh")
plt.ylabel("Loss")
plt.plot(losses)