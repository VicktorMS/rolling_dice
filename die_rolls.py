from die import Die


def sum_die_rolls(rolls, dies):
    results = []
    frequencies = []

    for _ in range(rolls):
        result = [die.roll() for die in dies]
        results.append(sum(result))


    max_result = sum([die.num_sides for die in dies])

    for value in range(len(dies), max_result + 1):
        value_frequency = results.count(value)
        frequencies.append(value_frequency)

    return frequencies

