
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
#--------------------

# Directorio donde están los datos
#pwd = 'C:/Users/mariajose/Desktop/archivos-para-ccad/simulaciones-Durga/simulaciones-BUENAS/09/'
pwd = 'C:/Users/mariajose/Desktop/archivos-para-ccad/simulaciones-Durga/simulaciones-BUENAS/1N/'

# Importar datos
#data0 = np.loadtxt(pwd+'delta_09_10000_10E6.txt')
#data1 = np.loadtxt(pwd+'delta_09_5000_10E6.txt')
#data2 = np.loadtxt(pwd+'delta_09_1000_10E6.txt')
#data3 = np.loadtxt(pwd+'delta_09_100_10E6.txt')

#data0r = np.loadtxt(pwd+'retorno_09_10000_10E6.txt')
#data1r = np.loadtxt(pwd+'retorno_09_5000_10E6.txt')
#data2r = np.loadtxt(pwd+'retorno_09_1000_10E6.txt')
#data3r = np.loadtxt(pwd+'retorno_09_100_10E6.txt')

data0 = np.loadtxt(pwd+'delta_00001_10000_10E6_RECONSTRUIDO.txt')
#data1 = np.loadtxt(pwd+'delta_00002_5000_10E6_RECONSTRUIDO.txt')
#data2 = np.loadtxt(pwd+'delta_0001_1000_10E6.txt')
#data3 = np.loadtxt(pwd+'delta_001_100_10E6.txt')

data0r = np.loadtxt(pwd+'retorno_00001_10000_10E6_RECONSTRUIDO.txt')
#data1r = np.loadtxt(pwd+'retorno_00002_5000_10E6_RECONSTRUIDO.txt')
#data2r = np.loadtxt(pwd+'retorno_0001_1000_10E6.txt')
#data3r = np.loadtxt(pwd+'retorno_001_100_10E6.txt')


color0 ='gold'
color1 = 'dodgerblue' #'blue'
color2='lime'
color3= 'magenta' #'deeppink'

marker0 = 'D'
marker1 = 's'
marker2 = 'o'
marker3 = '^'

label0 = '$N=10^4$'
label1 = '$N=5x10^3$'
label2 = '$N=10^3$'
label3 = '$N=10^2$'


#------------------- configuración ----------------
datadelta=data0                             #  (100: 3, 1000: 2 , 5000: 1, 10000: 0)
intervalo1=[2,3000]  # Intervalo ajuste lineal (100: [25,100], 1000: [25,1000] , 5000: [30,4500], 10000: [30,9500])
lim_escala=100000

dataretorno = data0r
lim_grafico =  [-15000,15000]                #  (100: [-1500,1500], 1000:  [-5200,5200], 5000: [-16000,16000], 10000: [-19000,19000]) 
lim_graficoZOOM=[-2000,2000]
tau = 1.5                                  #  (100: 1.51, 1000: 1.44, 5000: 1.44, 10000: 1.46)  
initial_guess1 = 0.01  #beta
initial_guess = [27,0.000005]     #aq, a1
int_graficado =[-35000,35000]    #hasta donde grafico curva ajustada #  (100: [-510,510], 1000:  [-4000,4000], 5000: [-12000,12000], 10000: [-20000,20000])                    
int_ajusteqg = [-25000,25000]      #en este int hago el ajuste para que el zoom se vea bien (100:[-370,370], 1000:  [-3800,3800], 5000: [-9950,9950], 10000: [-9950,9950] )
int_ajuste = [-9000,9000]
int_excluido = [0,0]

ig = False
qg = True
f = False

color=color0
marker=marker0
label=label0

# Ruta para guardar graficos
pwdgraf = 'C:/Users/mariajose/Desktop/graficos_tf/'
save_fig = True
nombre_archivo = 'AJUSTES_0001_norm-val-max_10000'

#0.9
# tau                  100: 1.51,     1000: 1.44,     5000: 1.44,     10000: 1.46
# (tau+2)/tau= q       100: 2.32,     1000: 2.39,     5000: 2.39,     10000: 2.37
# 1/1-q                100: -0.758,   1000: -0.719,   5000: -0.719,   10000: -0.730
# q-1                  100: 1.32,     1000: 1.39,     5000: 1.39,     10000: 1.37

