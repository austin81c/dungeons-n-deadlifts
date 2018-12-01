from src.helpers.constants import *


class Entity:
    def __init__(self, name="Default", align=NN, race="abstract", armor_class=6, hit_points=10, attrs=None):
        self.name = name
        self.attrs = DEFAULT_ATTRS if attrs is None else attrs
        self.align = align
        self.race = race
        self.armor_class = armor_class
        self.hit_points = hit_points

        print("Created: ", name, "--", align, race, "!")
        print("Attributes: ", self.attrs)
