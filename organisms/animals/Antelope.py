import random

import COLORS
from organisms.animals.Animal import Animal


class Antelope(Animal):
    def __init__(self, x, y, world):
        super().__init__(4, 4, COLORS.ANTELOPE_COLOR, x, y, world)

    def action(self):
        ax, ay = self.draw_direction()
        self.move(ax * 2, ay * 2)

    def collide(self, colliding, attacked):
        if attacked:
            rand = random.randint(0, 1)
            if rand == 0:
                colliding.collide(self, False)
                if not colliding.fight_avoided:
                    self.fight(colliding)
                else:
                    colliding.fight_avoided = False
            else:
                not_taken = self.world.get_not_taken_neighbour(self.x, self.y)
                if not_taken is not None:
                    self.x = not_taken[0]
                    self.y = not_taken[1]
                else:
                    colliding.collide(self, False)
                    if not colliding.fight_avoided:
                        self.fight(colliding)
                    else:
                        colliding.fight_avoided = False
        else:
            rand = random.randint(0, 1)
            if rand == 0:
                self.fight_avoided = True
                print("Antelope avoided fight with " + colliding.get_name())
