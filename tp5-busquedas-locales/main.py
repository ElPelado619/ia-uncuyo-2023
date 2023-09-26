import hillclimbing as hc
import simannealing as sa
import genetic as ga
import time
import numpy as np
import matplotlib.pyplot as plt

# Función que guarda una tupla de valores en un archivo CSV sin borrar el contenido previo
# Parámetros: values - Tupla de valores a guardar.
#             name - Nombre del archivo CSV.
def save_csv(values,name):
    # Abre el archivo en modo append.
    file = open(name + ".csv","a")
    # Escribe los valores en el archivo.
    file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) 
               + "," + str(values[4]) +  "\n")
    # Cierra el archivo.
    file.close()

def solver(n,max_states,option):
    if option == 1:
        return hc.hill_climbing(n,max_states,False)
    elif option == 2:
        return sa.simulated_annealing(n,max_states,100,0.99)
    elif option == 3:
        return ga.genetic_algorithm(n,5,1000,0.1,4,False)
    

def avg_and_std(n,name,option):
    # Arreglo nulo de 30 elementos
    states = [0 for i in range(30)]
    times = [0 for i in range(30)]
    hs = [0 for i in range(30)]

    for i in range(30):
        # Empieza a contar el tiempo
        start = time.time()

        # Ejecuta el algoritmo para 1000 reinas y 10000 estados.
        result = solver(n,10000,option)

        # Termina de contar el tiempo
        end = time.time()

        # Almacena el tiempo de ejecución.
        times[i] = end - start

        # Almacena el número de estados evaluados.
        states[i] = result[2]

        # Almacena el valor de la función H.
        hs[i] = result[1]

        if option == 1:
            save_csv(("Hill Climbing",n,times[i],states[i],hs[i]),"results")
        elif option == 2:
            save_csv(("Simulated Annealing",n,times[i],states[i],hs[i]),"results")
        elif option == 3:
            save_csv(("Genetic Algorithm",n,times[i],states[i],hs[i]),"results")
        

    return times, states, hs

for n in [4,8,10,12,15]:
    print("\n")
    t1, s1, h1 = avg_and_std(n,"Hill Climbing",1)
    print("Avg for " + str(n) + " queens in Hill Climbing: " + str(np.average(t1)) + " s")

    print("\n")
    t2, s2, h2 = avg_and_std(n,"Simulated Annealing",2)
    print("Avg for " + str(n) + " queens in Simulated Annealing: " + str(np.average(t2)) + " s")

    print("\n") 
    t3, s3, h3 = avg_and_std(n,"Genetic Algorithm",3)
    print("Avg for " + str(n) + " queens in Genetic Algorithm: " + str(np.average(t3)) + " s")


    # Grafica en un grafico de cajas y bigotes los tiempos de ejecución de los dos algoritmos,
    # y permite que las cajas tengan diferentes colores.
    plt.boxplot([t1,t2,t3],labels=["Hill Climbing","Simulated Annealing","Genetic Algorithm"],patch_artist=True)

    # Dibuja la grilla del grafico de color gris y transparencia de 0.2
    plt.grid(color='gray',alpha=0.2)

    plt.title("Execution time for " + str(n) + " queens")
    plt.ylabel("Time (s)")

    # Muestra los valores maximos y minimos con una precision de 4 decimales
    plt.text(1.1,np.max(t1),str(np.round(np.max(t1),4)))
    plt.text(1.1,np.min(t1),str(np.round(np.min(t1),4)))
    plt.text(2.1,np.max(t2),str(np.round(np.max(t2),4)))
    plt.text(2.1,np.min(t2),str(np.round(np.min(t2),4)))

    plt.show()


