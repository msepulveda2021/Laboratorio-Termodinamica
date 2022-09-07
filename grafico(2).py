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

fig, ax = plt.subplots(nrows=1, ncols=2, constrained_layout=True)

ax.plot(x_50,y_50)
ax.plot(x_150,y_150)
ax.plot(x_250,y_250)

plt.show()

