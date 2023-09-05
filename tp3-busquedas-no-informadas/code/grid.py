import pygame
import random
import bfsearch as bf

# Función para dibujar la grilla
def draw_grid(grid, GRID_SIZE, CELL_SIZE, screen):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            color = (255, 255, 255)  # Color por defecto (celda vacía)
            if  grid[x][y] == 1:
                color = (0, 0, 0)  # Color de obstáculo
            elif grid[x][y] == 2:
                color = (255, 123, 0)
            elif grid[x][y] == 3:
                color = (230, 0, 255)
            pygame.draw.rect(screen, color, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Crear la grilla con obstáculos
def create_obstacle_grid(GRID_SIZE, OBSTACLE_PERCENTAGE):
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    num_obstacles = int((OBSTACLE_PERCENTAGE / 100) * GRID_SIZE * GRID_SIZE)

    # Crear obstáculos
    for _ in range(num_obstacles):
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        grid[x][y] = 1

    # Crear posición de llegada
    xs = random.randint(0, GRID_SIZE - 1)
    ys = random.randint(0, GRID_SIZE - 1)
    grid[xs][ys] = 2

    xf = random.randint(0, GRID_SIZE - 1)
    yf = random.randint(0, GRID_SIZE - 1)
    while xs == xf and ys == yf:
        xf = random.randint(0, GRID_SIZE - 1)
        yf = random.randint(0, GRID_SIZE - 1)
        
    grid[xf][yf] = 3
    return grid

def search_in_matrix(matrix, target):
    for row_index, row in enumerate(matrix):
        if target in row:
            col_index = row.index(target)
            return row_index, col_index
    return None, None  # El valor no fue encontrado

def init_grid(GRID_SIZE, CELL_SIZE,OBSTACLE_PERCENTAGE):
    # Inicializar pygame
    pygame.init()

    # Crear la ventana de visualización
    window_size = (GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Entorno del Agente")


    # Crear la grilla con obstáculos
    obstacle_grid = create_obstacle_grid(GRID_SIZE,OBSTACLE_PERCENTAGE)

    # Bucle principal de visualización
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dibujar la grilla en cada iteración
        draw_grid(obstacle_grid, GRID_SIZE, CELL_SIZE, screen)
        pygame.display.flip()

    start = search_in_matrix(obstacle_grid,2)
    end = search_in_matrix(obstacle_grid,3)

    # Salir
    pygame.quit()

    return (obstacle_grid,start,end)

