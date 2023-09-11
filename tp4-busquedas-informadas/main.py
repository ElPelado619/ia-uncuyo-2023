# PUDISTE SINCRONIZAR

import grid
import A_star_search as astar
import numpy as np
import matplotlib.pyplot as plt


# Dimensiones de la grilla
GRID_SIZE = 100
CELL_SIZE = 7  # Tamaño de cada celda en píxeles
OBSTACLE_PERCENTAGE = 8

dataset = [None] * 30

# Generación del conjunto de datos
for k in range (0,30):
    dataset[k] = grid.init_grid(GRID_SIZE,CELL_SIZE,OBSTACLE_PERCENTAGE)

# RESOLUCIÓN CON A*
astar_states = [None] * 30
for i in range (0,30):
    print("\n[ITERACION " + str(i+1) + "]")
    (matrix,start,end) = dataset[i]
    (is_solvable,path) = astar.astar(matrix,start,end)

    if is_solvable:
        print("Se encontró un camino.")
        astar_states[i] = len(path)
        print("Cantidad de estados: " + str(astar_states[i]))
    else:
        print("No se encontró un camino.")

    # csv_tuple = ("BFS",i+1,astar_states[i],is_solvable)

    # with open(csv_file, mode='a', newline='') as archivo_csv:
    #     # Crea un objeto escritor CSV
    #     writer = csv.writer(archivo_csv)

    #     writer.writerow(csv_tuple)



#[IMPRIMIR RESULTADOS]

print("\nRESULTADOS DE A*\n")

print(sorted(astar_states))

avg = np.average(astar_states)
std = np.std(astar_states)

print("Promedio: " + str(avg) + "\nDesv. Estandar: " + str(std))

plt.boxplot(astar_states)
plt.show()