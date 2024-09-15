import random
import pandas as pd

def generate_population(population_size):
    """Gera uma população inicial de permutações válidas dos dígitos de 0 a 9, com 8 dígitos por indivíduo."""
    population = []
    digits = list(range(10))  # Dígitos possíveis de 0 a 9
    for _ in range(population_size):
        chromosome = random.sample(digits, 8)  # Gera uma permutação aleatória de 8 dígitos
        population.append({'chromosome': chromosome, 'fitness': None})
    return population

def is_valid_individual(individual):
    chromosome = individual['chromosome']
    return len(set(chromosome)) == len(chromosome)  # Verifica se todos os dígitos são únicos

def save_results_to_csv(df, filename):
    df.to_csv(filename, index=False)

