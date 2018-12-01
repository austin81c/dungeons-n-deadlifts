from src.models.Entity import *
from src.helpers.constants import *
from src.tracker.Log import *

class Main:

    main_log=None

    def log_workout(self):
        l = LogItem(description="died", dxd_skill="Necromancy", duration=30, irl_type="blah")
        self.main_log.log_event(l)


    def open_character(self):
        gen_at = generate_attrs()
        genny = Entity(name="You", race="Human", attrs=gen_at)


    def cli_loop(self):
        cmd = -1
        while cmd != 0:
            print("What would you like to do?")
            print("1: Log Workout")
            print("2: Character")
            print("0: Exit")
            raw_cmd=input(">")
            cmd = int(raw_cmd)
            print(cmd)
            switcher = {
                1: self.log_workout,
                2: self.open_character
            }
            switcher.get(cmd, -1)()
            print()



    def __init__(self):
        welcome = "Welcome to Dungeons and Deadlifts!"
        # dog_attrs = {STR: 16, CON: 8, DEX: 13, INT: 8, WIS: 6, CHA: 16}
        # Entity("Doggo", align=CG, race="Dog", armor_class=14, hit_points=20, attrs=dog_attrs)
        # gen_at = generate_attrs()
        # genny = Entity(attrs=gen_at)
        self.main_log = Log()
        print(welcome)


m = Main()
m.cli_loop()
print("See you soon!")