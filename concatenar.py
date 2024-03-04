
pwd = '/home/mjdomenech/TrabajoFinal/ArchivosDurga/Julia/JuliaThreads/febrero/deltas_00002_10E4.txt'

archivo-names = np.loadtxt(pwd, dtype='str')

print(archivo-names[99]) 

arrays = []

# Ruta base de los archivos
base_path = '/home/mjdomenech/TrabajoFinal/ArchivosDurga/Julia/JuliaThreads/febrero/'

i=1

# Iterar sobre los nombres de archivos en deltas_00001_10E4
for filename in archivo-names:
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

np.savetxt('/home/mjdomenech/TrabajoFinal/ArchivosDurga/Julia/JuliaThreads/febrero/Reconstruidos/delta_00002_5000_10E6.txt', result_array)