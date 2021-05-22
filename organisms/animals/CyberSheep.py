import COLORS
import CONSTANTS
import World
from organisms.animals.Sheep import Sheep


class CyberSheep(Sheep):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.strength = 11
        self.__color = COLORS.CYBER_SHEEP_COLOR

    @property
    def color(self):
        return self.__color

    def distance(self, organism):
        return World.calc_distance(organism.x, organism.y, self.x, self.y)

    def action(self):
        pine_borsch = list(filter(lambda org: org.get_name() == "PineBorscht", self.world.organisms))
        if any(True for _ in pine_borsch):
            minimal = min(pine_borsch, key=self.distance)
            if minimal is not None:
                dis_x = minimal.x - self.x
                dis_y = minimal.y - self.y
                if dis_x > 0:
                    self.move(*CONSTANTS.RIGHT_DIRECTION)
                elif dis_x < 0:
                    self.move(*CONSTANTS.LEFT_DIRECTION)
                elif dis_y < 0:
                    self.move(*CONSTANTS.UP_DIRECTION)
                elif dis_y > 0:
                    self.move(*CONSTANTS.DOWN_DIRECTION)
                else:
                    print("Implement cyber")
                    super().action()
        else:
            super().action()
