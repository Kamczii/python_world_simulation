import random

import COLORS
from organisms.plants.Plant import Plant


class Dandelion(Plant):
    def __init__(self, x, y, world):
        super().__init__(0, COLORS.DANDELION_COLOR, x, y, world)

    def action(self):
        for _ in range(3):
            rand = random.randint(0, 15)
            if rand == 0:
                self.multiplication()