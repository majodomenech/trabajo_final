sbatch: Para encolar un trabajo cuyo submit script es job.sh, luego de encolar el trabajo le devolverá un número que lo identifica.

> $sbatch job.sh
> Submitted batch job 1234

squeue: Muestra la cola de trabajos pendientes o en ejecución.

> squeue --me


###################################

Marcos M. <marcos.mazzini@gmail.com>
jue, 20 jul 2023, 9:40
para mí


Estimada/o Maria Jose Domenech,

Le comunicamos que su cuenta en el Centro de Computación de Alto Desempeño se encuentra activa.
Para acceder al cluster que desee sírvase ejecutar el comando correspondiente desde una terminal:

ssh mjdomenech@serafin.ccad.unc.edu.ar
ssh mjdomenech@mendieta.ccad.unc.edu.ar
ssh mjdomenech@eulogia.ccad.unc.edu.ar
ssh mjdomenech@mulatona.ccad.unc.edu.ar

No necesita especificar una contraseña, la llave pública enviada en la solicitud ha sido copiada en su directorio.

Hemos procedido también a inscribirle en la mailing-list de usuarias y usuarios del cluster, el grupo usuarios@ccad.unc.edu.ar:
https://groups.google.com/a/ccad.unc.edu.ar/d/forum/usuarios
A esta lista de correo se envían todos los anuncios sobre incidentes o mantenimientos programados del cluster. Además es un espacio para intercambiar experiencias o astucias en el uso de los recursos compartidos.
Adicionalmente puede incorporarse al grupo de zulip con el mismo fin:
https://ccadunc.zulipchat.com/join/mz45hkijjnu75f2vo2wn7756

Para facilitar la compilación de los programas hemos implementado el sistema de módulos (environment modules) que completan automáticamente las variables de entorno. Puede encontrar información básica sobre el uso de este sistema en nuestra página wiki:
http://dokuwiki.ccad.unc.edu.ar/

La wiki contiene asimismo información sobre el uso del sistema de colas y gestor de recursos computacionales SLURM:
https://dokuwiki.ccad.unc.edu.ar/doku.php?id=slurm

Tanto el cluster mendieta como el cluster serafin cuentan con colas de pruebas o simulaciones cortas.

Nombre de la cola: debug, short (serafin)
Tiempo máximo de ejecución: 2 minutos, 1 hora (serafin)
Número máximo de nodos: 2, 60 (serafin)
Prioridad: 20000

Los trabajos lanzados en esta cola serán "ultra-prioritarios" y se ejecutarán apenas los recursos solicitados se encuentren disponibles. Los trabajos que superen el límite de tiempo serán cancelados automáticamente por el sistema.

Para poder usar la cola se deberá agregar las siguientes instrucciones en el script de lanzamiento:

#!/bin/bash
#SBATCH --job-name=test
#SBATCH --partition=debug # / short      (serafin)
#SBATCH --ntasks=2
#SBATCH --time=0-00:01:59 # / 0-01:00    hasta una hora (serafin)

El cluster serafín es el que se ha incormporado más recientemente mientras que el cluster mendieta es específico para aplicaciones que puedan aprovechar GPU.

La cuota máxima de almacenamiento es de 500GB en su home, compartido entre todos los clusters del centro.
Cada vez que se ejecuta un trabajo éste tiene acceso además al directorio local /scratch para escrituras temporales en el nodo.
Una vez finalizado el trabajo, dicho sistema de ficheros se destruye, por lo tanto es importante copiar los datos útiles dentro del script de submit.

Todos aquellos trabajos de tecnología, ciencia aplicada o ciencia básica que hayan utilizado algún recurso computacional del CCAD deberán incluir una mención explícita de esto, en toda comunicación, ya sean publicaciones en revistas científicas, congresos, comunicados de prensa o notas en medios periodísticos. En medios escritos deberán incluir el párrafo que se indica a continuación:
Español
«Este trabajo utilizó recursos computacionales del CCAD de la Universidad Nacional de Córdoba (https://ccad.unc.edu.ar/), que forman parte del SNCAD del MinCyT de la República Argentina.»
English
«This work used computational resources from CCDA - Universidad Nacional de Córdoba (https://ccad.unc.edu.ar/), which are part of SNCAD MinCyT, República Argentina.»

El uso gratuito de los servicios del CCAD-UNC se limita a proyectos de índole pública. Si en alguna de las etapas del proyecto la utilización de los servicios del CCAD redunda en un fin comercial, éste deberá ser informado al Director del Centro <director@ccad.unc.edu.ar> a fin de que el mismo sea correctamente arancelado, siguiendo la reglamentación.  La falta del aviso de uso comercial implica el cierre de cuentas de todo el grupo de usuarios implicado en el proyecto.

En los equipos del CCAD-UNC solo se puede utilizar software con licencia válida, ya sea pública o privada. Cada usuaria/o deberá consultar si el CCAD-UNC tiene la licencia del Software que intenta utilizar y es responsable de cualquier infracción a las leyes vigentes.
El CCAD-UNC deslinda cualquier responsabilidad legal sobre el uso indebido del software por la imposibilidad técnica de monitorearlo constantemente.
La detección de un uso indebido supondrá el cierre de cuentas de todo el grupo de usuarios implicado en el proyecto.

Ante cualquier consulta, problema o incidente no dude en contactarnos a la dirección de correo <soporte@ccad.unc.edu.ar>

Atentamente,  Equipo de soporte CCAD - UNC
