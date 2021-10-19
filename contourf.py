# Importación de módulos
import numpy as np
import matplotlib.pyplot as plt


# Adquisición de datos
cero = np.loadtxt('0°.txt', skiprows=2)
cero = cero[:, 1]

quince = np.loadtxt('15°.txt', skiprows=2)
quince = quince[:, 1]

treinta = np.loadtxt('30°.txt', skiprows=2)
treinta = treinta[:, 1]

cuarentaycinco = np.loadtxt('45°.txt', skiprows=2)
cuarentaycinco = cuarentaycinco[:, 1]

sesenta = np.loadtxt('60°.txt', skiprows=2)
sesenta = sesenta[:, 1]

setentaycinco = np.loadtxt('75°.txt', skiprows=2)
setentaycinco = setentaycinco[:, 1]

noventa = np.loadtxt('90°.txt', skiprows=2)
noventa = noventa[:, 1]

z = np.vstack((noventa, setentaycinco, sesenta, cuarentaycinco, treinta,
               quince, cero, quince, treinta, cuarentaycinco, sesenta, setentaycinco,
               noventa))
x = [-90, -75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75, 90]

y = np.loadtxt('0°.txt', skiprows=2)
y = y[:, 0]

xlist = y
ylist = x
X, Y = np.meshgrid(xlist, ylist)
Z = z

fig, ax = plt.subplots(1, 1)
cp = ax.contourf(X, Y, Z, label='Amplitud [dB]')
fig.colorbar(cp)  # Add a colorbar to a plot
#ax.set_title('Directividad del altavoz')
ax.set_xlabel('Frecuencia (lineal) [Hz]')
ax.set_ylabel('Ángulo [°]')
plt.show()
