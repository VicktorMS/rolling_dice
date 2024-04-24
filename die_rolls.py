from die import Die
import numpy as np


"""
    Realiza rolagens de dados e retorna os resultados baseados na operação especificada.

    Args:
    - rolls: O número de rolagens a serem feitas.
    - dies: Uma lista de objetos Die representando os dados a serem rolados.
    - operation: A operação a ser realizada entre os resultados das rolagens ('+' para soma, '*' para multiplicação).

    Returns:
    - Uma lista contendo as frequências dos resultados das rolagens.
    """
def die_rolls(rolls, dies, operation):

    if operation not in ['+', '*', '-']:
        raise ValueError("Operação não suportada. Escolha '+' e '*'.")

    results = []
    frequencies = []

    if operation == '+':
        roll_function = np.sum
        max_result = np.sum([die.num_sides for die in dies])          

    elif operation == '*':
        roll_function = np.prod
        max_result = np.prod([die.num_sides for die in dies])          


    for _ in range(rolls):
        result = roll_function([die.roll() for die in dies])
        results.append(result)

    for value in range(len(dies), max_result + 1):
        value_frequency = results.count(value)
        frequencies.append(value_frequency)

    return frequencies, max_result



