import time
import pandas as pd
from genetic_algorithm import GeneticAlgorithm
from utils import save_results_to_csv

# Configurações para o experimento
configurations = [
    {'selection_method': 'tournament', 'crossover_method': 'cyclic', 'mutation_method': 'swap', 'reinsertion_method': 'ordered'},
    {'selection_method': 'tournament', 'crossover_method': 'cyclic', 'mutation_method': 'swap', 'reinsertion_method': 'elitism'},
    # Adicione todas as combinações de configurações possíveis
]

def run_experiment(config):
    population_size = 50
    num_generations = 50
    crossover_rate = 0.8
    mutation_rate = 0.2
    
    ga = GeneticAlgorithm(
        population_size=population_size,
        num_generations=num_generations,
        crossover_rate=crossover_rate,
        mutation_rate=mutation_rate,
        selection_method=config['selection_method'],
        crossover_method=config['crossover_method'],
        reinsertion_method=config['reinsertion_method']
    )
    
    start_time = time.time()
    best_solution = ga.run()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    converged = best_solution is not None
    
    return {
        'selection_method': config['selection_method'],
        'crossover_method': config['crossover_method'],
        'mutation_method': config['mutation_method'],
        'reinsertion_method': config['reinsertion_method'],
        'converged': converged,
        'execution_time': elapsed_time,
        'best_solution': best_solution
    }

def main():
    results = []
    for config in configurations:
        for _ in range(100):  # Execute 100 vezes para cada configuração
            result = run_experiment(config)
            results.append(result)
    
    # Crie um DataFrame para os resultados
    df = pd.DataFrame(results)
    
    # Salve os resultados em um arquivo CSV
    save_results_to_csv(df, 'experiments_results.csv')

if __name__ == "__main__":
    main()
