
# Importar librerías
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# Importar datos
delta_09_10000_10E6 = np.loadtxt('/home/mjdomenech/TrabajoFinal/ArchivosDurga/Julia/JuliaThreads/febrero/Reconstruidos/delta_00009_10000_10E6.txt')
delta_09_1000_10E6 = np.loadtxt('/home/mjdomenech/TrabajoFinal/ArchivosDurga/Julia/JuliaThreads/febrero/Reconstruidos/delta_00009_1000_10E6.txt')
delta_09_100_10E6 = np.loadtxt('/home/mjdomenech/TrabajoFinal/ArchivosDurga/Julia/JuliaThreads/febrero/Reconstruidos/delta_00009_100_10E6.txt')
delta_09_5000_10E6 = np.loadtxt('/home/mjdomenech/TrabajoFinal/ArchivosDurga/Julia/JuliaThreads/febrero/Reconstruidos/delta_00009_5000_10E6.txt')

###############################################################################
########################### GRAFICO PARA DELTAS
###############################################################################

#NORMALIZADA AL VAL MAX

data0 = delta_09_10000_10E6
data1 = delta_09_5000_10E6
data2 = delta_09_1000_10E6
data3 = delta_09_100_10E6

#-----------Parámetros para cada N-----------

lim_escala= 5000000

color0 = 'gold'
color1 = 'blue'
color2 = 'lime'
color3 = 'deeppink'

marker0 = 'D'
marker1 = 's'
marker2 = '^'
marker3 = 'o'

# Filtrar los valores mayores a lim_escala
#data0 = data0[data0 <= lim_escala]
data1 = data1[data1 <= lim_escala]
data2 = data2[data2 <= lim_escala]
data3 = data3[data3 <= lim_escala] 

#es para que no se haga tan pesado calcular todos los bins del 0 a un valor aislado 35213123513

#print(data0.shape)
print(data1.shape)
print(data2.shape)
print(data3.shape)

#---------------------------------

#NORMALIZADA AL VAL MAX
fig = plt.figure(figsize = [7.4, 5.8],layout='tight' )
ax1 = fig.add_subplot(111)

#================================================================================================
binsdelta0 = np.linspace(1.5, np.amax(data0)+0.5, int(np.amax(data0))) 

y0, bin_edges = np.histogram(data0, bins=binsdelta0)
x0 = bin_edges[1:]
x0 = x0.astype(int)

#plt.axvline(x1[-1],linestyle='-',linewidth=0.5)

p00 = np.amax(y0)
y0=y0/p00          #normalizo para que P(delta_max) = 1 (misma normaliz que Bakar)

mask = y0 != 0   # mascara booleana que quita los puntos del histograma que valdrían cero 
x0 = x0[mask]     # (joden al calcularles el log pq log(0) es menos inf)
y0 = y0[mask]

ax1.scatter(x0, y0, marker=marker0, facecolor='none', edgecolor=color0, s=10, label=label0)
#================================================================================================
#================================================================================================
binsdelta1 = np.linspace(1.5, np.amax(data1)+0.5, int(np.amax(data1))) 

y1, bin_edges = np.histogram(data1, bins=binsdelta1)
x1 = bin_edges[1:]
x1 = x1.astype(int)

#plt.axvline(x3[-1],linestyle='-',linewidth=0.5)

p01 = np.amax(y1)
y1=y1/p01          #normalizo para que P(delta_max) = 1 (misma normaliz que Bakar)

mask = y1 != 0   # mascara booleana que quita los puntos del histograma que valdrían cero 
x1 = x1[mask]     # (joden al calcularles el log pq log(0) es menos inf)
y1 = y1[mask]

ax1.scatter(x1, y1, marker=marker1, facecolor='none', edgecolor=color1, s=10, label=label1)

#================================================================================================
#================================================================================================
binsdelta2 = np.linspace(1.5, np.amax(data2)+0.5, int(np.amax(data2))) 

y2, bin_edges = np.histogram(data2, bins=binsdelta2)
x2 = bin_edges[1:]    #de esta forma se ignora el ultimo valor, pero no me importa pq seguro es 0
x2 = x2.astype(int)

