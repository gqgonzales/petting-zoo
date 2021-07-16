from .animal import Animal
from movements import Walking


class Llama(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift
        # stays on Llama because not all animals have shifts

    def __str__(self):
        return f"{self.name} the Llama"
