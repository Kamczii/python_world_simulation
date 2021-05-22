import COLORS
from organisms.plants.Plant import Plant


class Guarana(Plant):
    def __init__(self, x, y, world):
        super().__init__(0, COLORS.GUARANA_COLOR, x, y, world)

    def collide(self, colliding, attacked):
        print("Increased strength of "+colliding.get_name())
        colliding.strength += 3
