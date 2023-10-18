def is_valid(board, row, col):
    """
    Verifica si una reina puede ser colocada en la posición (row, col) del tablero sin amenazar a las demás reinas.
    """
    n = len(board)
    # Verificar si hay otra reina en la misma columna
    for i in range(n):
        if board[i][col] == 1:
            return False
    # Verificar si hay otra reina en la misma fila
    for j in range(n):
        if board[row][j] == 1:
            return False
    # Verificar si hay otra reina en la diagonal principal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i < n and j < n:
        if board[i][j] == 1:
            return False
        i += 1
        j += 1
    # Verificar si hay otra reina en la diagonal secundaria
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    # Si no se encontró ninguna amenaza, la posición es válida
    return True

def solve_n_queens(board, n, col, solutions, state_count):
    """
    Función recursiva que coloca las reinas en el tablero de manera secuencial.
    """
    # Si se han colocado todas las reinas, se encontró una solución
    if col == n:
        solutions.append([row[:] for row in board])
        return True
    # Intentar colocar la reina en cada fila de la columna actual
    for row in range(n):
        state_count[0] += 1  # Incrementar el contador de estados recorridos
        if is_valid(board, row, col):
            board[row][col] = 1
            # Si se encontró una solución, detener la recursión
            if solve_n_queens(board, n, col+1, solutions, state_count):
                return True
            board[row][col] = 0
    # Si no se encontró ninguna solución, devolver False
    return False

def n_queens_backtracking(n):
    """
    Función que resuelve el problema de las n reinas por backtracking.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    state_count = [0]  # Inicializar el contador de estados recorridos
    solve_n_queens(board, n, 0, solutions, state_count)
    return solutions[0], state_count[0]

