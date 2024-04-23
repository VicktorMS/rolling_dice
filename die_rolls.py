from die import Die
import numpy as np


def prod_between_rolls(rolls, dies):
    results = []
    for _ in range(rolls):
            result = np.array([die.roll() for die in dies])
            operation_result = np.prod(result) 
            results.append(operation_result)   
    return results


def sum_between_rolls(rolls, dies):
    results = []
    for _ in range(rolls):
            result = np.array([die.roll() for die in dies])
            operation_result = np.sum(result) 
            results.append(operation_result)        
    return results


def die_rolls(operation, rolls, dies):
    results = []
    frequencies = []
    max_result = 0

    dice_sides = np.array([die.num_sides for die in dies])

    if operation == '+':
        results = sum_between_rolls(rolls)
        max_result = np.sum(dice_sides)          

    elif operation == '*':
        results = prod_between_rolls(rolls)
        max_result = np.prod(dice_sides)                         

    else:
        raise ValueError("Operação não suportada. Escolha '+' ou '*'.")


    for value in range(len(dies), max_result + 1):
        value_frequency = results.count(value)
        frequencies.append(value_frequency)

    return frequencies

