#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:43:03 2019

@author: Josie
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def DataPlot():
    filename=input("Name of file you want to plot: ")
    data=pd.read_csv(filename,sep=";",header=None)
    DM=np.asmatrix(data)
    x=np.array(DM[:,1])
    y=np.array(DM[:,0])
    plt.plot(x, y, color='red')
    plt.xlabel('PWM Rate (LED)')
    plt.ylabel('ADC (Light Sensor)')
    plt.title('Yeast Cell Growth')
    #plt.xticks(range(1,x+1))
    #plt.yticks(range(1,y+1))
    plt.show()
    print(data)
DataPlot()    
    
    
    
    