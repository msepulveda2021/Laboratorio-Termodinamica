import numpy as np
import matplotlib.pyplot as plt

#----------------DATOS-------------------------------------------------------------------------

# gas ideal a presion constante de 5.8 atm
x_50 = np.array([300,150,225,375,450])
y_50 = np.array([10,5,7.5,12.5,15])

# gas ideal a presion constante de 18 atm
x_150 = np.array([300,150,225,375,450])
y_150 = np.array([10,5,7.5,12.5,15])

# gas ideal a presion constante de 29.2 atm
x_250 = np.array([300,150,225,375,450])
y_250 = np.array([10,5,7.5,12.5,15])

#----------------GRAFICOS----------------------------------------------------------------------

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(11,6), constrained_layout=True)

ax1.plot(x_50, y_50, marker='o')
ax1.set_xlabel('Temperatura (K)')
ax1.set_ylabel('Volumen (nm)')
ax1.set_title('Simulación 2')

ax2.plot(x_150, y_150, marker='o')
ax2.set_xlabel('Temperatura (K)')
ax2.set_ylabel('Volumen (nm)')
ax2.set_title('Simulación 3')

ax3.plot(x_250, y_250, marker='o')
ax3.set_xlabel('Temperatura (K)')
ax3.set_ylabel('Volumen (nm)')
ax3.set_title('Simulación 4')

plt.show()
plt.savefig('grafico(2,3,4).pdf')
