import random

# Attribute Constants
STR = "Strength"
CON = "Constitution"
DEX = "Dexterity"
INT = "Intelligence"
WIS = "Wisdom"
CHA = "Charisma"

# Alignment Constants
LG = "Lawful Good"
LN = "Lawful Neutral"
LE = "Lawful Evil"
NG = "Neutral Good"
NN = "True Neutral"
NE = "Neutral Evil"
CG = "Chaotic Good"
CN = "Chaotic Neutral"
CE = "Chaotic Evil"

# Default Entity attributes
DEFAULT_ATTRS = {STR: 9, CON: 9, DEX: 9, INT: 9, WIS: 9, CHA: 9}


# Generates pseudo-random attributes for Entity creation
# Utilizes the Roll 4, Pick 3 tabletop algorithm
def generate_attrs():
    attrs = DEFAULT_ATTRS.copy()
    for k, v in attrs.items():
        stat = dice_roll()
        attrs[k] = stat
    return attrs


def dice_roll() :
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    third = random.randint(1, 6)
    fourth = random.randint(1, 6)

    results = [first, second, third, fourth]
    results.sort()
    return results[0] + results[1] + results[2]

