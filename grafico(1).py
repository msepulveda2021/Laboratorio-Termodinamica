import numpy as np
import matplotlib.pyplot as plt

#------------------PARTICULAS PESADAS------------------------------------------------------------------------------------------------------

# Datos 300k, n50, p_pesadas
x_111 = np.array([15,13,11,9,7,5])
y_111 = np.array([3.85,4.5,5.3,6.45,8.35,11.65])
x_111err = 0.5
y_111err = np.array([0.45,0.4,0.5,0.45,0.45,0.45])

# Datos 300k, n100, p_pesadas
x_211 = np.array([15,13,11,9,7,5])
y_211 = np.array([7.75,8.95,10.65,13,16.75,23.45])
x_211err = 0.5
y_211err = np.array([0.45,0.45,0.45,0.4,0.45,0.35])

# Datos 300k, n150, p_pesadas
x_311 = np.array([15,13,11,9,7,5])
y_311 = np.array([11.65,13.5,15.95,19.45,25.1,35])
x_311err = 0.5
y_311err = np.array([0.3,0.45,0.45,0.45,0.4,0.4])

# Datos 600k, n50, p_pesadas
x_121 = np.array([15,13,11,9,7,5])
y_121 = np.array([7.8,9,10.65,12.9,16.65,23.35])
x_121err = 0.5
y_121err = np.array([0.45,0.45,0.45,0.4,0.35,0.4])

# Datos 600k, n100, p_pesadas
x_221 = np.array([15,13,11,9,7,5])
y_221 = np.array([15.5,18,21.2,26.1,33.6,46.75])
x_221err = 0.5
y_221err = np.array([0.4,0.4,0.35,0.4,0.4,0.35])

# Datos 600k, n150, p_pesadas
x_321 = np.array([15,13,11,9,7,5])
y_321 = np.array([23.35,26.95,31.8,39,50.25,70.1])
x_321err = 0.5
y_321err = np.array([0.4,0.35,0.35,0.4,0.3,0.25])

#-------PARTICULAS LIGERAS-----------------------------------------------------------------------------------------------------------------------------

# Datos 300k, n50, pligeras
x_112 = np.array([15,13,11,9,7,5])
y_112 = np.array([4.1,4.5,5.3,6.45,8.35,11.6])
x_112err = 0.5
y_112err = np.array([0.2,0.4,0.5,0.45,0.45,0.4])

# Datos 300k, n100, pligeras
x_212 = np.array([15,13,11,9,7,5])
y_212 = np.array([7.8,8.9,10.65,13,16.85,23.15])
x_212err = 0.5
y_212err = np.array([0.4,0.4,0.45,0.4,0.45,0.35])

# Datos 300k, n150, pligeras
x_312 = np.array([15,13,11,9,7,5])
y_312 = np.array([11.8,13.45,15.95,19.45,24.95,35.05])
x_312err = 0.5
y_312err = np.array([0.3,0.45,0.45,0.45,0.35,0.35])

# Datos 600k, n50, pligeras
x_122 = np.array([15,13,11,9,7,5])
y_122 = np.array([7.75,8.95,10.55,12.9,16.75,23.2])
x_122err = 0.5
y_122err = np.array([0.45,0.45,0.45,0.4,0.35,0.4])

# Datos 600k, n100, peligeras
x_222 = np.array([15,13,11,9,7,5])
y_222 = np.array([15.6,18,21.25,26,33.3,46.75])
x_222err = 0.5
y_222err = np.array([0.4,0.4,0.35,0.4,0.4,0.35])

# Datos 600k, n150, pligeras
x_322 = np.array([15,13,11,9,7,5])
y_322 = np.array([23.3,27.05,31.75,39,49.8,70.05])
x_322err = 0.5
y_322err = np.array([0.4,0.35,0.35,0.4,0.3,0.25])


#------------------------------------------------------------------------------------------------------------------------------------

plt.figure()
fig, (ax1, ax2) = plt.subplots(nrows=1, ncol=2, figsize = (11,7), constrained_layout=True)

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