import numpy as np
from die import Die
from die_rolls import die_rolls

import pygal


def main():
    die_list = [Die(), Die()]
    rolls = 15000
    operation = '+'

    frequency, max_result = die_rolls(rolls=rolls, dies=die_list, operation=operation)

    hist = pygal.Bar()
    hist.title = f"Results of rolling a D12 and a D12 {rolls} times."

    hist.x_labels = list(range(len(die_list), max_result + 1))
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add(operation.join(["D" + str(die.num_sides) for die in die_list]), frequency)
    hist.render_to_file('dice_visual.svg')

if __name__ == '__main__':
    main()