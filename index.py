from landlubbers import Llama, Donkey, Goat, Cow, Horse
from creepy_crawlies import Coral_Snake, Garden_Snake, Copperhead, Cobra, Diamondback
from sea_people import Goldfish, Mallard, Swan, Goose, Catfish
from attractions import varmint_village, critter_cove, slither_inn

# ---------------------- VARMINT VILLAGE ----------------------

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")
eeyore = Donkey("Eeyore", "blue donkey", "afternoon", "cantaloupe")
betsy = Cow("Betsy", "cow", "midday", "grass")
lats = Goat("Lats", "shorthair mountain goat", "afternoon", "tin cans")
legolas = Horse("Legolas", "black horse", "midday", "honeydew")

varmint_village.animals.append(miss_fuzz)
varmint_village.animals.append(eeyore)
varmint_village.animals.append(betsy)
varmint_village.animals.append(lats)
varmint_village.animals.append(legolas)

# for animal in varmint_village.animals:
#     print(
#         f"You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}"
#     )


# ---------------------- SLITHER INN ----------------------

king = Coral_Snake("King", "coral snake", "field mice")
kevin = Garden_Snake("Kevin", "garden snake", "little lizards")
jewel = Copperhead("Jewel", "pit viper", "whatever she wants")
nikki = Cobra("Nikki", "king cobra", "field mice")
flora = Diamondback("Flora", "western diamondback rattlesnake", "sour patch kids")

slither_inn.animals.append(king)
slither_inn.animals.append(kevin)
slither_inn.animals.append(jewel)
slither_inn.animals.append(nikki)
slither_inn.animals.append(flora)

# ---------------------- CRITTER COVE ----------------------

sam = Goldfish("Sam", "freshwater goldfish", "fish flakes")
lucas = Mallard("Lucas", "duck", "white bread")
gloria = Swan("Gloria", "swan", "lollipops")
sally = Goose("Sally", "goose", "PB&J")
piper = Catfish("Piper", "alabama catfish", "french fries")

critter_cove.animals.append(sam)
critter_cove.animals.append(lucas)
critter_cove.animals.append(gloria)
critter_cove.animals.append(sally)
critter_cove.animals.append(flora)
