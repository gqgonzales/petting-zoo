from .attraction import Attraction


class Wetlands(Attraction):
    def __init__(self, name):
        self.attraction_name = name
        self.description = "big birds and lil swimmers unite"
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    @property  # The getter
    def last_critter_added(self):
        return self.animals[-1]
