def fitness_function_2(chromosome, problem):
    letters_map = dict(zip(problem['letters'], chromosome))
    print(f"Letters map: {letters_map}")  # Debugging

    total = sum(to_number(word, letters_map) for word in problem['addends'])
    expected_result = to_number(problem['result'], letters_map)

    # Fitness value could be the absolute difference
    return abs(total - expected_result)

def to_number(word, letters_map):
    return sum(letters_map.get(char, 0) * 10**i for i, char in enumerate(reversed(word)))

