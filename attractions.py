# class Attraction:
#     def __init__(self, name, description):
#         self.attraction_name = name
#         self.description = description
#         self.animals = list()

#     def add_animal(self, animal):
#         self.animals.append(animal)


# varmint_village = Attraction("Varmint Village", "cute and fuzzy critters to cuddle")
# slither_inn = Attraction("Slither Inn", "creepy crawlies rule")
# critter_cove = Attraction("Critter Cove", "big birds and lil swimmers unite")


class PettingZoo:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)


class SnakePit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "creepy crawlies love to hang, but be careful"
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)


class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "big birds and lil swimmers unite"
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)
