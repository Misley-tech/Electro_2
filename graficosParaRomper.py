# Importación de paquetes
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ESTO ES UNA PRUEBA

# Transformo datos a números flotantes

def series_to_float(array):
    a = np.zeros(len(array))
    largo = len(array)
    vector = np.arange(largo)
    a[0] = array[0]
    for i in vector:
        a[i] = array[i]
    return a


#Lectura de archivos txt
nombre = 'ruidorosa'

def formateo(nombreArchivo):
    nuevoNombre = nombreArchivo + '.txt'
    A = pd.read_csv(nuevoNombre, header=None, delimiter="\t")

    #Ordeno las columnas
    A['Amplitud'] = A[0]
    A['Amplitud'] = A['Amplitud'].str.split('–').str[1]
    A['Frecuencia'] = A[0].str.split('–').str[0]

    A = A.drop(columns=0)
    A.Amplitud = A.Amplitud.str.strip()
    A.Frecuencia = A.Frecuencia.str.strip()

    #Paso el data frame a dos columnas

    Frecuencia_A = A.Frecuencia
    Amplitud_A = A.Amplitud

    frecuencia_A = pd.to_numeric(Frecuencia_A, errors='coerce')
    amplitud_A = pd.to_numeric(Amplitud_A, errors='coerce')

    A_array = series_to_float(amplitud_A)
    A_frec = series_to_float(frecuencia_A)

    datosFormateados = np.array([A_frec, A_array])

    return datosFormateados


salida = formateo(nombre)
#salidaSuavizada = su(salida[0], salida[1], 3)


impedancia = pd.read_csv('zaire.txt', header=None, sep='\s+')
impedancia20 = pd.read_csv('zaire 20g.txt', header=None, sep='\s+')

# Gráficos
"""
plt.figure(figsize=[10,5])
fig = plt.figure(1)

ax = fig.add_subplot(111)
ax.axvline(100, color = 'grey')
ax.axvline(200, color = 'grey')
ax.axvline(300, color = 'grey')
ax.axvline(400, color = 'grey')
ax.axvline(600, color = 'grey')
ax.axvline(800, color = 'grey')
ax.axvline(2000, color = 'grey')
ax.axvline(3000, color = 'grey')
ax.axvline(4000, color = 'grey')
ax.axvline(6000, color = 'grey')
ax.axvline(8000, color = 'grey')
ax.axvline(10000, color = 'grey')

plt.semilogx(salida[0], salidaSuavizada+108.44, 'b')

plt.xlim([40, 15000])
#plt.title('Curva de respuesta en frecuencia')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [dB SPL]')

plt.grid()
plt.show()
"""
plt.figure(figsize=[10, 5])
fig = plt.figure(1)

ax = fig.add_subplot(111)
ax.axvline(100, color = 'grey')
ax.axvline(200, color = 'grey')
ax.axvline(300, color = 'grey')
ax.axvline(400, color = 'grey')
ax.axvline(600, color = 'grey')
ax.axvline(800, color = 'grey')
ax.axvline(2000, color = 'grey')
ax.axvline(3000, color = 'grey')
ax.axvline(4000, color = 'grey')
ax.axvline(6000, color = 'grey')
ax.axvline(8000, color = 'grey')
ax.axvline(10000, color = 'grey')

plt.semilogx(impedancia[0], impedancia[1], 'b', label='Sin masa agregada')
plt.semilogx(impedancia20[0], impedancia20[1], 'violet', label='Con masa agregada')

#plt.xlim([40, 15000])
#plt.title('Curva de respuesta en frecuencia')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Impedancia [ohm]')
plt.legend()
plt.grid()
#plt.show()


"""
# Ejecución de funciones

amplitudes = np.empty((776, 14))

datos0 = pd.read_csv('0°.txt', header=None, sep="\s+")
frecuencias = datos0[0]

amp0 = pd.read_csv('0°.txt', header=None, sep="\s+")
amp0.pop(0)
amp0.pop(2)
amp0.pop(3)

amp15 = pd.read_csv('15°.txt', header=None, sep="\s+")
amp15.pop(0)
amp15.pop(2)
amp15.pop(3)

amp30 = pd.read_csv('30°.txt', header=None, sep="\s+")
amp30.pop(0)
amp30.pop(2)
amp30.pop(3)

amp45 = pd.read_csv('0°.txt', header=None, sep="\s+")
amp45.pop(0)
amp45.pop(2)
amp45.pop(3)

amp60 = pd.read_csv('0°.txt', header=None, sep="\s+")
amp60.pop(0)
amp60.pop(2)
amp60.pop(3)

amp75 = pd.read_csv('0°.txt', header=None, sep="\s+")
amp75.pop(0)
amp75.pop(2)
amp75.pop(3)

amp90 = pd.read_csv('0°.txt', header=None, sep="\s+")
print(amp90.info)
amp90.pop(0)
amp90.pop(2)
amp90.pop(3)

x = frecuencias
y = [-90, -75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75, 90]
z = [float(amp90), float(amp75), float(amp60), float(amp45), float(amp30), float(amp15), float(amp0),
     float(amp15), float(amp30), float(amp45), float(amp60), float(amp75), float(amp90)]
"""
