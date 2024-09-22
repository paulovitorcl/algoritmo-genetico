def fitness_function(individual):
    # Transformar o indivíduo em números SEND, MORE, e MONEY
    s, e, n, d, m, o, r, y = individual
    send = s * 1000 + e * 100 + n * 10 + d
    more = m * 1000 + o * 100 + r * 10 + e
    money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
    
    return abs((send + more) - money)
