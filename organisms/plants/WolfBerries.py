import COLORS
from organisms.plants.Plant import Plant


class WolfBerries(Plant):
    def __init__(self, x, y, world):
        super().__init__(99, COLORS.WOLF_BERRIES_COLOR, x, y, world)

    def collide(self, colliding, attacked):
        self.world.remove_organism(colliding)