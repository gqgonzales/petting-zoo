from .animal import Animal
from movements import Swimming


class Goldfish(Animal, Swimming):
    def __init__(self, name, species, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        # no more self.swimming = True

    def chirp(self):
        print("The fish seems very happy!")

    def swim(self):
        print(f"{self} swims gracefully.")

    def __str__(self):
        return f"{self.name} the Goldfish"
