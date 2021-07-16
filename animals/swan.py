from .animal import Animal
from movements import Walking, Swimming


class Swan(Animal, Walking, Swimming):
    def __init__(self, name, species, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
        # no more self.swimming = True

    def honk(self):
        print("The swan honks gracefully.")

    def __str__(self):
        return f"{self.name} the Swan"
