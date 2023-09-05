import heapq

def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def ucs(matrix, start, end):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = [(0, start, [])]  # (cost, (x, y), path)

    while queue:
        cost, (x, y), path = heapq.heappop(queue)

        if (x, y) == end:
            # Imprimir el camino
            print("Camino desde la raiz hasta el objetivo:")
            for step in path:
                print("-> " + str(step), end=' ')
            return (True, path)  # Encontramos el destino

        if visited[x][y]:
            continue

        visited[x][y] = True

        # Definir movimientos (arriba, abajo, izquierda, derecha)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, rows, cols) and (matrix[new_x][new_y] == 0 or matrix[new_x][new_y] == 3):
                # Calcular el costo acumulado
                new_cost = cost + 1 
                # Agregar el paso al camino
                new_path = path + [(new_x, new_y)]
                heapq.heappush(queue, (new_cost, (new_x, new_y), new_path))

    return (False, None)  # No se encontró un camino

