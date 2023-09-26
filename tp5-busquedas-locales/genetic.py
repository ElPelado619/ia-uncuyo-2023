import random
import matplotlib.pyplot as plt

def fitness(board):
    # Función de adaptación: Cantidad de pares de reinas en conflicto.
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def tournament_selection(population, tournament_size):
    # Selección por torneo.
    selected = random.sample(population, tournament_size)
    return min(selected, key=fitness)

def single_point_crossover(parent1, parent2):
    # Cruce de un solo punto.
    n = len(parent1)
    crossover_point = random.randint(1, n - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual, mutation_rate):
    # Mutación de un individuo.
    if random.random() < mutation_rate:
        n = len(individual)
        gene_to_mutate = random.randint(0, n - 1)
        new_position = random.randint(0, n - 1)
        individual[gene_to_mutate] = new_position

def genetic_algorithm(N, population_size, max_generations, mutation_rate, tournament_size, print_h):
    population = [[random.randint(0, N - 1) for _ in range(N)] for _ in range(population_size)]
    generations = 0
    hs = []

    while generations < max_generations:
        new_population = []

        for _ in range(population_size):
            parent1 = tournament_selection(population, tournament_size)
            parent2 = tournament_selection(population, tournament_size)
            child1, child2 = single_point_crossover(parent1, parent2)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population
        generations += 1
        best_individual = min(population, key=fitness)
        hs.append(fitness(best_individual))

    if print_h:
        plt.plot(range(max_generations), hs)
        plt.title("Genetic Algorithm")
        plt.ylabel("Fitness")
        plt.xlabel("Generations")
        plt.show()

    return best_individual, fitness(best_individual), max_generations
