from .animal import Animal
from movements import Slithering


class Copperhead(Animal, Slithering):
    def __init__(self, name, species, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
        # no more self.swimming = True

    def __str__(self):
        return f"{self.name} the Copperhead"
