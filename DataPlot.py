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
    Ref=float(input("Measured Reference Light Intensity: "))
    data=pd.read_csv(filename,sep=",",header=None)
    DM=np.asmatrix(data)
    y=np.array(DM[:,1])
    """l=len(y)
    x=np.arange(0,l,1)"""
    x=np.array(DM[:,0])
    y=np.transpose(y)
    OD=np.zeros(np.size(y))
    print(y)
    for i in y:
        OD=-np.log10(i/Ref)
        #Can also be written as np.log10(Ref/id)
    print(OD)
    NOD=(OD+0.03566)/0.2143
    print(NOD)
    plt.plot(x, NOD, color='red',markersize=0.5)
    plt.grid(axis='both')
    plt.xlabel('Time (seconds)')
    plt.ylabel('OD')
    plt.title('OD vs. Time (Overnight 3 Yeast 1)')
    #plt.xticks(range(1,x+1))
    #plt.yticks(range(1,y+1))
    plt.show()
DataPlot()    
    
    
   
    