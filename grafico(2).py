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

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig.suptitle()

ax1.plot(x_50, y_50)
ax1.set_xlabel()
ax1.set_ylabel()

ax2.plot(x_150, y_150)
ax2.set_xlabel()
ax2.set_ylabel()

ax3.plot(x_250, y_250)
ax3.set_xlabel()
ax3.set_ylabel()

plt.show()
