from .animal import Animal
from movements import Swimming


class Catfish(Animal, Swimming):
    def __init__(self, name, species, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        # no more self.swimming = True

    def purr(self):
        print("The fish seems very happy!")

    def swim(self):
        print(f"{self} swims, briskly!")

    def __str__(self):
        return f"{self.name} the Catfish"
