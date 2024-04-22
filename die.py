from random import randint


class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
    # def roll(self, rolls=1):
    #     results = []
    #     for _ in range(rolls):
    #         results.append(randint(1, self.num_sides))
    #     return results
    