import random

def tournament_selection(population):
    """Seleciona pais usando seleção por torneio."""
    tournament_size = 3
    selected = []
    for _ in range(tournament_size):
        competitor = random.choice(population)
        selected.append(competitor)
    return min(selected, key=lambda ind: ind['fitness']), min(selected, key=lambda ind: ind['fitness'])

def roulette_selection(population):
    """Seleciona pais usando seleção por roleta."""
    total_fitness = sum(ind['fitness'] for ind in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for ind in population:
        current += ind['fitness']
        if current > pick:
            return ind, random.choice(population)
    return random.choice(population), random.choice(population)

