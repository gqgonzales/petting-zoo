from .animals import Animal
from datetime import date


class Goat(Animal):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift  # stays on Llama because not all animals have shifts
        self.walking = True

    def feed(self):
        print(
            f'{self.name} is very picky and will ONLY eat {self.food}. The last feed time was on {date.today().strftime("%m/%d/%Y")}.'
        )
