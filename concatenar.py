
import numpy as np

#------------------ configuración ----------------

# aca poner la ruta donde estan los archivo_names, destildar la correcta

#pwd = '/home/mjdomenech/TrabajoFinal/ArchivosDurga/Julia/JuliaThreads/febrero/deltas_00002_10E4.txt'
pwd = 'C:\\Users\\mariajose\\Desktop\\archivos-para-ccad\\simulaciones-CCAD\\10E3marzo1\\'

#pwd = 'C:\Users\mariajose\Desktop\archivos-para-ccad\simulaciones-Durga\simulaciones-CCAD\10E3marzo1\'
#pwd = '/home/mjdomenech/TrabajoFinal/ArchivosCCAD/JuliaThreads/marzo1/'

#archivo = 'deltas_00001_10E3.txt'
archivo = 'retornos_00001_10E3.txt'

#archivo_resultante = 'delta_00001_10000_concatenado1.txt'
archivo_resultante = 'retorno_00001_10000_concatenado1.txt'

#------------------------------------------------

archivo_names = np.loadtxt(pwd+archivo, dtype='str')

print('ejemplo: ', archivo_names[99]) 

arrays = []

# Ruta base de los archivos
base_path = pwd

i=1

# Iterar sobre los nombres de archivos en deltas_00001_10E4
for filename in archivo_names:
    # Construir la ruta completa del archivo
    full_path = base_path + filename
    
    if i % 10 == 0:
        print(i,full_path)
        
    i+=1
    
    # Cargar el archivo y agregarlo a la lista de arrays
    array = np.loadtxt(full_path)
    arrays.append(array)

# Concatenar los arrays en uno solo
result_array = np.concatenate(arrays)

print('shape del array resultante:', np.shape(result_array))

np.savetxt(pwd+archivo_resultante, result_array)