import random
from fitness import fitness_function
from selection import tournament_selection, roulette_selection
from crossover import cyclic_crossover, pmx_crossover
from mutation import mutate
from reinsertion import reinsertion_ordered, reinsertion_elitism
from utils import generate_population, is_valid_individual

class GeneticAlgorithm:
    def __init__(self, population_size, num_generations, crossover_rate, mutation_rate, 
                 selection_method, crossover_method, reinsertion_method):
        self.population_size = population_size
        self.num_generations = num_generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.selection_method = selection_method
        self.crossover_method = crossover_method
        self.reinsertion_method = reinsertion_method

        # Gera a população inicial
        self.population = generate_population(population_size)
        self.evaluate_population()

    def evaluate_population(self):
        """Calcula o fitness de cada cromossomo na população."""
        for individual in self.population:
            individual['fitness'] = fitness_function(individual['chromosome'])

    def select_parents(self):
        if self.selection_method == 'tournament':
            return tournament_selection(self.population)
        return roulette_selection(self.population)

    def crossover(self, parent1, parent2):
        """Seleciona o método de crossover baseado na configuração."""
        if self.crossover_method == 'cyclic':
            return cyclic_crossover(parent1, parent2)
        elif self.crossover_method == 'pmx':
            return pmx_crossover(parent1, parent2)
        else:
            raise ValueError(f"Unknown crossover method: {self.crossover_method}")

    def mutate(self, individual):
        """Aplica a mutação no cromossomo do indivíduo."""
        return mutate(individual, self.mutation_rate)


    def reinsertion(self, parents, offspring):
        if self.reinsertion_method == 'ordered':
            return reinsertion_ordered(parents, offspring)
        elif self.reinsertion_method == 'elitism':
            return reinsertion_elitism(parents, offspring, elitism_rate=0.2)
        else:
            raise ValueError(f"Unknown reinsertion method: {self.reinsertion_method}")

    def run(self):
        for generation in range(self.num_generations):
            self.evaluate_population()
            best_individual = min(self.population, key=lambda ind: ind['fitness'])
            print(f"Generation {generation}: Best Fitness = {best_individual['fitness']}")
            
            # Adicione mais informações para verificar o progresso
            print(f"Best Chromosome: {best_individual['chromosome']}")

            offspring = []
            for _ in range(self.population_size // 2):
                parent1, parent2 = self.select_parents()

                if isinstance(parent1, dict) and isinstance(parent2, dict):
                    if random.random() < self.crossover_rate:
                        child1_chromosome, child2_chromosome = self.crossover(parent1['chromosome'], parent2['chromosome'])
                    else:
                        child1_chromosome, child2_chromosome = parent1['chromosome'], parent2['chromosome']

                    child1 = {'chromosome': child1_chromosome, 'fitness': None}
                    child2 = {'chromosome': child2_chromosome, 'fitness': None}

                    child1 = self.mutate(child1)
                    child2 = self.mutate(child2)

                    if is_valid_individual(child1) and is_valid_individual(child2):
                        offspring.append(child1)
                        offspring.append(child2)

            for individual in offspring:
                if individual['fitness'] is None:
                    individual['fitness'] = fitness_function(individual['chromosome'])

            self.population = self.reinsertion(self.population, offspring)

            best_individual = min(self.population, key=lambda ind: ind['fitness'])
            if fitness_function(best_individual['chromosome']) == 0:
                print(f"Solution found: {best_individual['chromosome']}")
                return best_individual['chromosome']
            
        print("No valid solution found.")
        return None


