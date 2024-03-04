#using Threads
using Random
using DelimitedFiles
using Dates
include("funciones.jl")  # archivo funciones.jl que contiene las funciones



(alfa, N, l, cantidad_simulaciones) = ARGS   #ojo que los ARGS los toma como strings (aunque ingrese por ej: 0.01 100 10E4 5)

alfa_number = parse(Float64, alfa)
l_number = parse(Float64, l)
N_number = parse(Int, N)
cantidad_simulaciones_number = parse(Int, cantidad_simulaciones)



# CHEQUEO TIPOS
tipo1 = typeof(alfa_number)
tipo2 = typeof(alfa)
println("alfa_number es $alfa_number y de tipo $tipo1, mientras que alfa es $alfa y de tipo $tipo2")

tipo1 = typeof(N_number)
tipo2 = typeof(N)
println("N_number es $N_number y de tipo $tipo1, mientras que N es $l y de tipo $tipo2")

tipo1 = typeof(l_number)
tipo2 = typeof(l)
println("l_number es $l_number y de tipo $tipo1, mientras que l es $l y de tipo $tipo2")

tipo1 = typeof(cantidad_simulaciones_number)
tipo2 = typeof(cantidad_simulaciones)
println("cantidad_simulaciones_number es $cantidad_simulaciones_number y de tipo $tipo1, mientras que cantidad_simulaciones es $cantidad_simulaciones y de tipo $tipo2")
###



T = 300000   # INDICE T

alfastring = replace(string(alfa), "." => "")




Threads.@threads for i = 1:cantidad_simulaciones_number
        
    println("i = $i on thread $(Threads.threadid())")
    #comando = crear_comando(alfa,N,l,i)
    #print(string(comando))
    
    v = sistema(N_number, N_number/2, 0, 1)
    
    (delta, retorno, tejec, Ttotal) = evolucion_temporal_sin_s!(alfa_number,v,T,cant_puntos=l_number)
    
   
    fecha = Dates.format(Dates.now(), "yyyy-mm-dd-HH-MM-SS")
    -
    archivo_output = "/home/mjdomenech/TrabajoFinal/ArchivosCCAD/JuliaThreads/marzo1/output_"*alfastring*"_"*N*"_"*l*"_"*string(i)*"_"*fecha*".txt"
    
    open(archivo_output, "w") do file
    
        #redirect_stdout(file) # Redirigir la salida estándar al archivo
        
        
        println(file, "alfa_number:      ", alfa_number)
        println(file, "cantidad de puntos en distrib de retorno:      ", size(retorno, 1))
        println(file, "                                 delta: ", size(delta, 1))
        println(file, "pasos temporales por ciclo, T=", T)
        println(file, "tiempo de ejecución: ", tejec, " minutos")
        println(file, "pasos temp totales: ", Ttotal)
    
    end
    
    # Guardar arreglos en archivos
    archivo_retorno = "/home/mjdomenech/TrabajoFinal/ArchivosCCAD/JuliaThreads/marzo1/retorno_"*alfastring*"_"*N*"_"*l*"_"*string(i)*"_"*fecha*".txt"

    open(archivo_retorno, "w") do io
        writedlm(io, retorno)
    end

    archivo_delta = "/home/mjdomenech/TrabajoFinal/ArchivosCCAD/JuliaThreads/marzo1/delta_"*alfastring*"_"*N*"_"*l*"_"*string(i)*"_"*fecha*".txt"
    open(archivo_delta, "w") do io
        writedlm(io, delta)
    end

    archivo_tiempo = "/home/mjdomenech/TrabajoFinal/ArchivosCCAD/JuliaThreads/marzo1/tejec_"*alfastring*"_"*N*"_"*l*"_"*string(i)*"_"*fecha*".txt"
    open(archivo_tiempo, "w") do io
        writedlm(io, tejec)
    end
     
end


#esto no anda porque cada thread me abre y cierra el archivo y se hace lio
#fecha = Dates.format(Dates.now(), "yyyy-mm-dd-HH-MM-SS"
#archivo_stdout = "/home/mjdomenech/TrabajoFinal/ArchivosDurga/Julia/JuliaThreads/stdout_"*alfastring*"_"*N*"_"*l*fecha*".txt"
#open(archivo_stdout, "w") do out
#    redirect_stdout(out) # Redirigir la salida estándar al archivo
#    println("i = $i on thread $(Threads.threadid()) LISTO")
#end


#println(Threads.nthreads())
#println(Threads.threadid())