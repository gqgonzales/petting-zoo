from datetime import date

# ---------------------- LANDLUBBERS ----------------------


class Llama:
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.shift = ""
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walpiper = True


class Donkey:
    def __init__(self, name, species, shift):
        self.name = ""
        self.species = ""
        self.shift = ""
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walpiper = True


class Goat:
    def __init__(self, name, species, shift):
        self.name = ""
        self.species = ""
        self.shift = ""
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walpiper = True


class Cow:
    def __init__(self, name, species, shift):
        self.name = ""
        self.species = ""
        self.shift = ""
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walpiper = True


class Horse:
    def __init__(self, name, species, shift):
        self.name = ""
        self.species = ""
        self.shift = ""
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walpiper = True


# miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning")
# eeyore = Donkey("Eeyore", "blue donkey", "afternoon")
betsy = Cow("Betsy", "cow", "midday")
# lats = Goat("Lats", "shorthair mountain goat", "afternoon")
# legolas = Horse("Legolas", "black horse", "midday")
print(
    f"{betsy.name} the {betsy.species} is available to pet during the {betsy.shift} shift."
)
