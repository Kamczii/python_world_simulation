import COLORS
from organisms.plants.Plant import Plant


class Grass(Plant):
    def __init__(self, x, y, world):
        super().__init__(0, COLORS.GRASS_COLOR, x, y, world)