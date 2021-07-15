from animals import (
    Llama,
    Donkey,
    Goat,
    Cow,
    Horse,
    CoralSnake,
    GardenSnake,
    Copperhead,
    Cobra,
    Diamondback,
    Goldfish,
    Mallard,
    Swan,
    Goose,
    Catfish,
)
from attractions import SnakePit, PettingZoo, Wetlands

# from animals.slithering import CoralSnake, GardenSnake, Copperhead, Cobra, Diamondback, Goldfish, Mallard, Swan, Goose, Catfish, SnakePit, PettingZoo, Wetlands
# from animals.swimming import Goldfish, Mallard, Swan, Goose, Catfish
# from attractions import SnakePit, PettingZoo, Wetlands

# ---------------------- VARMINT VILLAGE ----------------------

varmint_village = PettingZoo("Varmint Village")

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")
eeyore = Donkey("Eeyore", "blue donkey", "afternoon", "cantaloupe")
betsy = Cow("Betsy", "cow", "midday", "grass")
lats = Goat("Lats", "shorthair mountain goat", "afternoon", "tin cans")
legolas = Horse("Legolas", "black horse", "midday", "honeydew")

varmint_village.add_animal(betsy)
varmint_village.add_animal(lats)

for animal in varmint_village.animals:
    print(
        f"You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}"
    )


# ---------------------- SLITHER INN ----------------------

slither_inn = SnakePit("Slither Inn")

king = CoralSnake("King", "coral snake", "field mice")
kevin = GardenSnake("Kevin", "garden snake", "little lizards")
jewel = Copperhead("Jewel", "pit viper", "whatever she wants")
nikki = Cobra("Nikki", "king cobra", "field mice")
flora = Diamondback("Flora", "western diamondback rattlesnake", "sour patch kids")

slither_inn.add_animal(king)

for animal in slither_inn.animals:
    print(
        f"You can find {animal.name} the {animal.species} in {slither_inn.attraction_name}"
    )

# ---------------------- CRITTER COVE ----------------------

critter_cove = Wetlands("Critter Cove")

sam = Goldfish("Sam", "freshwater goldfish", "fish flakes")
lucas = Mallard("Lucas", "duck", "white bread")
gloria = Swan("Gloria", "swan", "lollipops")
sally = Goose("Sally", "goose", "PB&J")
piper = Catfish("Piper", "alabama catfish", "french fries")

critter_cove.add_animal(sam)
critter_cove.add_animal(lucas)
critter_cove.add_animal(gloria)
critter_cove.add_animal(sally)


# Critter Cove is where you'll find big birds and lil swimmers unite, like
#    - Swooney the fainting goat
#    - Wilbur the pot-bellied pig
#    - Linda the domesticated llama

print(
    f"{critter_cove.attraction_name} is where you'll find {critter_cove.description}, like"
)
for animal in critter_cove.animals:
    print(f"– {animal.name}")
