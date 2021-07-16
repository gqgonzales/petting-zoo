from .animal import Animal
from movements import Walking


# class Donkey(Animal):

#     # Remove redundant properties from Llama's initialization, and set their values via Animal
#     def __init__(self, name, species, shift, food, chip_num):
#         super().__init__(name, species, food, chip_num)
#         self.shift = shift  # stays on Llama because not all animals have shifts
#         self.walking = True


class Donkey(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift
        # stays on Donkey because not all animals have shifts

    def __str__(self):
        return f"{self.name} the Donkey"
