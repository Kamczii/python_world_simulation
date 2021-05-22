import random
from organisms.Organism import Organism


class Plant(Organism):
    """"Plant inherits organism, additionally can multiply"""
    def __init__(self, strength, color, x, y, world):
        super().__init__(strength, 0, color, x, y, world)

    def multiplication(self):
        not_taken_neighbour = self.world.get_not_taken_neighbour(self.x, self.y)
        if not_taken_neighbour is not None:
            type_to_create = type(self)
            new_object = type_to_create(not_taken_neighbour[0], not_taken_neighbour[1], self.world)
            self.world.add_organism(new_object)

    def collide(self, colliding, attacked):
        pass

    def action(self):
        rand = random.randint(0, 15)
        if rand == 0:
            self.multiplication()
