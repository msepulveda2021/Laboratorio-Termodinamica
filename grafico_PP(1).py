import numpy as np
import matplotlib.pyplot as plt

#------------------PARTICULAS PESADAS------------------------------------------------------------------------------------------------------

# Datos 300k, n50, p_pesadas
x_11 = np.array([15,13,11,9,7,5])
y_11 = np.array([3.85,4.5,5.3,6.45,8.35,11.65])
x_11err = 0.5
y_11err = np.array([0.45,0.4,0.5,0.45,0.45,0.45])

# Datos 300k, n100, p_pesadas
x_21 = np.array([15,13,11,9,7,5])
y_21 = np.array([7.75,8.95,10.65,13,16.75,23.45])
x_21err = 0.5
y_21err = np.array([0.45,0.45,0.45,0.4,0.45,0.35])

# Datos 300k, n150, p_pesadas
x_31 = np.array([15,13,11,9,7,5])
y_31 = np.array([11.65,13.5,15.95,19.45,25.1,35])
x_31err = 0.5
y_31err = np.array([0.3,0.45,0.45,0.45,0.4,0.4])

# Datos 600k, n50, p_pesadas
x_12 = np.array([15,13,11,9,7,5])
y_12 = np.array([7.8,9,10.65,12.9,16.65,23.35])
x_12err = 0.5
y_12err = np.array([0.45,0.45,0.45,0.4,0.35,0.4])

# Datos 600k, n100, p_pesadas
x_22 = np.array([15,13,11,9,7,5])
y_22 = np.array([15.5,18,21.2,26.1,33.6,46.75])
x_22err = 0.5
y_22err = np.array([0.4,0.4,0.35,0.4,0.4,0.35])

# Datos 600k, n150, p_pesadas
x_32 = np.array([15,13,11,9,7,5])
y_32 = np.array([23.35,26.95,31.8,39,50.25,70.1])
x_32err = 0.5
y_32err = np.array([0.4,0.35,0.35,0.4,0.3,0.25])

#-------PARTICULAS LIGERAS-----------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------

plt.figure()
fig, ax = plt.subplots(figsize = (5,7))

#--------------------------------------------------------------------------------------------------------------------

L1 = ax.errorbar(x_11, y_11, x_11err, y_11err, linestyle='dotted', marker='P', markersize=10, color='orange')
L2 = ax.errorbar(x_21, y_21, x_21err, y_21err, linestyle='dotted', marker='P', markersize=10, color='darkorange')
L3 = ax.errorbar(x_31, y_31, x_31err, y_31err, linestyle='dotted', marker='P', markersize=10, color='darkgoldenrod')
L4 = ax.errorbar(x_12, y_12, x_12err, y_12err, linestyle='-', marker='o', markersize=7, color='lightsteelblue')
L5 = ax.errorbar(x_22, y_22, x_22err, y_22err, linestyle='-', marker='o', markersize=7, color='cornflowerblue')
L6 = ax.errorbar(x_32, y_32, x_32err, y_32err, linestyle='-', marker='o', markersize=7, color='royalblue')

#----------------------------------------------------------------------------------------------------------------------------

ax.legend((L1, L2, L3, L4, L5, L6), 
          ('T=300K, n=50','T=300K, n=100','T=300K, n=150','T=600K, n=50', 'T=600K, n=100', 'T=600K, n=150'), loc='upper right', shadow = True)
ax.set_xlabel('Volumen (nm)')
ax.set_ylabel('Presión (atm)')
ax.set_title('Partículas Pesadas')

archivo_1 = 'grafico-PP.pdf'
plt.savefig(archivo_1)

plt.show()
