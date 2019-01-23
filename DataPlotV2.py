import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

data = pd.read_csv('data4m.txt',sep=",",header=None)
ref = 2259.41
cons = 0.114
x = np.asarray(data.iloc[:,0]/3600)
y = np.asarray(data.iloc[:,1])
OD = np.zeros(np.size(y))

for idx, i in enumerate(y):
    OD[idx]=((-np.log10(i/ref)+0.03566)/0.2143)

LimitedOD = OD[120:720]
LimitedTime = x[120:720]

pc = np.polyfit(LimitedTime,LimitedOD,20)
p = np.poly1d(pc)

dx = np.polyder(p)
lx = dx(LimitedTime)
q = lx/LimitedOD

#cons = np.average(q)
#print(cons)

figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')

l = [cons]*LimitedTime.size

plt.plot(LimitedTime,q,'g-',label='Growth rate pr time')
plt.plot(LimitedTime,l,'b-',label='Modeled growth rate 0.114')
plt.grid(axis='both')
plt.xlabel('Time (hours)')
plt.ylabel('Mu')
plt.title('Mu vs. Time (Strain 2)')
plt.yticks(np.arange(-0.15, 0.25, 0.05))
plt.legend()
plt.show