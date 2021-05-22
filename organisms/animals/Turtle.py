import random

import COLORS
from organisms.animals.Animal import Animal


class Turtle(Animal):
    def __init__(self, x, y, world):
        super().__init__(2, 1, COLORS.TURTLE_COLOR, x, y, world)

    def action(self):
        if random.randint(0, 3) == 0:
            super().action()

    def collide(self, colliding, attacked):
        if attacked:
            colliding.collide(self, False)
            if not colliding.fight_avoided:
                self.fight(colliding)
            else:
                colliding.fight_avoided = False
        else:
            if colliding.strength < 5:
                self.fight_avoided = True
                print("Turtle reflected attack of "+colliding.get_name())
