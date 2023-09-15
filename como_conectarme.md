______________________________________________________________________________
# CONECTARME A DURGA (máquina)

## -DESDE LA PC
abrir comand prompt de windows (o cualquier terminal):
>ssh mjdomenech@durga.famaf.unc.edu.ar

Ecooyighaew5eichioghoh2wequaek2e

poniendo eso me conecto a Durga y veo un linux normal en mi carpeta de usuario home/mjdomenech

### como mandar un script para que corra en 2do plano

>nohup python ~/TrabajoFinal/CorridaSistema_09_5000_10E6.py &
>nohup julia ~/TrabajoFinal/CorridasJulia/CorridaSistema_09_100_10E6.jl &

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

hacer:
-pedir usuario


________________________________________________________
--------------------------------------------------------
Aprender a usar git

hacer:
-entender que son los repositorios y como copiarlos a mi github

VER CURSO ICARO
