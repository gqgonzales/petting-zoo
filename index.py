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

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow", 5000)
eeyore = Donkey("Eeyore", "blue donkey", "afternoon", "cantaloupe", 5001)
betsy = Cow("Betsy", "cow", "midday", "grass", 5002)
lats = Goat("Lats", "shorthair mountain goat", "afternoon", "tin cans", 5003)
legolas = Horse("Legolas", "black horse", "midday", "honeydew", 5004)

varmint_village.add_animal(betsy)
varmint_village.add_animal(lats)

for animal in varmint_village.animals:
    print(
        f"You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}"
    )


# ---------------------- SLITHER INN ----------------------

slither_inn = SnakePit("Slither Inn")

king = CoralSnake("King", "coral snake", "field mice", 5005)
kevin = GardenSnake("Kevin", "garden snake", "little lizards", 5006)
jewel = Copperhead("Jewel", "pit viper", "whatever she wants", 5007)
nikki = Cobra("Nikki", "king cobra", "field mice", 5008)
flora = Diamondback("Flora", "western diamondback rattlesnake", "sour patch kids", 5009)

slither_inn.add_animal(king)
slither_inn.add_animal(kevin)

print(slither_inn.last_critter_added)


for animal in slither_inn.animals:
    print(
        f"You can find {animal.name} the {animal.species} at {slither_inn.attraction_name}"
    )

# ---------------------- CRITTER COVE ----------------------

critter_cove = Wetlands("Critter Cove")

sam = Goldfish("Sam", "freshwater goldfish", "fish flakes", 5010)
lucas = Mallard("Lucas", "duck", "white bread", 5011)
gloria = Swan("Gloria", "swan", "lollipops", 5012)
sally = Goose("Sally", "goose", "PB&J", 5013)
piper = Catfish("Piper", "alabama catfish", "french fries", 5014)

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

gloria.feed()
lats.feed()
sam.feed()
