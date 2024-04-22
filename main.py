from die import Die
from die_rolls import sum_die_rolls

import pygal


def main():
    die_list = [Die(), Die(), Die()]
    rolls = 5000

    frequency = sum_die_rolls(rolls=rolls, dies=die_list)


    hist = pygal.Bar()
    hist.title = f"Results of rolling a D12 and a D12 {rolls} times."

    max_result = sum([die.num_sides for die in die_list])
    hist.x_labels = list(range(len(die_list), max_result + 1))

    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add(" + ".join(["D" + str(die.num_sides) for die in die_list]), frequency)
    hist.render_to_file('dice_visual.svg')

if __name__ == '__main__':
    main()