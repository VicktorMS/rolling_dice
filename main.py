import numpy as np
from die import Die
from die_rolls import die_rolls

import matplotlib.pyplot as plt


def main():
    die_list = [Die(12), Die()]
    rolls = 100000
    operation = '*'

    frequency, max_result = die_rolls(rolls=rolls, dies=die_list, operation=operation)
    die_numbers = list(range(len(die_list), max_result + 1))
    label = operation.join([f"D{str(die.num_sides)}" for die in die_list])


    fig, ax = plt.subplots()

    ax.bar(die_numbers, frequency, label=label, color='red')
    ax.set_ylabel('fruit supply')
    ax.set_title(f'{label} {"{:,}".format(rolls)} times')
    ax.legend(title='Dices')
    plt.show()

if __name__ == '__main__':
    main()