#1/N
# tau                  100: 1.49,     1000: 1.44,     5000: 1.44,     10000: 1.46
# (tau+2)/tau= q       100: 2.34,     1000: 2.39,     5000: 2.39,     10000: 2.37
# 1/1-q                100: -0.746,   1000: -0.719,   5000: -0.719,   10000: -0.730
# q-1                  100: 1.34,     1000: 1.39,     5000: 1.39,     10000: 1.37


def FUNC_log(x,aq,a1): # Cambiar valores de 1/(1-q) y de (q-1) según cada q
    
    return -0.746 * np.log( 1 - (aq/a1) + (aq/a1) * np.exp(1.34*a1*(x**2)) )

#--------------------

def qgaussian(x,aq):
    
    return ((1-(1-2.33)*aq*(x**2))**(1/(1-2.33)))

def qgaussian_log(x,aq):
    
    return (1/(1-2.33))*np.log(1-(1-2.33)*aq*(x**2))
    

def separar_par_impar(data):
    
    data_pares = data[data % 2 == 0]
    data_impares = data[data % 2 != 0]
    
    return data_pares, data_impares

def grafico(datadelta,lim_escala,intervalo1,   dataretorno,lim_grafico,tau,int_ajusteqg,int_ajuste,int_graficado,initial_guess1,initial_guess,ig,qg,f,int_excluido,  color,marker,label,pwdgraf,nombre_archivo,save_fig):
    #NORMALIZADO AL VAL MAX

    fig = plt.figure(figsize = [10.5, 3.9],layout='tight' )
                              #[11.6, 4.8] [9.8, 3.8]
    #########################
    #########################
    ax1 = fig.add_subplot(121)
    

    #====================================
    intervalo1=intervalo1 # Intervalo para hacer el ajuste lineal
    lim_escala=lim_escala # Límite escala y grafico
    
    # Filtrar los valores mayores a lim_escala
    datadelta = datadelta[datadelta <= lim_escala]

    #binsdelta1 = np.linspace(1.5, np.amax(datadelta)+0.5, int(np.amax(datadelta)/2))
    binsdelta1 = np.linspace(1.5, np.amax(datadelta)+0.5, int(np.amax(datadelta))) 
    
    y1, bin_edges = np.histogram(datadelta, bins=binsdelta1)
    x1 = bin_edges[1:]
    x1 = x1.astype(int)
    p01 = np.amax(y1)
    y1=y1/p01          # Normalizo para que P(delta_max) = 1 (misma normaliz que Bakar)
    mask = y1 != 0     # Máscara booleana que quita los puntos del histograma que valdrían cero 
    x1 = x1[mask]      # (joden al calcularles el log pq log(0) es menos inf)
    y1 = y1[mask]
    
    ax1.scatter(x1, y1, marker=marker, facecolor='none', edgecolor=color, s=10, label=label)
    #-------------------------------- 
    #AJUSTE

    x=np.log10(x1)
    y=np.log10(y1)
    xcasi = x[x >= np.log10(intervalo1[0])]         # Cota inferior
    ycasi = y[x >= np.log10(intervalo1[0])]
    xfinal = xcasi[xcasi <= np.log10(intervalo1[1])]         # Cota superior
    yfinal = ycasi[xcasi <= np.log10(intervalo1[1])]
    #ax1.axvline(intervalo[0],linestyle='--',linewidth=0.5)
    #ax1.axvline(intervalo[1],linestyle='--',linewidth=0.5)

    # Graficar ajuste
    slope, intercept, r_value, p_value, std_err = stats.linregress(xfinal, yfinal)
    print("Pendiente:", slope)
    print("Intercept:", intercept)
    ax1.plot(10**(xfinal), 10**(slope*(xfinal) + intercept), color="black", label=f'Ajuste lineal, $\\tau={tau:.2f}$',linewidth=0.8)
    #ax1.plot(10**(xfinal), 10**(-1.55*(xfinal) + intercept), ls='--', color="black", label='Ajuste',linewidth=0.8)
    #ax1.plot(np.exp(xfinal), np.exp(-slope*(xfinal) + intercept), color="black", label='Ajuste',linewidth=0.8)
    #plt.plot(np.exp(xfinal), np.exp(-1.517*xfinal + intercept+1.5), color="red",linewidth=0.5)
    #ax1.scatter(10**(xfinal), 10**(yfinal), color='orange')
    #====================================
    
    #########################
    #########################
    
    ax2 = fig.add_subplot(122)
    
    #====================================
    lim_grafico = lim_grafico
    tau = tau
    q = (tau+2)/tau
    print('q: ', round(q,3))

    # Grafico datos
    binsretorno = np.linspace(lim_grafico[0]-0.5,lim_grafico[1]+0.5,int(((-lim_grafico[0]+lim_grafico[1])/2)+2))
    #binsretorno = np.linspace(lim_grafico[0]-0.5,lim_grafico[1]+0.5,int((-lim_grafico[0]+lim_grafico[1]+2)/10))
    y_tot, bin_edges_tot = np.histogram(dataretorno, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],int((-lim_grafico[0]+lim_grafico[1])/2+1)).astype(int)
    #x_tot = np.linspace(lim_grafico[0],lim_grafico[1],int((-lim_grafico[0]+lim_grafico[1]+2)/10)-1).astype(int)
    p00_tot = np.amax(y_tot)
    mask = y_tot != 0   # Máscara booleana que quita los puntos del histograma que valdrían cero 
    x_tot = x_tot[mask]
    y_tot = y_tot[mask] # (joden al calcularles el log pq log(0) es menos inf)
    y_tot = y_tot/p00_tot 
    
    y_tot=np.log(y_tot) # Graficamos el logaritmo de los datos, en lugar de usar escala logarítmica
    ax2.scatter(x_tot, 10**(y_tot), label=label, color=color, marker=marker, s=10, facecolor='none')
    #-------------------------------- 
    # Ajustar los datos

    popt1=0
    popt=0
    if qg == True:
        dataretorno = separar_par_impar(dataretorno)[0]  # El ajuste lo hago en la rama par  
        binsretorno = np.linspace(int_ajusteqg[0]-0.5,int_ajusteqg[1]+0.5,-int_ajusteqg[0]+int_ajusteqg[1]+2)
        #binsretorno = np.linspace(int_ajuste[0]-0.5,int_ajuste[1]+0.5,int((-int_ajuste[0]+int_ajuste[1]+2)/10))
        y, bin_edges_tot = np.histogram(dataretorno, binsretorno)
        x = np.linspace(int_ajusteqg[0],int_ajusteqg[1],-int_ajusteqg[0]+int_ajusteqg[1]+1).astype(int)
        #x = np.linspace(int_ajuste[0],int_ajuste[1],int((-int_ajuste[0]+int_ajuste[1]+2)/10)-1).astype(int)
        p00 = np.amax(y)
        mask = y != 0   # mascara booleana que quita los puntos del histograma que valdrían cero 
        x = x[mask]
        y = y[mask] # (joden al calcularles el log pq log(0) es menos inf)
        y = y/p00
        y = np.log(y)
                                                                              
        # Le quitamos a x los valores entre -30,30 para que el pico donde se abre no lo tome en el ajuste
        #x_filtrado = x[(x <= int_excluido[0]) | (x >= int_excluido[1])]
        #y_filtrado = y[(x <= int_excluido[0]) | (x >= int_excluido[1])]
        popt1, pcov = curve_fit(qgaussian_log, x, y, p0=initial_guess1)#, bounds=([0,0], [np.inf,np.inf]))
        print(label)
        print('beta: ',round(popt1[0],3), 'sin redondear: ',popt1)
    
        #x_filtrado_mayor = x_filtrado[x_filtrado >= 0]
        #x_filtrado_menor = x_filtrado[x_filtrado <= 0]
        #######ax2.plot(x, 10**(qgaussian_log(x, popt1[0])), color='red', linewidth=0.8)
        #ax2.plot(x_filtrado_mayor, 10**(qgaussian_log(x_filtrado_mayor, popt1[0])), color='red',label=f'Ajuste $f(x)$, $q = {q:.2f}$', linewidth=0.8)
        #ax2.plot(x_filtrado_menor, 10**(qgaussian_log(x_filtrado_menor, popt1[0])), color='red', linewidth=0.8)
        
        x_proy = np.linspace(int_graficado[0],int_graficado[1],-int_graficado[0]+int_graficado[1]+1).astype(int)
        #x_proy_mayor = x_proy[x_proy >= x_filtrado[-1]]
        #x_proy_menor = x_proy[x_proy <= x_filtrado[0]]
        
        #ax2.plot(x_proy_mayor, 10**(qgaussian_log(x_proy_mayor, popt1[0])), color='black', linestyle='--' , linewidth=0.8)#label='Proyección'
        #ax2.plot(x_proy_menor, 10**(qgaussian_log(x_proy, popt1[0])), color='black', linestyle='--' , linewidth=0.8)#label='Proyección'
        ax2.plot(x_proy, 10**(qgaussian_log(x_proy, popt1[0])), color='black', linestyle='-.' , linewidth=0.8,label=f'Ajuste $g(x)$, $q = {q:.2f}$')
        
        xx=1   # Punto para la leyenda
        yy=1
        ax2.scatter(xx, yy, color='none', label=f'$\\beta={round(popt1[0],2)}$')
    
        
    if f == True:
        dataretorno = separar_par_impar(dataretorno)[0]  # El ajuste lo hago en la rama par  
        binsretorno = np.linspace(int_ajuste[0]-0.5,int_ajuste[1]+0.5,-int_ajuste[0]+int_ajuste[1]+2)
        #binsretorno = np.linspace(int_ajuste[0]-0.5,int_ajuste[1]+0.5,int((-int_ajuste[0]+int_ajuste[1]+2)/10))
        y, bin_edges_tot = np.histogram(dataretorno, binsretorno)
        x = np.linspace(int_ajuste[0],int_ajuste[1],-int_ajuste[0]+int_ajuste[1]+1).astype(int)
        #x = np.linspace(int_ajuste[0],int_ajuste[1],int((-int_ajuste[0]+int_ajuste[1]+2)/10)-1).astype(int)
        p00 = np.amax(y)
        mask = y != 0   # mascara booleana que quita los puntos del histograma que valdrían cero 
        x = x[mask]
        y = y[mask] # (joden al calcularles el log pq log(0) es menos inf)
        y = y/p00
        y = np.log(y)
                                                                              
        # Le quitamos a x los valores entre -30,30 para que el pico donde se abre no lo tome en el ajuste
        x_filtrado = x[(x <= int_excluido[0]) | (x >= int_excluido[1])]
        y_filtrado = y[(x <= int_excluido[0]) | (x >= int_excluido[1])]
        popt, pcov = curve_fit(FUNC_log, x_filtrado, y_filtrado, p0=initial_guess, bounds=([0,0], [np.inf,np.inf]))

        print(label)
        print('aq: ',round(popt[0],3), 'sin redondear: ',popt[0])
        print('a1: ',round(popt[1],10), 'sin redondear: ',popt[1])

        #x_filtrado_mayor = x_filtrado[x_filtrado >= 0]
        #x_filtrado_menor = x_filtrado[x_filtrado <= 0]
        #########ax2.plot(x_filtrado_mayor, 10**(FUNC_log(x_filtrado_mayor, *popt)), color='black',label=f'Ajuste $f(x)$, $q = {q:.2f}$', linewidth=0.8)
        #########ax2.plot(x_filtrado_menor, 10**(FUNC_log(x_filtrado_menor, *popt)), color='black', linewidth=0.8)
        #ax2.plot(x, 10**(FUNC_log(x, *popt)), color='black',label=f'Ajuste $f(x)$, $q = {q:.2f}$', linewidth=0.8)
        
        x_proy = np.linspace(int_graficado[0],int_graficado[1],-int_graficado[0]+int_graficado[1]+1).astype(int)
        #x_proy_mayor = x_proy[x_proy >= x_filtrado[-1]]
        #x_proy_menor = x_proy[x_proy <= x_filtrado[0]]
        #ax2.plot(x_proy_mayor, 10**(FUNC_log(x_proy_mayor, *popt)), color='black', linestyle='--' , linewidth=0.8)#label='Proyección'
        #ax2.plot(x_proy_menor, 10**(FUNC_log(x_proy_menor, *popt)), color='black', linestyle='--' , linewidth=0.8)#label='Proyección'
        ax2.plot(x_proy, 10**(FUNC_log(x_proy, *popt)), color='black', linestyle='-' , linewidth=0.8,label=f'Ajuste $f(x)$, $q = {q:.2f}$')
        
        xx=1   # Punto para la leyenda
        yy=1
        ax2.scatter(xx, yy, color='none', label=f'$a_q={round(popt[0],3)}$\n$a_1={round(popt[1],13)}$')
        
    #-------------------------------- 
    
    
    if ig == True:
        ax2.plot(x_tot, 10**(qgaussian_log(x_tot, initial_guess)), color='red', linewidth=0.8, linestyle='--',
             label='initial guess')
    
    #ax2.plot(x_proy, 10**(qgaussian_log(x_proy, 0.05)), color='red', linestyle='--' , linewidth=0.8)#label='Proyección'
    
    
    #===================== PARÁMETROS AX1

    ax1.yaxis.set_ticks_position('both')
    ax1.tick_params(labelleft=True,labelright=False)
    ax1.xaxis.set_ticks_position('both')
    ax1.tick_params(labelbottom=True,labeltop=False)
    # Aumentar el tamaño de la fuente en los ejes
    #ax1.tick_params(axis='x', labelsize=18, length=6, width=1)
    #ax1.tick_params(axis='y', labelsize=18, length=6, width=1)
    # Configurar las marcas menores en el eje y
    ax1.tick_params(axis='y', which='minor', size=3)
    ax1.yaxis.set_ticks_position('both')
    ax1.tick_params(labelleft=True,labelright=False)
    ax1.xaxis.set_ticks_position('both')
    ax1.tick_params(labelbottom=True,labeltop=False)
    #ax1.set_title("distribución deltas (fluctuation lenght)")
    ax1.set_yscale('log')
    ax1.set_xscale('log')
    ax1.set_xlabel('$\lambda$',fontsize = 10)
    ax1.set_ylabel('$P(\lambda)/P(\lambda_{máx})$', fontsize = 10)
    #plt.xticks(fontsize = 15)
    ax1.legend(fontsize = 10)
    ax1.set_xlim(0.5, lim_escala)
    
    #===================== PARÁMETROS AX2

    #plt.title('AJUSTE QG + G con q fijo')
    ax2.set_xlabel('$\Delta \lambda$ (retornos)',fontsize = 10)
    ax2.set_ylabel('$P(\Delta \lambda)/P(0)$',fontsize = 10)
    #ax1.legend()
    #ax2.set_xlim(lim_grafico[0],lim_grafico[1])
    #ax1.set_ylim(lim_graficoy[0],lim_graficoy[1])
    # Aumentar el tamaño de la fuente en los ejes
    #ax2.tick_params(axis='x', labelsize=18, length=6, width=1)
    #ax2.tick_params(axis='y', labelsize=18, length=6, width=1)
    # Configurar las marcas menores en el eje y
    #ax2.tick_params(axis='y', which='minor', size=3)
    ax2.yaxis.set_ticks_position('both')
    ax2.tick_params(labelleft=True,labelright=False)
    ax2.xaxis.set_ticks_position('both')
    ax2.tick_params(labelbottom=True,labeltop=False)
    ax2.set_yscale("log")
    ax2.set_xscale("linear")
    ax2.legend(fontsize = 10)
    
    ax2.set_ylim(5E-14,10)
    ax2.set_xlim(lim_grafico[0],lim_grafico[1])
    
    fig.tight_layout()
   
    #fig.savefig('/home/mjdomenech/TrabajoFinal/Figuras/OVERLEAF/resultados-marzo/1-AJUSTES_09_norm-val-max100.pdf', format='pdf')
    
    if save_fig == True:
        #fig.savefig(pwdgraf+nombre_archivo+'.pdf', format='pdf')
        fig.savefig(pwdgraf+nombre_archivo+'.png', dpi=600)
    
    #fig.show()
    
    return popt1, popt


