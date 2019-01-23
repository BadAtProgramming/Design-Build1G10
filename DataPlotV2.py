import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

data = pd.read_csv('data3m2.txt',sep=",",header=None)
ref = 2259.41
cons = 0.08
x = np.asarray(data.iloc[:,0]/3600)
y = np.asarray(data.iloc[:,1])
OD = np.zeros(np.size(y))

for idx, i in enumerate(y):
    OD[idx]=((-np.log10(i/ref)+0.03566)/0.2143)

pc = np.polyfit(x,OD,20)
p = np.poly1d(pc)

dx = np.polyder(p)
lx = dx(x)
q = lx/OD


figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')

l = [cons]*x.size

plt.plot(x,q,'g-',label='Growth rate pr time')
plt.plot(x,l,'b-',label='Modeled growth rate')
plt.grid(axis='both')
plt.xlabel('Time (hours)')
plt.ylabel('Mu')
plt.title('Mu vs. Time')
plt.yticks(np.arange(-0.05, 0.1, 0.05))
plt.legend()
plt.show