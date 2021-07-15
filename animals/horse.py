from animals.animals import Animal
from datetime import date


class Horse(Animal):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift  # stays on Llama because not all animals have shifts
        self.walking = True
