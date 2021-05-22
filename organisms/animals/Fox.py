import COLORS
from organisms.animals.Animal import Animal


class Fox(Animal):
    def __init__(self, x, y, world):
        super().__init__(3, 7, COLORS.FOX_COLOR, x, y, world)

    def action(self):
        ax, ay = self.draw_direction()

        taken = self.world.taken(self.x + ax, self.y + ay)

        if taken is not None and taken.strength > self.strength:
            print("Fox has stopped because of stronger opponent ", self.x, self.y)
            return
        self.move(ax, ay)
