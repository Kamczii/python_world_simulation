import CONSTANTS
from organisms.Organism import Organism

import random

from organisms.plants.Plant import Plant


class Animal(Organism):
    """Animal inherits organism, additionally can move, fight, eat and copulate"""
    def __init__(self, strength, initiative, color, x, y, world):
        super().__init__(strength, initiative, color, x, y, world)
        self.fight_avoided = False

    def collide(self, colliding, attacked):
        if attacked:
            colliding.collide(self, False)
            if not colliding.fight_avoided:
                self.fight(colliding)
            else:
                colliding.fight_avoided = False

    def copulate(self, colliding):
        not_taken_neighbour = self.world.get_not_taken_neighbour(self.x, self.y)
        if not_taken_neighbour is not None:
            type_to_create = type(colliding)
            new_object = type_to_create(not_taken_neighbour[0], not_taken_neighbour[1], self.world)
            self.world.add_organism(new_object)

    def action(self):
        direction = self.draw_direction()
        self.move(*direction)

    def move(self, ax, ay):
        if ax == 0 and ay == 0:
            return
        new_x = self.x + ax
        new_y = self.y + ay

        new_x = self.world.return_to_map_x(new_x)
        new_y = self.world.return_to_map_y(new_y)

        if new_x == self.x and new_y == self.y:  # obiekt stoi w miejscu
            return

        colliding = self.world.taken(new_x, new_y)

        if colliding is not None and colliding.age > 0 and self.age > 0:
            if isinstance(self, type(colliding)):
                self.copulate(colliding)
            elif issubclass(type(colliding), Plant):
                self.eat(colliding)
                self.x = new_x
                self.y = new_y
            else:
                self.collide(colliding, True)
                self.x = new_x
                self.y = new_y
        else:
            self.x = new_x
            self.y = new_y

    def fight(self, colliding):
        print("Fight occured " + self.get_name() + " and " + colliding.get_name())
        if self.strength > colliding.strength:
            self.world.remove_organism(colliding)
            print(self.get_name() + " won")
        elif self.strength < colliding.strength:
            self.world.remove_organism(self)
            print(colliding.get_name() + " won")
        else:  # wygrywa atakujacy
            self.world.remove_organism(colliding)
            print(self.get_name() + " won")

    def eat(self, colliding):
        print(self.get_name()+" eats "+colliding.get_name())
        colliding.collide(self, False)
        self.world.remove_organism(colliding)

    @staticmethod
    def draw_direction():
        rand = random.randint(0, 3)

        if rand == 0:
            return CONSTANTS.LEFT_DIRECTION
        elif rand == 1:
            return CONSTANTS.RIGHT_DIRECTION
        elif rand == 2:
            return CONSTANTS.UP_DIRECTION
        elif rand == 3:
            return CONSTANTS.DOWN_DIRECTION
