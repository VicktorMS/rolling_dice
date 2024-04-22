from die import Die
import pygal

# Creating Two D6
die_1 = Die()
die_2 = Die(12)

results = []
frequencies = []
rolls = 50000


for roll in range(rolls):
    result = die_1.roll() + die_2.roll()
    results.append(result)


max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    value_frequency = results.count(value)
    frequencies.append(value_frequency)


hist = pygal.Bar()

hist.title = f'Results of rolling a D6 and a D10 50,000 times.' #Titulo principal
hist.x_labels = list(range(2, max_result + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"


hist.add(f'D6 + D6', frequencies) # Legenda
hist.render_to_file('die_visual.svg')