from datetime import date

# ---------------------- CREEPY CRAWLIES ----------------------


class Coral_Snake:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.slithering = False
        self.walking = False
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


class Garden_Snake:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.slithering = False
        self.walking = False
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


class Copperhead:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.slithering = False
        self.walking = False
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


class Cobra:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.slithering = False
        self.walking = False
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


class Diamondback:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.slithering = False
        self.walking = False
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


# king = Coral_Snake("King", "coral snake", "field mice")
# kevin = Garden_Snake("Kevin", "garden snake", "little lizards")
# jewel = Copperhead("Jewel", "pit viper", "whatever she wants")
# nikki = Cobra("Nikki", "king cobra, "field mice"")
# flora = Diamondback("Flora", "western diamondback rattlesnake", "sour patch kids")
