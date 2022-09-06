import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------------------------------------------------

# Datos 300k, n50
x_11 = np.array([15,13,11,9,7,5])
y_11 = np.array([4.1,4.5,5.3,6.45,8.35,11.6])
x_11err = 0.5
y_11err = np.array([0.2,0.4,0.5,0.45,0.45,0.4])

# Datos 300k, n100
x_21 = np.array
y_21 = np.array
x_21err = np.array
y_21err = 0.5

# Datos 300k, n150
x_31 = np.array
y_31 = np.array
x_31err = np.array
y_31err = 0.5

# Datos 600k, n50
x_12 = np.array
y_12 = np.array
x_12err = np.array
y_12err = np.array

# Datos 600k, n100
x_22 = np.array
y_22 = np.array
x_22err = np.array
y_22err = 

# Datos 600k, n150
x_32 = np.array
y_32 = np.array
x_32err = np.array
y_32err = np.array

#------------------------------------------------------------------------------------------------------------------------------------

# lower & upper limits of the error
lolims = np.array([0, 0, 1, 0, 1, 0, 0, 0, 1, 0], dtype=bool)
uplims = np.array([0, 1, 0, 0, 0, 1, 0, 0, 0, 1], dtype=bool)
ls = 'dotted'

fig, ax = plt.subplots(figsize=(7, 4))

# standard error bars
ax.errorbar(x, y, xerr=xerr, yerr=yerr, linestyle=ls)

# including upper limits
ax.errorbar(x, y + 0.5, xerr=xerr, yerr=yerr, uplims=uplims,
            linestyle=ls)

# including lower limits
ax.errorbar(x, y + 1.0, xerr=xerr, yerr=yerr, lolims=lolims,
            linestyle=ls)

# including upper and lower limits
ax.errorbar(x, y + 1.5, xerr=xerr, yerr=yerr,
            lolims=lolims, uplims=uplims,
            marker='o', markersize=8,
            linestyle=ls)

# Plot a series with lower and upper limits in both x & y
# constant x-error with varying y-error
xerr = 0.2
yerr = np.full_like(x, 0.2)
yerr[[3, 6]] = 0.3

# mock up some limits by modifying previous data
xlolims = lolims
xuplims = uplims
lolims = np.zeros_like(x)
uplims = np.zeros_like(x)
lolims[[6]] = True  # only limited at this index
uplims[[3]] = True  # only limited at this index

# do the plotting
ax.errorbar(x, y + 2.1, xerr=xerr, yerr=yerr,
            xlolims=xlolims, xuplims=xuplims,
            uplims=uplims, lolims=lolims,
            marker='o', markersize=8,
            linestyle='none')

# tidy up the figure
ax.set_xlim((0, 5.5))
ax.set_title('Errorbar upper and lower limits')
plt.show()
