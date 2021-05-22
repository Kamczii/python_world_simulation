from abc import ABC, abstractmethod


class Organism(ABC):
    """Basic representation of living organism"""
    def __init__(self, strength, initiative, color, x, y, world):
        self.strength = strength
        self.initiative = initiative
        self.x = x
        self.y = y
        self.age = 0
        self.world = world
        self.__color = color

    @property
    def color(self):
        return self.__color

    @abstractmethod
    def collide(self, colliding, attacked):
        pass

    @abstractmethod
    def action(self):
        pass

    def draw(self):
        self.world.draw()

    def get_name(self):
        return type(self).__name__
