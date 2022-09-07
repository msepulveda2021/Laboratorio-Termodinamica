import numpy as np
import matplotlib.pyplot as plt

matplotlib.use("pgf")
matplotlib.rcParams.update({

    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

#------------------------------------------------------------------------------------------------------------------------

# Datos 300k, n50, pligeras
x_11 = np.array([15,13,11,9,7,5])
y_11 = np.array([4.1,4.5,5.3,6.45,8.35,11.6])
x_11err = 0.5
y_11err = np.array([0.2,0.4,0.5,0.45,0.45,0.4])

# Datos 300k, n100, pligeras
x_21 = np.array([15,13,11,9,7,5])
y_21 = np.array([7.8,8.9,10.65,13,16.85,23.15])
x_21err = 0.5
y_21err = np.array([0.4,0.4,0.45,0.4,0.45,0.35])

# Datos 300k, n150, pligeras
x_31 = np.array([15,13,11,9,7,5])
y_31 = np.array([11.8,13.45,15.95,19.45,24.95,35.05])
x_31err = 0.5
y_31err = np.array([0.3,0.45,0.45,0.45,0.35,0.35])

# Datos 600k, n50, pligeras
x_12 = np.array([15,13,11,9,7,5])
y_12 = np.array([7.75,8.95,10.55,12.9,16.75,23.2])
x_12err = 0.5
y_12err = np.array([0.45,0.45,0.45,0.4,0.35,0.4])

# Datos 600k, n100, peligeras
x_22 = np.array([15,13,11,9,7,5])
y_22 = np.array([15.6,18,21.25,26,33.3,46.75])
x_22err = 0.5
y_22err = np.array([0.4,0.4,0.35,0.4,0.4,0.35])

# Datos 600k, n150, pligeras
x_32 = np.array([15,13,11,9,7,5])
y_32 = np.array([23.3,27.05,31.75,39,49.8,70.05])
x_32err = 0.5
y_32err = np.array([0.4,0.35,0.35,0.4,0.3,0.25])

#------------------------------------------------------------------------------------------------------------------------------------

fig, ax = plt.subplots(figsize = (5,7))

#--------------------------------------------------------------------------------------------------------------------

L1 = ax.errorbar(x_11, y_11, x_11err, y_11err, linestyle='dotted', marker='P', markersize=15, color='lime')
L2 = ax.errorbar(x_21, y_21, x_21err, y_21err, linestyle='dotted', marker='P', markersize=15, color='limegreen')
L3 = ax.errorbar(x_31, y_31, x_31err, y_31err, linestyle='dotted', marker='P', markersize=15, color='green')
L4 = ax.errorbar(x_12, y_12, x_12err, y_12err, linestyle='-', marker='o', markersize=10, color='lightcoral')
L5 = ax.errorbar(x_22, y_22, x_22err, y_22err, linestyle='-', marker='o', markersize=10, color='red')
L6 = ax.errorbar(x_32, y_32, x_32err, y_32err, linestyle='-', marker='o', markersize=10, color='firebrick')

#----------------------------------------------------------------------------------------------------------------------------

ax.legend((L1, L2, L3, L4, L5, L6), ('300K, N50','300K, N100','300K, N150','600K, N50', '600K, N100', '600K, N150'), loc='upper right', shadow = True)
ax.set_xlabel('Volumen (nm)')
ax.set_ylabel('Presion (atm)')
ax.set_title('Particulas Pesadas')

plt.show()
plt.savefig('grafico_pp.pgf')
