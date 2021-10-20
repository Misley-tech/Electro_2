# Importación de librerías
import numpy as np
import pandas as pd

# Definición de variables
pasos = 5  # pasos de a 5°, configurable por el "usuario"
cant_pasos = int(20//pasos+1)  # cantidad de pasos entre 0 y 180°
array_conteo = np.linspace(0, 180, num=cant_pasos, dtype=int)  # Vector de ángulos
impulso = [None] * (np.max(array_conteo)+1)  # Vector vacío


"""
A continuación se debería poder leer todos los archivos .csv, eliminar encabezados,
y guardar en una hermosa matriz... Todavía no pasa.
"""

for i in array_conteo:
    archivo = pd.read_csv("Archivos/de620me90_hor_deg{:.0f}.csv".format(i), header=None)
    archivo = archivo.drop([0, 1, 2])  # Saco las primeras 3 filas que sólo tienen encabezados
    n = i//5
    print("i = "+str(i))
    if i == 0:
        impulso[n] = archivo
    else:
        archivo.drop(columns=0)
        impulso[n] = archivo[1]
    print(impulso)


