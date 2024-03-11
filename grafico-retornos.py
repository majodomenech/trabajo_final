
# Importar librerías
import numpy as np
import matplotlib.pyplot as plt
#from scipy import stats

#------------------ configuración ----------------

# Directorio donde están los datos
pwd = 'C:/Users/mariajose/Desktop/archivos-para-ccad/simulaciones-Durga/simulaciones-BUENAS/'

# Importar datos
#data0 = np.loadtxt(pwd+'09/retorno_09_10000_10E6.txt') 
#data1 = np.loadtxt(pwd+'09/retorno_09_5000_10E6.txt')
#data2 = np.loadtxt(pwd+'09/retorno_09_1000_10E6.txt')
#data3 = np.loadtxt(pwd+'09/retorno_09_100_10E6.txt')

data0 = np.loadtxt(pwd+'1N/retorno_00001_10000_10E6_RECONSTRUIDO.txt') 
data1 = np.loadtxt(pwd+'1N/retorno_00002_5000_10E6_RECONSTRUIDO.txt')
data2 = np.loadtxt(pwd+'1N/retorno_0001_1000_10E6.txt')
data3 = np.loadtxt(pwd+'1N/retorno_001_100_10E6.txt')

# Ruta para guardar graficos
pwdgraf = 'C:/Users/mariajose/Desktop/graficos_tf/'
save_fig = True
#nombre_archivo = 'retornos_09_norm-val-max'
nombre_archivo = 'retornos_1N_norm-val-max4'

color0 = 'gold'
color1 = 'dodgerblue'#'blue'
color2 = 'lime'
color3 = 'magenta'#'deeppink'

marker0 = 'D'
marker1 = 's'
marker2 = 'o'
marker3 = '^'

label0 = '$N = 10^4$'
label1 = '$N = 5x10^3$'
label2 = '$N = 10^3$'
label3 = '$N = 10^2$'

lim_grafico = [-20500,20500]
lim_grafico_zoom = [-2000,2000]
lim_grafico_ZOOMZOOM = [-40,40]

#-------------------------------------------------


def grafico_retornos(data0,data1,data2,data3,  lim_grafico,
                     color0,color1,color2,color3,
                     marker0,marker1,marker2,marker3,
                     label0,label1,label2,label3,
                     pwdgraf, save_fig, nombre_archivo):

    lim_grafico=lim_grafico

    fig = plt.figure(figsize = [7.4, 5.8], layout='tight')

    ax1 = fig.add_subplot(111)
    binsretorno = np.linspace(lim_grafico[0]-0.5,lim_grafico[1]+0.5,-lim_grafico[0]+lim_grafico[1]+2)

    #==================================
    y_tot, bin_edges_tot = np.histogram(data0, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker0, facecolor='none', edgecolor=color0, s=15, label=label0)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data1, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker1, facecolor='none', edgecolor=color1, s=15, label=label1)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data2, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker2, facecolor='none', edgecolor=color2, s=15, label=label2)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data3, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker3, facecolor='none', edgecolor=color3, s=15, label=label3)#, color='cyan')
    #==================================
    
    #---------------------------------------------------------
    # Aumentar el tamaño de la fuente en los ejes
    ax1.tick_params(axis='x', labelsize=18, length=6, width=1)
    ax1.tick_params(axis='y', labelsize=18, length=6, width=1)

    # Configurar las marcas menores en el eje y
    ax1.tick_params(axis='y', which='minor', size=3)


    ax1.yaxis.set_ticks_position('both')
    ax1.tick_params(labelleft=True,labelright=False)

    ax1.xaxis.set_ticks_position('both')
    ax1.tick_params(labelbottom=True,labeltop=False)

    ax1.set_yscale("log")
    ax1.legend(fontsize = 15)
    #---------------------------------------------------------
    #ax1.set_title('distribución de retornos (log return)')
    #fig.show()
    
    ax1.set_xlabel('$\Delta \lambda$ (retornos)',fontsize = 14)
    ax1.set_ylabel('$P(\Delta \lambda)/P(0)$',fontsize = 14)
    ax1.set_xlim(lim_grafico[0],lim_grafico[1])
    
    if save_fig == True:
        fig.savefig(pwdgraf+nombre_archivo+'.pdf', format='pdf')

    #fig.savefig('/home/mjdomenech/TrabajoFinal/Figuras/OVERLEAF/resultados-febrero/1-retornos_09_norm-val-max.png', dpi=300)

grafico_retornos(data0,data1,data2,data3,  lim_grafico,
                     color0,color1,color2,color3,
                     marker0,marker1,marker2,marker3,
                     label0,label1,label2,label3,
                     pwdgraf, save_fig, nombre_archivo)

