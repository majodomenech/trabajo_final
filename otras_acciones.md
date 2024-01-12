## pasar nombres de archivos

dentro del directorio donde tengo todos los archivos, me creo uno con la lista de los nombres así

> ls delta_001_100_10E4_* > deltas_001_10E4.txt

## ver espacio en disco de mi usuario en el servidor

En durga tengo 15 gb disponibles en la carpeta de usuario. Puedo ver cuánto ocupan los directorios principales haciendo:

> du -h --max-depth=1 | sort -rh

ejemplo de lo que devuelve:

(jnb-env) mjdomenech@durga:~$ du -h --max-depth=1 | sort -rh
13G     .
4,9G    ./micromamba
3,8G    ./TrabajoFinal
3,3G    ./.julia
501M    ./julia-1.9.1
164M    ./.local
13M     ./.cache
13M     ./bin
8,0M    ./.ipython
104K    ./carpeta
56K     ./.jupyter
24K     ./.config
8,0K    ./.mamba
8,0K    ./.conda
4,0K    ./.ipynb_checkpoints
