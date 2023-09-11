from queue import PriorityQueue

def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def astar(matrix, start, end):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # Cola de prioridad para A* 
    open_list = PriorityQueue()
    open_list.put((0, start))  # (f(n), nodo)
    came_from = {}  # To reconstruct the path

    g_score = {point: float('inf') for point in start}
    g_score[start] = 0

    while not open_list.empty():
        _, current = open_list.get()

        if current == end:
            # Reconstruye el camino
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            return True, path

        visited[current[0]][current[1]] = True

        # Define movimientos posibles
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            new_x, new_y = current[0] + dx, current[1] + dy

            if is_valid(new_x, new_y, rows, cols) and not visited[new_x][new_y] and (matrix[new_x][new_y] == 0 or matrix[new_x][new_y] == 3):
                tentative_g_score = g_score[current] + 1  # Asume un costo de uno para moverse de una celda hacia otra

                if tentative_g_score < g_score.get((new_x, new_y), float('inf')):
                    came_from[(new_x, new_y)] = current
                    g_score[(new_x, new_y)] = tentative_g_score
                    f_score = tentative_g_score + euclidean_distance((new_x, new_y), end)
                    open_list.put((f_score, (new_x, new_y)))

    return False, None  # No se encontró un camino