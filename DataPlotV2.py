import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = pd.read_csv(input("Name of file: "),sep=",",header=None)
ref = float(input("Input initial value: "))
x = np.asarray(data.iloc[:,0])
y = np.asarray(data.iloc[:,1])
OD=np.zeros(np.size(y))

for idx, i in enumerate(y):
    OD[idx]=((-np.log10(i/ref)+0.03566)/0.2143)

def func(x,a,b,c):
    return a*b**x+c    

popt, pcov = curve_fit(func, x, y)

plt.plot(x, func(x, *popt), 'g--')

plt.show