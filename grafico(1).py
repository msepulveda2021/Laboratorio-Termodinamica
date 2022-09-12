import numpy as np
import matplotlib.pyplot as plt

#ERROR

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

#--------------------------------------------------------------------------------------------------------------------

plt.figure()
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize = (13, 10), constrained_layout=True)

L11 = ax1.errorbar(x_111, y_111, x_111err, y_111err, linestyle='dotted', marker='P', markersize=10, color='orange')
L21 = ax1.errorbar(x_211, y_211, x_211err, y_211err, linestyle='dotted', marker='P', markersize=10, color='darkorange')
L31 = ax1.errorbar(x_311, y_311, x_311err, y_311err, linestyle='dotted', marker='P', markersize=10, color='darkgoldenrod')
L41 = ax1.errorbar(x_121, y_121, x_121err, y_121err, linestyle='-', marker='o', markersize=6, color='lightsteelblue')
L51 = ax1.errorbar(x_221, y_221, x_221err, y_221err, linestyle='-', marker='o', markersize=7, color='cornflowerblue')
L61 = ax1.errorbar(x_321, y_321, x_321err, y_321err, linestyle='-', marker='o', markersize=7, color='royalblue')

L12 = ax2.errorbar(x_112, y_112, x_112err, y_112err, linestyle='dotted', marker='P', markersize=10, color='lime')
L22 = ax2.errorbar(x_212, y_212, x_212err, y_212err, linestyle='dotted', marker='P', markersize=10, color='limegreen')
L32 = ax2.errorbar(x_312, y_312, x_312err, y_312err, linestyle='dotted', marker='P', markersize=10, color='green')
L42 = ax2.errorbar(x_122, y_122, x_122err, y_122err, linestyle='-', marker='o', markersize=6, color='lightcoral')
L52 = ax2.errorbar(x_222, y_222, x_222err, y_222err, linestyle='-', marker='o', markersize=7, color='red')
L62 = ax2.errorbar(x_322, y_322, x_322err, y_322err, linestyle='-', marker='o', markersize=7, color='firebrick')

#----------------------------------------------------------------------------------------------------------------------------

ax1.legend((L11, L21, L31, L41, L51, L61), 
          ('T=300K, n=50','T=300K, n=100','T=300K, n=150','T=600K, n=50', 'T=600K, n=100', 'T=600K, n=150'), loc='upper right', shadow = True, prop={'size': 16})
ax1.set_xlabel('Volumen (nm)', fontsize= 20)
ax1.set_ylabel('Presión (atm)', fontsize= 20)
ax1.set_title('Partículas Pesadas', fontsize= 25)

ax2.legend((L12, L22, L32, L42, L52, L62),
           ('T=300K, n=50','T=300K, n=100','T=300K, n=150','T=600K, n=50', 'T=600K, n=100', 'T=600K, n=150'), loc='upper right', shadow = True, prop={'size': 16})
ax2.set_xlabel('Volumen (nm)', fontsize= 20)
ax2.set_title('Partículas Ligeras', fontsize= 25)

plt.rcParams['font.size'] = 18

archivo_1 = 'grafico(1).pdf'
plt.savefig(archivo_1)

plt.show()
