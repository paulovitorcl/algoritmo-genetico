import time
import pandas as pd
from genetic_algorithm_2 import GeneticAlgorithm
from utils import save_results_to_csv

# Definindo os problemas
problems = [
    {
        'letters': ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y'],
        'addends': ['SEND', 'MORE'],
        'result': 'MONEY'
    },
    {
        'letters': ['E', 'A', 'T', 'H', 'T', 'O', 'P', 'L'],
        'addends': ['EAT', 'THAT'],
        'result': 'APPLE'
    },
    {
        'letters': ['C', 'R', 'O', 'S', 'D', 'A', 'N', 'G', 'E'],
        'addends': ['CROSS', 'ROADS'],
        'result': 'DANGER'
    },
    {
        'letters': ['C', 'O', 'A', 'L', 'G', 'E', 'R'],
        'addends': ['COCA', 'COLA'],
        'result': 'OASIS'
    },
    {
        'letters': ['D', 'O', 'N', 'A', 'L', 'G', 'R', 'B', 'T'],
        'addends': ['DONALD', 'GERALD'],
        'result': 'ROBERT'
    }
]


# Configurações para o experimento
configurations = [
    {'selection_method': 'tournament', 'crossover_method': 'cyclic', 'mutation_method': 'swap', 'reinsertion_method': 'ordered'} #1   
]

def run_experiment(config, problem):

    # Other configurations
    population_size = 100
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
        reinsertion_method=config['reinsertion_method'],
        problem=problem
    )
    
    start_time = time.time()
    best_solution = ga.run()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    converged = best_solution is not None
    
    return {
        'problem': problem['result'],
        'converged': converged,
        'execution_time': elapsed_time,
        'best_solution': best_solution
    }

def main():
    # Get the output filename interactively from the user
    #output_filename = input("Enter the desired filename for the results (e.g., experiments_results.csv): ")

    output_filename = "resultados_2/results.csv"

    results = []
    for config in configurations:
        for problem in problems:
            for _ in range(100):  # Execute 100 times for each configuration
                result = run_experiment(config,problem)
                results.append(result)

    # Create a DataFrame for the results
    df = pd.DataFrame(results)

    # Save the results using the user-provided filename
    save_results_to_csv(df, output_filename)

    print("Results successfully saved to", output_filename)

if __name__ == "__main__":
    main()
