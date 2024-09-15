from genetic_algorithm import GeneticAlgorithm

if __name__ == "__main__":
    # Configurações para o AG
    params = {
        'population_size': 100,
        'num_generations': 50,
        'crossover_rate': 0.6,
        'mutation_rate': 0.1,
        'selection_method': 'tournament',  # Alternativa: 'roulette'
        'crossover_method': 'cyclic',     # Alternativa: 'pmx'
        'reinsertion_method': 'ordered',  # Alternativa: 'elitism'
    }
    
    # Rodar o AG para o problema SEND+MORE=MONEY
    ga = GeneticAlgorithm(**params)
    solution = ga.run()

    if solution:
        print(f"Solution found: {solution}")
    else:
        print("No valid solution found.")
