# Importación de librerías
import numpy as np
import pandas as pd

# Definición de variables
pasos = 5  # pasos de a 5°, configurable por el "usuario"
cant_pasos = int(15//pasos+1)  # cantidad de pasos entre 0 y 180°
array_conteo = np.linspace(0, 180, num=cant_pasos, dtype=int)  # Vector de ángulos
#impulso = [None] * len(array_conteo)  # Vector vacío
impulso = []

"""
A continuación se debería poder leer todos los archivos .csv, eliminar encabezados,
y guardar en una hermosa matriz... Todavía no pasa.
"""

for i in range(len(array_conteo)):
    archivo = pd.read_csv("Archivos/de620me90_hor_deg{:.0f}.csv".format(array_conteo[i]), header=None)
    archivo = archivo.drop([0, 1, 2])  # Elimina las primeras 3 filas que sólo tienen encabezados
    if i == 0:  # Elimina la columna de tiempo en todos los impulsos excepto el primero
        impulso.append(archivo)
    else:
        del (archivo[0])
        impulso.append(archivo)
        continue
print(impulso)
