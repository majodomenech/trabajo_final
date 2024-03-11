#!/bin/bash

#SBATCH --job-name=concatenador-jose

#SBATCH --output=concatenador-jose.log

#SBATCH --partition=short

#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=1 
#SBATCH --cpus-per-task=64 ## Esto nos deja modificar el número de hilos que podemos usar. Serafin 1-64

#SBATCH --exclusive 

#SBATCH --mail-type=ALL    
#SBATCH --mail-user=m.jose.domenech@mi.unc.edu.ar

. /etc/profile
srun python /home/mjdomenech/TrabajoFinal/ArchivosCCAD/JuliaThreads/marzo1/concatenar.py