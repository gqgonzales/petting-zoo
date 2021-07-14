from datetime import date

# ---------------------- LANDLUBBERS ----------------------


class Llama:
    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walking = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


class Donkey:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walking = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


class Goat:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walking = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


class Cow:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walking = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


class Horse:
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walking = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')


# miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")
# eeyore = Donkey("Eeyore", "blue donkey", "afternoon", "cantaloupe")
# betsy = Cow("Betsy", "cow", "midday", "grass")
# lats = Goat("Lats", "shorthair mountain goat", "afternoon", "tin cans")
# legolas = Horse("Legolas", "black horse", "midday", "honeydew")
# print(
#     f"{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift."
# )
# print(miss_fuzz.feed())
