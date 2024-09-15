import random

def mutate(individual, mutation_rate):
    chromosome = individual['chromosome']
    if isinstance(chromosome, list):
        for i in range(len(chromosome)):
            if random.random() < mutation_rate:
                idx1, idx2 = random.sample(range(len(chromosome)), 2)
                chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
        individual['chromosome'] = chromosome
    return individual


