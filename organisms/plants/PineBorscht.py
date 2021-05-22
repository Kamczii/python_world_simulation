import random

import COLORS
from organisms.animals.Animal import Animal
from organisms.plants.Plant import Plant


class PineBorscht(Plant):
    def __init__(self, x, y, world):
        super().__init__(10, COLORS.PINE_BORSCHT_COLOR, x, y, world)

    def collide(self, colliding, attacked):
        if colliding.get_name() != "CyberSheep":
            self.world.remove_organism(colliding)

    def action(self):
        rand = random.randint(0, 15)
        if rand == 0:
            self.multiplication()

        neighbours = self.world.get_neighbours_set(self.x, self.y)
        organisms = [organism for organism in self.world.organisms if (organism.x, organism.y) in neighbours]
        results = filter(lambda organism: organism.get_name() != "CyberSheep" and issubclass(type(organism), Animal),
                         organisms)
        for result in results:
            print(self.get_name() + " kills " + result.get_name())
            self.world.remove_organism(result)
