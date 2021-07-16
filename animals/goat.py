from .animal import Animal
from movements import Walking
from datetime import date


class Goat(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift
        # stays on Goat because not all animals have shifts

    def __str__(self):
        return f"{self.name} the Goat"

    def feed(self):
        print(
            f'{self.name} is very picky and will ONLY eat {self.food}. The last feed time was on {date.today().strftime("%m/%d/%Y")}.'
        )
