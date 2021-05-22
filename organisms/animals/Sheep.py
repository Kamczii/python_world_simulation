import COLORS
from organisms.animals.Animal import Animal


class Sheep(Animal):
    def __init__(self, x, y, world):
        super().__init__(4, 4, COLORS.SHEEP_COLOR, x, y, world)