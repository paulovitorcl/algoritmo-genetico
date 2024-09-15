def reinsertion_ordered(parents, offspring):
    """Reinsere os indivíduos na população ordenando pelo fitness."""
    # Adicionar fitness aos indivíduos da prole
    for individual in offspring:
        if individual['fitness'] is None:
            individual['fitness'] = fitness_function(individual['chromosome'])

    # Garantir que os pais também tenham o fitness calculado
    for individual in parents:
        if individual['fitness'] is None:
            individual['fitness'] = fitness_function(individual['chromosome'])

    # Combinar pais e prole
    combined = parents + offspring

    # Ordenar a população combinada pelo fitness
    combined.sort(key=lambda ind: ind['fitness'])

    # Manter o tamanho da população original
    return combined[:len(parents)]


def reinsertion_elitism(parents, offspring, elitism_rate=0.2):
    num_elites = int(len(parents) * elitism_rate)
    elites = sorted(parents, key=lambda ind: ind['fitness'])[:num_elites]
    return elites + sorted(offspring, key=lambda ind: ind['fitness'])[:len(parents) - num_elites]
