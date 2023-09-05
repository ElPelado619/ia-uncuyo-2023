# PUDISTE SINCRONIZAR

import grid
import bfsearch as bf
import dfsearch as df
import limited_dfs as ldf
import ucsearch as uc
import numpy as np
import matplotlib.pyplot as plt
import csv

csv_file = 'results.csv'

with open(csv_file, mode='a', newline='') as archivo_csv:
    # Crea un objeto escritor CSV
    writer = csv.writer(archivo_csv)

# Dimensiones de la grilla
GRID_SIZE = 100
CELL_SIZE = 7  # Tamaño de cada celda en píxeles
OBSTACLE_PERCENTAGE = 8

dataset = [None] * 30

# Generación del conjunto de datos
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

    csv_tuple = ("BFS",i+1,bfs_states[i],is_solvable)

    with open(csv_file, mode='a', newline='') as archivo_csv:
        # Crea un objeto escritor CSV
        writer = csv.writer(archivo_csv)

        writer.writerow(csv_tuple)



# RESOLUCIÓN CON DFS
dfs_states = [None] * 30
for i in range (0,30):
    print("\n[ITERACION " + str(i+1) + "]")
    (matrix,start,end) = dataset[i]
    (is_solvable,path) = df.dfs(matrix,start,end)

    if is_solvable:
        print("Se encontró un camino.")
        dfs_states[i] = len(path)
        print("Cantidad de estados: " + str(dfs_states[i]))
    else:
        print("No se encontró un camino.")

    csv_tuple = ("DFS",i+1,dfs_states[i],is_solvable)

    with open(csv_file, mode='a', newline='') as archivo_csv:
        # Crea un objeto escritor CSV
        writer = csv.writer(archivo_csv)

        writer.writerow(csv_tuple)

# RESOLUCIÓN CON LIMITED DFS
ldfs_states = [None] * 30
ldfs_solved = [False] * 30
for i in range (0,30):
    print("\n[ITERACION " + str(i+1) + "]")
    (matrix,start,end) = dataset[i]
    (is_solvable,path) = ldf.dfs(matrix,start,end,int(np.average(dfs_states)))

    if is_solvable:
        print("Se encontró un camino.")
        ldfs_states[i] = len(path)
        ldfs_solved[i] = True
        print("Cantidad de estados: " + str(ldfs_states[i]))
    else:
        print("No se encontró un camino.")
        ldfs_states[i] = int(np.average(dfs_states))
        print("Cantidad de estados: " + str(ldfs_states[i]))

    csv_tuple = ("LDFS",i+1,ldfs_states[i],is_solvable)

    with open(csv_file, mode='a', newline='') as archivo_csv:
        # Crea un objeto escritor CSV
        writer = csv.writer(archivo_csv)

        writer.writerow(csv_tuple)

# RESOLUCIÓN CON UCS
ucs_states = [None] * 30
for i in range (0,30):
    print("\n[ITERACION " + str(i+1) + "]")
    (matrix,start,end) = dataset[i]
    (is_solvable,path) = uc.ucs(matrix,start,end)

    if is_solvable:
        print("Se encontró un camino.")
        ucs_states[i] = len(path)
        print("Cantidad de estados: " + str(ucs_states[i]))
    else:
        print("No se encontró un camino.")

    csv_tuple = ("UCS",i+1,ucs_states[i],is_solvable)

    with open(csv_file, mode='a', newline='') as archivo_csv:
        # Crea un objeto escritor CSV
        writer = csv.writer(archivo_csv)

        writer.writerow(csv_tuple)

#[IMPRIMIR RESULTADOS]

print("\nRESULTADOS DE BFS\n")

print(sorted(bfs_states))

avg = np.average(bfs_states)
std = np.std(bfs_states)

print("Promedio: " + str(avg) + "\nDesv. Estandar: " + str(std))

plt.boxplot(bfs_states)
plt.show()

print("\nRESULTADOS DE DFS\n")

print(sorted(dfs_states))

avg = np.average(dfs_states)
std = np.std(dfs_states)

print("Promedio: " + str(avg) + "\nDesv. Estandar: " + str(std))

plt.boxplot(dfs_states)
plt.show()

print("\nRESULTADOS DE DFS LIMITADO\n")

print(sorted(ldfs_states))
ldfs_solved = [y for y,x in sorted(zip(ldfs_solved,ldfs_states))]
print(sorted(ldfs_solved,key=None,reverse=True))

avg = np.average(ldfs_states)
std = np.std(ldfs_states)

print("Promedio: " + str(avg) + "\nDesv. Estandar: " + str(std))

plt.boxplot(ldfs_states)
plt.show()

print("\nRESULTADOS DE UCS\n")

print(sorted(ucs_states))


avg = np.average(ucs_states)
std = np.std(ucs_states)

print("Promedio: " + str(avg) + "\nDesv. Estandar: " + str(std))

plt.boxplot(ucs_states)
plt.show()

plt.boxplot([bfs_states,dfs_states,ldfs_states,ucs_states])
plt.show()