import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

data5_1 = np.genfromtxt('datos-5-1.txt')

agua_t = data5_1[:,0]
agua_T = data5_1[:,1]
alcohol_t = data5_1[:,2]
alcohol_T = data5_1[:,3]
benzeno_t = data5_1[:,4]
benzeno_T = data5_1[:,5]

plt.plot(agua_t, agua_T, label='agua', marker='o', markersize=4, color='royalblue')
plt.plot(alcohol_t, alcohol_T, label='alcohol', marker='o', markersize=4, color='darkred')
plt.plot(benzeno_t, benzeno_T, label='benzeno', marker='o', markersize=4, color='green')

plt.hlines(78.3, 0, 500, color='darkred', linestyles=(0,(1,1)))
plt.hlines(80.2, 0, 500, color='green', linestyles=(0,(1,1)))
plt.hlines(100, 0, 500, color='royalblue', linestyles=(0,(1,1)))

plt.xlabel('Tiempo [s]')
plt.ylabel('Temperatura [ºC]')
plt.grid(True)
plt.legend(shadow = True, prop={'size': 11}, loc='lower right')

plt.savefig('lel.pdf')