## pasar nombres de archivos

dentro del directorio donde tengo todos los archivos, me creo uno con la lista de los nombres así

> ls delta_001_100_10E4_* > deltas_001_10E4.txt

## ver espacio en disco de mi usuario en el servidor

En durga tengo 15 gb disponibles en la carpeta de usuario. Puedo ver cuánto ocupan los directorios principales haciendo:

> du -h --max-depth=1 | sort -rh
