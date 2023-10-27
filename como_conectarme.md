______________________________________________________________________________
# CONECTARME A DURGA (máquina)

## -DESDE LA PC
abrir comand prompt de windows (o cualquier terminal):
>ssh mjdomenech@durga.famaf.unc.edu.ar

Ecooyighaew5eichioghoh2wequaek2e

poniendo eso me conecto a Durga y veo un linux normal en mi carpeta de usuario home/mjdomenech

### como mandar un script para que corra en 2do plano

>nohup python ~/TrabajoFinal/CorridaSistema_09_5000_10E6.py &
>
>nohup julia ~/TrabajoFinal/CorridasJulia/CorridaSistema_09_100_10E6.jl &

los que más suelo mandar:

corrida común
>nohup julia ~/TrabajoFinal/CorridasJulia/CorridaSistema_0001_1000_10E6.jl &

corrida JuliaParalelos
>nohup julia ~/TrabajoFinal/CorridasJulia/CorridasParalelas/CorridaSistema_00001_10000_10E4_1.jl &

corrida JuliaThreads
>nohup julia -t 20 ~/TrabajoFinal/CorridasJulia/CorridasThreads/lanzador_threads.jl 0.0001 10000 10E4 20 &

### instalar paquetes en enviroment

>micromamba install -c conda-forge 'nombre-paquete'

 





### como abrir notebooks ya iniciados para usarlos

ssh mjdomenech@durga blabla
contraseña
micromamba activate jnb-env
jupyternotebook list
copio el link que quiero, hago tunneling con el respectivo port en otra terminal y pego el link en mi navegador
y listo

### Los enviroments que creé con micromamba

jnb-env:  
enviroment con python. Instalé Numpy, Matplotlib, Scipy

julia-env:
enviroment con julia. Instalé julia, Pyplot


### Pasos que seguí para instalar todo

instalé micromamba siguiendo lo de acá: https://waylonwalker.com/install-micromamba/
creé el enviroment como juan explica acá: https://github.com/jipphysics/jupyter-ccad/blob/main/README.md (https://github.com/jipphysics/jupyter-ccad)
pude abrir el notebook en segundo plano (no se cierra si cierro terminal donde inicié el notebook): https://stackoverflow.com/questions/47331050/how-to-run-jupyter-notebook-in-the-background-no-need-to-keep-one-terminal-for
hago tunneling en otra terminal, pongo el link en el navegador y tengo mi jupyter que queda andando aún si apago mi computadora local.


## -DESDE LA TABLET
-con terminus
-con el otro programa

-----------------------------------------------------

para pasar archivos desde mi compu a mi carpeta de Durga uso filezilla
servidor: durga.famaf.unc.edu.ar
usuario: mjdomenech
contraseña: Ecooyighaew5eichioghoh2wequaek2e
puerto: 22



debería:
-ver como instalar anaconda y crear un enviroment donde instalar python y posiblemente jupyter notebook.
-una vez instalado eso puedo seguir los pasos de juan para usar ver el jupyter de durga en mi navegador.
-usar midnight commander para pasar archivos desde mi compu a durga (no se como) o filezilla

-generar clave fuerte? hacer lo de clave publica - clave privada
Cambiá el pass por uno fuerte y/o usá https://www.strongdm.com/blog/ssh-passwordless-login

-htop se mira la carga (como uso esto?)



________________________________________________________
--------------------------------------------------------
CONECTARME A BANDURRIA (cluster)

hacer:
-ver bien los archivos que me mando flor .sh

________________________________________________________
--------------------------------------------------------
usar visual studio para abrir ventanas y conectarme ssh desde su terminal


________________________________________________________
--------------------------------------------------------
CONECTARME CCAD (igual que durga creo)

# como mandar a la cola scritps

squeue -> comando para ver cola

squeue --me -> trabajos que tengo yo en la cola


los archivos .sh son lanzadores de bash, dicen las instrucciones para mandar los scripts a la cola del cluster. 

Necesito el submit.sh y el script de julia o de python.

nico siempre larga los trabajos en el home (de su usuario) por las dudas. Los trabajos se lanzan con:

>sbatch submit.sh     (siempre tiene que ser .sh y tener esas instrucciones de cabecera)

# como paralelizar en julia

Threads.@threads for i in 1:100 ... 

(parte del paquete base de julia, no hay que instalar nada)

# cosas del submit.sh

cuando mandas una tarea te dan un nodo, batch exclusive es que cuando agarras un nodo te queda para vos mientras lo uses. Cada nodo tiene 64 cores, entonces se pueden mandar 64 tareas diferentes
el mail es para que te avise cuando termina.





# distinguir clave privada de la publica

id_rsa.pub -> publica
id_rsa -> privada


________________________________________________________
--------------------------------------------------------
Aprender a usar git

hacer:
-entender que son los repositorios y como copiarlos a mi github

VER CURSO ICARO
