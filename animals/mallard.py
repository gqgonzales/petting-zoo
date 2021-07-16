from .animals import Animal


class Mallard(Animal):

    # Remove redundant properties from Llama's initialization, and set their values via Animal
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True
