import numpy as np 
import matplotlib.pyplot as plt

plt.style.use('seaborn')

datos5_2 = np.genfromtxt('datos-5-2.txt')

al_t_100 = datos5_2[:,0]
al_T_100 = datos5_2[:,1]
al_t_150 = datos5_2[:,2]
al_T_150 = datos5_2[:,3]
al_t_200 = datos5_2[:,4]
al_T_200 = datos5_2[:,5]

plt.plot(al_t_100, al_T_100, label='100 [g] de alcohol')
plt.plot(al_t_150, al_T_150, label='150 [g] de alcohol')
plt.plot(al_t_200, al_T_200, label='200 [g] de alcohol')

plt.hlines(78.3, 0, 70, linestyles=(0,(1,1)))

plt.legend(prop={'size':11}, loc='lower right')
plt.xlabel('Tiempo [s]')
plt.ylabel('Temperatura [ºC]')

plt.savefig('lol.pdf')