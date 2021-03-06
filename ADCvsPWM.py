#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:25:22 2019

@author: Josie
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def DataPlot():
    filename=input("Name of file you want to plot: ")
    data=pd.read_csv(filename,sep=";",header=None)
    DM=np.asmatrix(data)
    print(data)
    x=np.arange(0,1024)
    y=np.array(DM[0,:])
    y=np.transpose(y)
    plt.plot(x, y, color='red')
    plt.xlabel('PWM Rate (LED)')
    plt.ylabel('ADC (Light Sensor)')
    plt.title('Yeast Cell Growth')
    #plt.xticks(range(1,x+1))
    #plt.yticks(range(1,y+1))
    plt.show()
DataPlot()

""" PWM rate is the freq that has a max of 255, starting from 0"""
