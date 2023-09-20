import random
import matplotlib.pyplot as plt

# Función objetivo: Contabiliza la cantidad de pares de reinas amenazadas en el tablero.
# Parámetros: board - Lista de enteros que representa un tablero de ajedrez.
# Valor de retorno: Cantidad de pares de reinas amenazadas en el tablero.
def h(board):
    n = len(board)
    # Contador de pares de reinas amenazadas.
    h = 0
    # Recorre el tablero.
    for i in range(n):
        # Recorre el tablero a partir de la fila siguiente a la fila actual.
        for j in range(i+1, n):
            # Si las reinas están en la misma fila o en la misma diagonal, se incrementa el contador.
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                h += 1
    return h

# Algoritmo Hill Climbing para resolver el problema de las N reinas.
# Parámetros: n - Tamaño del tablero de ajedrez.
#             max_evaluations - Número máximo de estados a evaluar.
# Valor de retorno: Tupla con el estado final, el valor de la función H y el número de estados evaluados.
def hill_climbing(n, max_evaluations, print_h):
    # Genera un tablero aleatorio.
    current = [random.randint(0, n-1) for i in range(n)]
    # Evalúa el tablero generado.
    current_h = h(current)
    evaluations = 1
    hs = [current_h]
    # Ciclo principal del algoritmo.
    while evaluations < max_evaluations and current_h > 0:
        # Genera un nuevo tablero vecino.
        neighbor = [current[i] for i in range(n)]
        col = random.randint(0, n-1)
        row = random.randint(0, n-1)
        neighbor[col] = row
        # Evalúa el tablero generado.
        neighbor_h = h(neighbor)
        evaluations += 1
        hs.append(current_h)
        # Compara el tablero generado con el mejor tablero actual.
        if neighbor_h < current_h:
            current = neighbor
            current_h = neighbor_h
            # Si encuentra un tablero sin amenazas, termina la ejecución.
            if current_h == 0:
                break
    
    if current_h == 0 and print_h:
        evaluations += 1
        hs.append(current_h)
        # Grafica los valores de h respecto a cada iteración.
        plt.plot(range(evaluations), hs)
        plt.title("Hill Climbing")
        plt.ylabel("H")
        plt.xlabel("Iterations")
        plt.show()

    return current, current_h, evaluations


