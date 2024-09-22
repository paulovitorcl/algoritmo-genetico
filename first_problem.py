import time
import pandas as pd
from genetic_algorithm import GeneticAlgorithm
from utils import save_results_to_csv

# Configurações para o experimento
configurations = [
    {'selection_method': 'tournament', 'crossover_method': 'cyclic', 'mutation_method': 'swap', 'reinsertion_method': 'ordered'}, #1
    {'selection_method': 'tournament', 'crossover_method': 'cyclic', 'mutation_method': 'swap', 'reinsertion_method': 'elitism'}, #2  
    {'selection_method': 'tournament', 'crossover_method': 'pmx', 'mutation_method': 'swap', 'reinsertion_method': 'ordered'}, #3     
    {'selection_method': 'tournament', 'crossover_method': 'pmx', 'mutation_method': 'swap', 'reinsertion_method': 'elitism'}, #4     
    {'selection_method': 'roulette', 'crossover_method': 'cyclic', 'mutation_method': 'swap', 'reinsertion_method': 'ordered'}, #5     
    {'selection_method': 'roulette', 'crossover_method': 'cyclic', 'mutation_method': 'swap', 'reinsertion_method': 'elitism'} #6    
    #{'selection_method': 'roulette', 'crossover_method': 'pmx', 'mutation_method': 'swap', 'reinsertion_method': 'ordered'} #7        
    #{'selection_method': 'roulette', 'crossover_method': 'pmx', 'mutation_method': 'swap', 'reinsertion_method': 'elitism'} #8     
]

def run_experiment(config):
    # First configuration
    # population_size = 100
    # num_generations = 50
    # crossover_rate = 0.6
    # mutation_rate = 0.2

    # Other configurations
    population_size = 100
    num_generations = 50
    crossover_rate = 0.8
    mutation_rate = 0.2

    # Configurations 7 and 8 
    # population_size = 50
    # num_generations = 20
    # crossover_rate = 0.8
    # mutation_rate = 0.2
    
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
    # Get the output filename interactively from the user
    #output_filename = input("Enter the desired filename for the results (e.g., experiments_results.csv): ")

    output_filename = "resultados/results.csv"

    results = []
    for config in configurations:
        for _ in range(100):  # Execute 100 times for each configuration
            result = run_experiment(config)
            results.append(result)

    # Create a DataFrame for the results
    df = pd.DataFrame(results)

    # Save the results using the user-provided filename
    save_results_to_csv(df, output_filename)

    print("Results successfully saved to", output_filename)

if __name__ == "__main__":
    main()
