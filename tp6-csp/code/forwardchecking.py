def is_valid(board, row, col, n, queen_positions):
    """
    Verifica si una reina puede ser colocada en la posición (row, col) del tablero sin amenazar a las demás reinas.
    """
    # Verificar si hay otra reina en la misma columna
    for i in range(n):
        if board[i][col] == 1:
            return False

    # Verificar si hay otra reina en la misma fila
    for j in range(n):
        if board[row][j] == 1:
            return False

    # Verificar si hay otra reina en las diagonales
    for i, j in queen_positions:
        if abs(row - i) == abs(col - j):
            return False

    return True

def n_queens_forward_checking(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    queen_positions = []
    state_count = [0]  # Variable para contar los estados explorados

    def forward_checking(board, col, n, queen_positions):
        state_count[0] += 1  # Incrementar el contador de estados explorados
        if col == n:
            return True

        for row in range(n):
            if is_valid(board, row, col, n, queen_positions):
                board[row][col] = 1
                queen_positions.append((row, col))

                if forward_checking(board, col + 1, n, queen_positions):
                    return True

                board[row][col] = 0
                queen_positions.pop()

        return False

    if forward_checking(board, 0, n, queen_positions):
        return board, state_count[0]
    else:
        return None,  state_count[0]




