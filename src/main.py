from src.models.Entity import *
from src.helpers.constants import *


def main():
    welcome = "Welcome to Dungeons and Deadlifts!"
    dog_attrs = {STR: 16, CON: 8, DEX: 13, INT: 8, WIS: 6, CHA: 16}
    Entity("Doggo", align=CG, race="Dog", armor_class=14, hit_points=20, attrs=dog_attrs)

    gen_at = generate_attrs()
    genny = Entity(attrs=gen_at)

    print(welcome)


main()


print("See you soon!")