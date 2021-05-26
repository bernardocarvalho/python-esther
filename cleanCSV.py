#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file take the csv files writen by the Red Pitaya streaming application 
https://redpitaya.readthedocs.io/en/latest/appsFeatures/apps-featured/streaming/appStreaming.html

and removes the 4 zeros that appear each 16384 samples


"""
import sys
#import matplotlib as plt
import numpy as np
import matplotlib.pyplot as plt

    
if len(sys.argv) > 1:
    filen = str(sys.argv[1])
else:
    filen = 'dataDMA16'

#filen ='data_file_2021-05-26_15-35-28'
#data = np.fromfile(filen + '.bin', offset=20, dtype='int16')
data = np.genfromtxt(filen + '.csv')
idx=np.arange(-5,len(data),16384, dtype=np.intp)
lastGood= data[idx]
idx=np.arange(-4,len(data),16384, dtype=np.intp)
data[idx]=lastGood
idx=np.arange(-3,len(data),16384, dtype=np.intp)
data[idx]=lastGood
idx=np.arange(-2,len(data),16384, dtype=np.intp)
data[idx]=lastGood
idx=np.arange(-1,len(data),16384, dtype=np.intp)
data[idx]=lastGood

np.savetxt(filen + '_clean.csv',data, fmt='%i')

if len(sys.argv) > 2:
    fig = plt.figure()
    plt.plot(data)  
    plt.show()
