from collections import deque

def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def bfs(matrix, start, end):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start, [])])  # Guarda el camino hasta este punto como una lista vacía

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            # Imprimir el camino
            print("Camino desde la raiz hasta el objetivo:")
            for step in path:
                print("-> " + str(step), end=' ')
            return (True,path)  # Encontramos el destino

        # Definir movimientos (arriba, abajo, izquierda, derecha)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, rows, cols) and not visited[new_x][new_y] and (matrix[new_x][new_y] == 0 or matrix[new_x][new_y] == 3):
                # Agregar el paso al camino
                new_path = path + [(new_x, new_y)]
                queue.append(((new_x, new_y), new_path))
                visited[new_x][new_y] = True

    return (False,None)  # No se encontró un camino

