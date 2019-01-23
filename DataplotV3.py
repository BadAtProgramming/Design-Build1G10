import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import scipy.optimize
import math

data = pd.read_csv('data3m.txt',sep=",",header=None)
ref = 2228.26
#cons = 0.08
x = np.asarray(data.iloc[:,0]/3600)
y = np.asarray(data.iloc[:,1])
OD = np.zeros(np.size(y))

for idx, i in enumerate(y):
    OD[idx]=((-np.log10(i/ref)+0.03566)/0.2143)

figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
plt.rcParams.update({'font.size': 22})

LimitedOD = OD[120:1500]
LimitedTime = x[120:1500]
#Calculate coefficients of exponential fit
coeff = scipy.optimize.curve_fit(lambda t,a,b: a*np.exp(b*t),LimitedTime,LimitedOD,  p0=(4, 0.1))
#Calculate DoubleTime
DoubleTime = math.log10(2)/(math.log10(1+coeff[0][1]))
#Insert coefficients into standard exp equation
print(DoubleTime)

Curve = coeff[0][0]*np.exp(coeff[0][1]*LimitedTime)
plt.plot(x, OD, 'r-',label='OD')
plt.plot(LimitedTime,Curve,'g-',label='Exponential Regression \n a=0.611 and b=0.078',linewidth=3)
plt.grid(axis='both')
plt.xlabel('Time (hours)')
plt.ylabel('OD')
plt.title('OD vs. Time (Strain 1)')
plt.legend()
plt.show
print(coeff)