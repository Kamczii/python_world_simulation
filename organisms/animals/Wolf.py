import COLORS
import CONSTANTS
from organisms.animals.Animal import Animal


class Wolf(Animal):
    def __init__(self, x, y, world):
        super().__init__(9, 5, COLORS.WOLF_COLOR, x, y, world)
