#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 15:54:13 2018

@author: bernardo carvalho
#https://github.com/ZipCPU/dspfilters
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# IIR moving average with C length
def mavg_iir(x, C):
    a = [ 1, -1 ]
    b = np.concatenate(([1], np.zeros(C-1,), [-1])) / C
    y=signal.lfilter(b, a, x)
    return y

def lp_filter_resp(x, order, Wn):
    b, a = signal.butter(order, Wn, 'low')
    y=signal.lfilter(b, a, x)
    return y

# Dif  node where time of dif-ferentiation (parameter F) is usually 
#equivalent to the leading edge of the signal from the pre- amplifier.   
def diff_fir(x, F):
    a = [1]
    b = np.concatenate(([1], np.zeros(F-1,), [-1]))
    y=signal.lfilter(b, a, x)
    return y

def gauge_signal(L,n, Wn, noiseLevel):
    #second order response with Wn normalized cut
    # L length heaviside, n delay
    x = np.concatenate([np.zeros(n,), np.ones(L-n,)]) 
    y = lp_filter_resp(x, 2, Wn) + np.random.randn(len(x)) * noiseLevel
    return x, y 

if __name__ == "__main__":
    #
    Fs= 250.0  # in MSPS
    Ts =1/Fs # in us  
    #Wn = 0.004   
    Wn = 0.001 
    C = 5 # Moving average taps
    F = 250 #np.int(1/Wn) #usually #equivalent to the leading edge of the signal
    L  = np.int(Fs * 90) # number total samples= 50 us
    t=np.arange(L) * Ts - 10.0
    n1 = np.int(10.0 * Fs)
    noise1 = 0.01 # 5%
    x1, y1 =gauge_signal(L,n1, Wn, noise1)
    #return x, y 
 #   x1 = np.concatenate([np.zeros(n1,), np.ones(L-n1,)]) 
 #   y1 = lp_filter_resp(x1, 2, Wn) + np.random.randn(len(x1)) * noise1
    
    y1_int = (y1*512.0).astype(np.int16)
    #f = open('data_hex.txt', 'w')
    #for i in range (len(y1)):
    #    f.write("%04x\n" %(0xFFFF &y1_int[i]))
    #f.close()
    #np.savetxt('/Users/bernardo/iVerilog/data_files/in_data.txt', y1_int,fmt='%d')
    
    #https://www.devdungeon.com/content/working-binary-data-python#hex
    n2 = np.int(40.0 * Fs)
    noise2 = 0.01 # 5%
    x2 = np.concatenate([np.zeros(n2,), np.ones(L-n2,)]) 
    y2 = lp_filter_resp(x2, 2, Wn) + np.random.randn(len(x2)) * noise2
    
    
    n3 = np.int(70.0 * Fs)
    noise3 = 0.02 # 5%
    x3 = np.concatenate([np.zeros(n3,), np.ones(L-n3,)]) 
    y3 = lp_filter_resp(x3, 2, Wn) + np.random.randn(len(x3)) * noise3
    
    y3m = mavg_iir(y3, C)
    y3f = diff_fir(y3m, F)
    y3ff = diff_fir(y3f, F)
    
    plt.clf()
    
    l1, l2 = plt.plot(t,x1, t,y1)
    
    l3, l4 = plt.plot(t, x2, t,y2)
    
    l5, l6, l7 = plt.plot(t, x3, t,y3,  t, y3ff)
    #plt.axis["xzero"].set_visible(True)
    
    plt.plot([0, 40], [0.6, 0.6], 'k-.')
    
    plt.legend((l1, l3, l5), ('sensor 1', 'sensor 2', 'sensor 3'), loc='lower left', shadow=True)
    
    plt.xlabel('T / us')
    plt.title('Section 7 Pressures v=10km/s')
    plt.show()
# yo=np.loadtxt('/Users/bernardo/iVerilog/esther-timing-verilog/data_files/out_data.txt')
    
#plt.plot(yo);plt.legend([b,c,d], ["gauge","diff","diff2"], loc=1)
#    plotLTI([1, 5], [1, 10, 44, 120])
