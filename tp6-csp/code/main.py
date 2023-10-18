import time
import backtracking as bt
import forwardchecking as fc
import matplotlib.pyplot as plt

# Función para imprimir una solución
def imprimir_solucion(solucion):
    n = len(solucion)
    print(n)
    for i in range(n):
        for j in range(n):
            print(solucion[i][j], end=" ")
        print()
    print()

# Función para calcular el tiempo de ejecución de una función de CSP
def calcular_tiempo(n, funcion):
    # Iniciar temporizador
    inicio = time.time()
    
    # Llamar a la función correspondiente
    if funcion == "backtracking":
        solucion, estados = bt.n_queens_backtracking(n)
    elif funcion == "forwardchecking":
        solucion, estados =  fc.n_queens_forward_checking(n)

    # imprimir_solucion(solucion)
    
    # Detener temporizador y calcular tiempo transcurrido
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    
    # Devolver tiempo transcurrido
    return tiempo_transcurrido, estados

# Ejecutar calcular_tiempo 30 veces para cada n = 4, 8, 10, 12, 15 usando backtracking y forwardchecking
for n in [15]:
    print("n =", n)

    plt.figure()
    for funcion in ["backtracking", "forwardchecking"]:
        print("Función:", funcion)
        tiempos = []
        estados = []
        for i in range(30):
            tiempos.append(calcular_tiempo(n, funcion)[0])
            estados.append(calcular_tiempo(n, funcion)[1])
        #print("Tiempos:", tiempos)
        print("Tiempo promedio:", sum(tiempos) / len(tiempos))
        #print("Estados:", estados)
        print("Estado promedio:", sum(estados) / len(estados))
        print()

        if funcion == "backtracking":
            t1 = tiempos
            e1 = estados
        else:
            t2 = tiempos
            e2 = estados

    # Graficar tiempos en caja y bigote
    plt.boxplot([t1, t2], labels=["Backtracking", "Forward checking"])
    plt.title("Tiempos de ejecución para n = " + str(n))
    plt.ylabel("Tiempo (s)")

    # Guardar gráfico en archivo
    # plt.savefig("tiempos_n_" + str(n) + ".png")
    # plt.show()

    # Graficar estados en grafico de barras
    plt.bar(["Backtracking", "Forward checking"], [sum(e1) / len(e1), sum(e2) / len(e2)])
    plt.title("Estados explorados para n = " + str(n))
    plt.ylabel("Estados")

    # Guardar gráfico en archivo
    # plt.savefig("estados_n_" + str(n) + ".png")
    # plt.show()


       

 





