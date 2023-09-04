import grid
import bfsearch as bf
import numpy as np
import matplotlib.pyplot as plt

# Dimensiones de la grilla
GRID_SIZE = 100
CELL_SIZE = 7  # Tamaño de cada celda en píxeles
OBSTACLE_PERCENTAGE = 8

dataset = [None] * 30


# GENERACIÓN DEL CONJUNTO DE DATOS
for k in range (0,30):
    dataset[k] = grid.init_grid(GRID_SIZE,CELL_SIZE,OBSTACLE_PERCENTAGE)

# RESOLUCIÓN CON BFS
bfs_states = [None] * 30
for i in range (0,30):
    print("\n[ITERACION " + str(i+1) + "]")
    (matrix,start,end) = dataset[i]

    (is_solvable,path) = bf.bfs(matrix,start,end)
    if is_solvable:
        print("Se encontró un camino.")
        bfs_states[i] = len(path)
        print("Cantidad de estados: " + str(bfs_states[i]))
        
    else:
        print("No se encontró un camino.")

print(sorted(bfs_states))

avg = np.average(bfs_states)
std = np.std(bfs_states)

print("Promedio: " + str(avg) + "\nDesv. Estandar: " + str(std))

plt.boxplot(bfs_states)
plt.show()