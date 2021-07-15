from .attractions import Attraction


class SnakePit(Attraction):
    def __init__(self, name):
        self.attraction_name = name
        self.description = "creepy crawlies love to hang, but be careful"
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)