def grafico_retornos_zoom(data0,data1,data2,data3,  lim_grafico_zoom,
                     color0,color1,color2,color3,
                     marker0,marker1,marker2,marker3,
                     label0,label1,label2,label3,
                     pwdgraf, save_fig, nombre_archivo):

    #ZOOM
    lim_grafico=lim_grafico_zoom
    fig = plt.figure(figsize = [7.4, 5.8], layout='tight')

    ax1 = fig.add_subplot(111)
    binsretorno = np.linspace(lim_grafico[0]-0.5,lim_grafico[1]+0.5,-lim_grafico[0]+lim_grafico[1]+2)

    #==================================
    y_tot, bin_edges_tot = np.histogram(data0, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker0, facecolor='none', edgecolor=color0, s=15, label=label0)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data1, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker1, facecolor='none', edgecolor=color1, s=15, label=label1)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data2, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker2, facecolor='none', edgecolor=color2, s=15, label=label2)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data3, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker3, facecolor='none', edgecolor=color3, s=15, label=label3)#, color='cyan')
    #==================================
    
    # Aumentar el tamaño de la fuente en los ejes
    ax1.tick_params(axis='x', labelsize=18, length=6, width=1)
    ax1.tick_params(axis='y', labelsize=18, length=6, width=1)

    # Configurar las marcas menores en el eje y
    ax1.tick_params(axis='y', which='minor', size=3)

    ax1.yaxis.set_ticks_position('both')
    ax1.tick_params(labelleft=True,labelright=False)

    ax1.xaxis.set_ticks_position('both')
    ax1.tick_params(labelbottom=True,labeltop=False)

    ax1.set_yscale("log")
    ax1.legend(fontsize = 15)
    
    ax1.set_xlabel('$\Delta \lambda$ (retornos)',fontsize = 14)
    ax1.set_ylabel('$P(\Delta \lambda)/P(0)$',fontsize = 14)
    ax1.set_xlim(lim_grafico_zoom[0],lim_grafico_zoom[1])
    #ax1.set_title('distribución de retornos (log return)')
    #fig.show()

    if save_fig == True:
        fig.savefig(pwdgraf+nombre_archivo+'_zoom'+'.pdf', format='pdf')

    #fig.savefig('/home/mjdomenech/TrabajoFinal/Figuras/OVERLEAF/resultados-febrero/1-retornos_09_norm-val-maxZOOM1.png', dpi=300)

grafico_retornos_zoom(data0,data1,data2,data3,  lim_grafico_zoom,
                     color0,color1,color2,color3,
                     marker0,marker1,marker2,marker3,
                     label0,label1,label2,label3,
                     pwdgraf, save_fig, nombre_archivo)

def grafico_retornos_ZOOMZOOM(data0,data1,data2,data3,  lim_grafico_ZOOMZOOM,
                     color0,color1,color2,color3,
                     marker0,marker1,marker2,marker3,
                     label0,label1,label2,label3,
                     pwdgraf, save_fig, nombre_archivo):

    #ZOOM ZOOM

    lim_grafico=lim_grafico_ZOOMZOOM
    fig = plt.figure(figsize = [4.4, 3.5], layout='tight')

    ax1 = fig.add_subplot(111)
    binsretorno = np.linspace(lim_grafico[0]-0.5,lim_grafico[1]+0.5,-lim_grafico[0]+lim_grafico[1]+2)

    #==================================
    y_tot, bin_edges_tot = np.histogram(data0, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker0, facecolor='none', edgecolor=color0, s=15, label=label0)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data1, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker1, facecolor='none', edgecolor=color1, s=15, label=label1)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data2, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker2, facecolor='none', edgecolor=color2, s=15, label=label2)#, color='cyan')
    #==================================
    #==================================
    y_tot, bin_edges_tot = np.histogram(data3, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p0_tot = np.amax(y_tot)

    ax1.scatter(x_tot, y_tot/p0_tot, marker=marker3, facecolor='none', edgecolor=color3, s=15, label=label3)#, color='cyan')
    #==================================

    # Aumentar el tamaño de la fuente en los ejes
    ax1.tick_params(axis='x', labelsize=15, length=4, width=1)
    ax1.tick_params(axis='y', labelsize=15, length=4, width=1)

    # Configurar las marcas menores en el eje y
    ax1.tick_params(axis='y', which='minor', size=3)

    ax1.yaxis.set_ticks_position('both')
    ax1.tick_params(labelleft=True,labelright=False)

    ax1.xaxis.set_ticks_position('both')
    ax1.tick_params(labelbottom=True,labeltop=False)

    ax1.set_yscale("log")
    #ax1.legend(fontsize = 15)
    #ax1.set_title('distribución de retornos (log return)')
    ax1.set_xlim(lim_grafico_ZOOMZOOM[0],lim_grafico_ZOOMZOOM[1])
    ax1.set_ylim(0.01,2)

    if save_fig == True:
        fig.savefig(pwdgraf+nombre_archivo+'_ZOOMZOOM'+'.pdf', format='pdf')

    #fig.savefig('/home/mjdomenech/TrabajoFinal/Figuras/OVERLEAF/resultados-febrero/1-retornos_09_norm-val-maxZOOM1PICO.png', dpi=300)
    #fig.show()
        

grafico_retornos_ZOOMZOOM(data0,data1,data2,data3,  lim_grafico_ZOOMZOOM,
                     color0,color1,color2,color3,
                     marker0,marker1,marker2,marker3,
                     label0,label1,label2,label3,
                     pwdgraf, save_fig, nombre_archivo) 