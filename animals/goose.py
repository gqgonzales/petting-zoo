from .animal import Animal
from movements import Walking, Swimming
from datetime import date


class Goose(Animal, Walking, Swimming):
    def __init__(self, name, species, food, chip_num):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
        # no more self.swimming = True

    def feed(self):
        print(
            f'{self.name} is very picky and will ONLY eat {self.food}. The last feed time was on {date.today().strftime("%m/%d/%Y")}.'
        )

    def honk(self):
        print("The goose honks. A lot")

    def walk(self):
        print(f"{self} waddles")

    def __str__(self):
        return f"{self.name} the Goose"


# class Goose(Animal):

#     # Remove redundant properties from Llama's initialization, and set their values via Animal
#     def __init__(self, name, species, food, chip_num):
#         super().__init__(name, species, food, chip_num)
#         self.swimming = True

#     def feed(self):
#         print(
#             f'{self.name} is very picky and will ONLY eat {self.food}. The last feed time was on {date.today().strftime("%m/%d/%Y")}.'
#         )
