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
    #change back to ';' 
    data=pd.read_csv(filename,sep=",",header=None)
    DM=np.asmatrix(data)
    y=np.array(DM[:,0])
    l=len(y)
    x=np.arange(0,l,1)
    y=np.transpose(y)
    OD=np.zeros(np.size(y))
    for id in y:
        OD=-np.log10(id/Ref)
        #Can also be written as np.log10(Ref/id)
    plt.plot(x, OD, color='red',markersize=0.5)
    plt.xlabel('Time (min)')
    plt.ylabel('OD')
    plt.title('Yeast Cell Growth (OD vs. Time)')
    #plt.xticks(range(1,x+1))
    #plt.yticks(range(1,y+1))
    plt.show()
DataPlot()    
    
    
    
    