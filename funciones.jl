using Random
##using PyPlot

####################
# DEFINICIÓN SISTEMA
####################

function sistema(N, N0, e0, e1)
    """
    Función para armar array v (sistema).
    N: num total de partic. N0: cantidad con estado e0, N1: cantidad con estado e1.
    Devuelve array v.
    """
    v = []             #en Julia, los array y las listas son lo mismo :)
    N1 = N - N0
    
    for i in 1:N0
        push!(v, e0)
    end

    for i in 1:N1
        push!(v, e1)
    end
    
    #v = array(list1)    #esto no hace falta ya  
    
    return v             #en Julia, por defecto la función retorna la última variable que fue evaluada
end

########################
# EVOLUCIONES TEMPORALES
########################

function ehrenfest!(v)        #en Julia por convención, se pone ! al final del nombre para indicar que la función
                              #modifica el valor de sus argumentos, en este caso el array v (no solo produce un return)
    N = length(v)
    m = rand(1:N)             #da num aleatorio entre 1 y N (ambos incluidos). 
                              #los índices de los arrays en Julia van de 1 a N a diferencia de Python que van de 0 a N-1
    
    if v[m] == 1
        v[m] = 0
    elseif v[m] == 0
        v[m] = 1
    end
    
    return v
end

function votante!(v)
    N = length(v)
    m1 = rand(1:N)      # elige un número entero al azar entre 1 y N
    m2 = rand(1:N)
    
    while m2 == m1
        m2 = rand(1:N)
    end
    
    if v[m1] != v[m2]
        v[m2] = v[m1]
    end
    
    return v
end



function evolucion_ciclo_sin_s!(alfa, v, T, ciclo, s, k, delta, retorno)
    #println("--------------------------------------------------------------------------------------------")
    #println("adentro de un ciclo de $T pasos temp, k = $k al iniciar el ciclo número $ciclo")

    for i in 1:T                            # i = 1,2,3,...,T
        t_i = i                             # t_i = 1,2,3,...,T 
        t = (ciclo - 1) * T + t_i           # t = 1,2,3,...,T, T+1,T+2,...,2T, 2T+1,2T+2,...,3T 
        r = rand()

        if r <= alfa 
            ehrenfest!(v)                   
        elseif r >= alfa
            votante!(v)
        end

        push!(s, sum(v))                    
        N = length(v)                       # s tiene i+1 elementos
        if s[t_i+1] == N / 2                # s[1]=cond inicial, s[t_i+1]= s[2],s[3],...,
            push!(k, t)    
        end    
    end
end

function evolucion_temporal_sin_s!(alfa, v, T; multiples_ciclos=true, cant_puntos=20000)
    tic = time()

    ciclo = 0
    k = [0]                            #list_k = [0]      --------> condición inicial para t=0
    s = [sum(v)]                       #list_s = [sum(v)] --------> condición inicial para t=0
    delta = []                         #list_delta = []
    delta_sin_1 = [0]                  #list_delta_sin_1 = [0]
    retorno = []                       #list_retorno = []

    while length(delta_sin_1) < cant_puntos + 1
        ciclo += 1
        evolucion_ciclo_sin_s!(alfa, v, T, ciclo, s, k, delta, retorno)

        largok = length(k)

        for j in 1:(largok-1)
            push!(delta, k[j + 1] - k[j])  #push!(array, elemento) agrega "elemento" al final del array push!([1,2],5) da [1,2,5]
        end
        
        #calculo tamaño temporal fluctuaciones
        k_fin_ciclo = k[largok]
        k = [k_fin_ciclo]
        s = [sum(v)]

        delta_sin_1 = filter(x -> x != 1.0, delta)
        delta = delta_sin_1
                
        #println("reinicio k y s al finalizar el ciclo: k=$k, s=$s")
        #println("se aplicaron $T pasos temporales, hay $(length(delta_sin_1)) puntos en delta")

        if !multiples_ciclos  #"if not multiples_ciclos == True then break" es decir "if multiples_ciclos == False then break" 
            break
        end
    end

    largo_delta = length(delta)
    retorno = []


    for j in 1:(largo_delta-1)
        push!(retorno, delta[j + 1] - delta[j])
    end
    
    #retorno = collect(list_retorno)     esto no hace falta porque es cuando en python convertía la lista a array
    tiempo_ejec = (time() - tic) / 60
    Ttotal = T * ciclo

    return delta, retorno, tiempo_ejec, Ttotal
end




