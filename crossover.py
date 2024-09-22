import random

def cyclic_crossover(parent1, parent2):
    """
    Implementa o crossover cíclico entre dois cromossomos. 
    Se os pais não tiverem os mesmos elementos, retorne os pais originais.
    """
    # Verifica se ambos os pais têm os mesmos elementos (em qualquer ordem)
    if sorted(parent1) != sorted(parent2):
        # Se não forem permutações dos mesmos elementos, retorne os pais sem realizar o crossover
        return parent1, parent2

    size = len(parent1)
    child1 = [None] * size
    child2 = [None] * size

    # Ciclo inicial começa no índice 0
    index = 0
    while True:
        # Atribui genes dos pais aos filhos
        child1[index] = parent1[index]
        child2[index] = parent2[index]

        # Encontra o próximo índice para continuar o ciclo
        index = parent2.index(parent1[index])

        # Se o ciclo fechou, pare
        if index == 0:
            break

    # Preencher os genes restantes
    for i in range(size):
        if child1[i] is None:
            child1[i] = parent2[i]
        if child2[i] is None:
            child2[i] = parent1[i]

    return child1, child2



def pmx_crossover(parent1, parent2):
    size = len(parent1)
    child1, child2 = parent1[:], parent2[:]
    
    start, end = sorted([random.randint(0, size - 1) for _ in range(2)])
    
    # Troca de valores entre start e end
    child1[start:end], child2[start:end] = parent2[start:end], parent1[start:end]
    
    # Corrigir duplicações
    def fix(child, parent):
        for i in range(start, end):
            while child.count(child[i]) > 1:
                replacement = parent[i]
                for j in range(size):
                    if child[j] == replacement:
                        child[j] = child[i]
                        break
        return child
    
    return fix(child1, parent1), fix(child2, parent2)