#plt.axvline(x2[-1],linestyle='-',linewidth=0.5)

p02 = np.amax(y2)
y2=y2/p02          #normalizo para que P(delta_max) = 1 (misma normaliz que Bakar)

mask = y2 != 0   # mascara booleana que quita los puntos del histograma que valdrían cero 
x2 = x2[mask]     # (joden al calcularles el log pq log(0) es menos inf)
y2 = y2[mask]

ax1.scatter(x2, y2, marker=marker2, facecolor='none', edgecolor=color2, s=10, label=label2)
#================================================================================================
#================================================================================================
binsdelta3 = np.linspace(1.5, np.amax(data3)+0.5, int(np.amax(data3))) 

y3, bin_edges = np.histogram(data3, bins=binsdelta3)
x3 = bin_edges[1:]    #de esta forma se ignora el ultimo valor, pero no me importa pq seguro es 0
x3 = x3.astype(int)

#plt.axvline(x3[-1],linestyle='-',linewidth=0.5)

p03 = np.amax(y3)
y3=y3/p03          #normalizo para que P(delta_max) = 1 (misma normaliz que Bakar)

mask = y3 != 0   # mascara booleana que quita los puntos del histograma que valdrían cero 
x3 = x3[mask]     # (joden al calcularles el log pq log(0) es menos inf)
y3 = y3[mask]

ax1.scatter(x3, y3, marker=marker3, facecolor='none', edgecolor=color3, s=10, label=label3)
#================================================================================================
#================================================================================================

# AJUSTE

intervalo=[20,4000] # Elijo un intervalo diferente para hacer el ajuste
x=np.log(x1)
y=np.log(y1)
xcasi = x[x >= np.log(intervalo[0])]         #cota inferior
ycasi = y[x >= np.log(intervalo[0])]
xfinal = xcasi[xcasi <= np.log(intervalo[1])]         #cota superior
yfinal = ycasi[xcasi <= np.log(intervalo[1])]
#plt.axvline(intervalo[0],linestyle='-',linewidth=0.5)
#plt.axvline(intervalo[1],linestyle='-',linewidth=0.5)
#plt.scatter(np.exp(xfinal), np.exp(yfinal), color='orange')

# Hacer ajuste
slope, intercept, r_value, p_value, std_err = stats.linregress(xfinal, yfinal)

print("Pendiente:", slope)
print("Intercept:", intercept)

plt.plot(np.exp(xfinal), np.exp(-1.409*xfinal + intercept+1.5), color="black", label='Ajuste',linewidth=0.8)
#plt.plot(np.exp(xfinal), np.exp(-1.517*xfinal + intercept+1.5), color="red",linewidth=0.5)

#================================================================================================

#-------------------------configuración estilo-------------------------
ax1.yaxis.set_ticks_position('both')
ax1.tick_params(labelleft=True,labelright=False)

ax1.xaxis.set_ticks_position('both')
ax1.tick_params(labelbottom=True,labeltop=False)

# Aumentar el tamaño de la fuente en los ejes
ax1.tick_params(axis='x', labelsize=18, length=6, width=1)
ax1.tick_params(axis='y', labelsize=18, length=6, width=1)

# Configurar las marcas menores en el eje y
ax1.tick_params(axis='y', which='minor', size=3)

ax1.yaxis.set_ticks_position('both')
ax1.tick_params(labelleft=True,labelright=False)

ax1.xaxis.set_ticks_position('both')
ax1.tick_params(labelbottom=True,labeltop=False)

#ax1.set_title("distribución deltas (fluctuation lenght)")
ax1.set_yscale('log')
ax1.set_xscale('log')

ax1.set_xlabel('$\lambda$ (tamaño de avalancha)',fontsize = 18)
ax1.set_ylabel('$P(\lambda)/P(\lambda_{máx})$', fontsize = 18)

#plt.xticks(fontsize = 15)

ax1.legend(fontsize = 16)
ax1.set_xlim(0.5, lim_escala)

fig.show()

#fig.savefig('/home/mjdomenech/TrabajoFinal/Figuras/OVERLEAF/resultados-febrero/1-deltas_09_norm-val-max.png')