popt1, popt = grafico(datadelta,lim_escala,intervalo1,   dataretorno,lim_grafico,tau,int_ajusteqg,int_ajuste,int_graficado,initial_guess1,initial_guess,ig,qg,f,int_excluido,   color,marker,label,pwdgraf,nombre_archivo,save_fig)


def grafico_zoomzoom(dataretorno,lim_graficoZOOM,popt1,popt,   color,marker,label,pwdgraf,nombre_archivo,save_fig,qg,f):
        
    fig = plt.figure(figsize = [4.8, 3.5], layout='tight')
        
    ax2 = fig.add_subplot(111)

    #====================================
    lim_grafico = lim_graficoZOOM

    # Grafico datos
    binsretorno = np.linspace(lim_grafico[0]-0.5,lim_grafico[1]+0.5,-lim_grafico[0]+lim_grafico[1]+2)
    y_tot, bin_edges_tot = np.histogram(dataretorno, binsretorno)
    x_tot = np.linspace(lim_grafico[0],lim_grafico[1],-lim_grafico[0]+lim_grafico[1]+1).astype(int)
    p00_tot = np.amax(y_tot)
    mask = y_tot != 0   # Máscara booleana que quita los puntos del histograma que valdrían cero 
    x_tot = x_tot[mask]
    y_tot = y_tot[mask] # (joden al calcularles el log pq log(0) es menos inf)
    y_tot = y_tot/p00_tot
    y_tot=np.log(y_tot) # Graficamos el logaritmo de los datos, en lugar de usar escala logarítmica
    ax2.scatter(x_tot, 10**(y_tot), label=label, color=color, marker=marker, s=10, facecolor='none')

    # Grafico curva con los parámetros ajustados
  
    if qg == True:
        ax2.plot(x_tot, 10**(qgaussian_log(x_tot, popt1[0])), color='black', linestyle='-.', linewidth=0.8)
    
    if f == True:
        ax2.plot(x_tot, 10**(FUNC_log(x_tot, *popt)), color='black', linewidth=0.8)
    
    #ax2.plot(x_tot, 10**(qgaussian_log(x_tot, 0.05)), color='red', linestyle='--' , linewidth=0.8)#label='Proyección'
   
    #=========PARAMETROS AX2================
    #ax2.set_xlim(lim_grafico[0],lim_grafico[1])
    #ax2.set_ylim(1E-5,0.5E1)

    # Aumentar el tamaño de la fuente en los ejes
    ax2.tick_params(axis='x', labelsize=15, length=4, width=1)
    ax2.tick_params(axis='y', labelsize=15, length=4, width=1)

    # Configurar las marcas menores en el eje y
    ax2.tick_params(axis='y', which='minor', size=3)
    ax2 .yaxis.set_ticks_position('both')
    ax2.tick_params(labelleft=True,labelright=False)
    ax2.xaxis.set_ticks_position('both')
    ax2.tick_params(labelbottom=True,labeltop=False)
    ax2.set_yscale('log')
       
    if save_fig == True:
        #fig.savefig(pwdgraf+nombre_archivo+'ZOOMZOOM'+'.pdf', format='pdf')
        fig.savefig(pwdgraf+nombre_archivo+'ZOOMZOOM'+'.png', dpi=600)

        #fig.show()

grafico_zoomzoom(dataretorno,lim_graficoZOOM,popt1,popt,  color,marker,label,pwdgraf,nombre_archivo,save_fig,qg,f)  
    