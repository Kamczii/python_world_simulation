import pickle

import CONSTANTS
import random

from organisms.animals.Antelope import Antelope
from organisms.animals.CyberSheep import CyberSheep
from organisms.animals.Fox import Fox
from organisms.animals.Human import Human
from organisms.animals.Sheep import Sheep
from organisms.animals.Turtle import Turtle
from organisms.animals.Wolf import Wolf
from organisms.plants.Dandelion import Dandelion
from organisms.plants.Grass import Grass
from organisms.plants.Guarana import Guarana
from organisms.plants.PineBorscht import PineBorscht
from organisms.plants.WolfBerries import WolfBerries


def calc_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


class World:
    """Holds simulated world logic, responsible for simulating round and control the player if exist.
    Also it's responsible for saving and loading from a file."""

    AVAILABLE_TYPES = [
        Antelope,
        CyberSheep,
        Fox,
        Sheep,
        Turtle,
        Wolf,
        Dandelion,
        Grass,
        Guarana,
        PineBorscht,
        WolfBerries
    ]

    def __init__(self, width, height, organisms_count):
        self.__width = width
        self.__height = height
        self.__organisms = []
        self.__player = Human(0, 0, self)
        self.add_organism(self.player)
        self.init_world(organisms_count)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def organisms(self):
        return self.__organisms

    @property
    def player(self):
        return self.__player

    def do_round(self):
        for organism in self.__organisms:
            organism.action()
            organism.age += 1

    def return_to_map_x(self, new_x):
        if new_x < 0:
            new_x = 0
        elif new_x > self.width - 1:
            new_x = self.width - 1
        return new_x

    def return_to_map_y(self, new_y):
        if new_y < 0:
            new_y = 0
        elif new_y > self.height - 1:
            new_y = self.height - 1
        return new_y

    def taken(self, x, y):
        for organism in self.__organisms:
            if organism.x == x and organism.y == y:
                return organism
        return None

    def move_player(self, direction):
        if self.player is not None:
            if direction == CONSTANTS.LEFT:
                self.player.willing_to_move(*CONSTANTS.LEFT_DIRECTION)
            elif direction == CONSTANTS.RIGHT:
                self.player.willing_to_move(*CONSTANTS.RIGHT_DIRECTION)
            elif direction == CONSTANTS.UP:
                self.player.willing_to_move(*CONSTANTS.UP_DIRECTION)
            elif direction == CONSTANTS.DOWN:
                self.player.willing_to_move(*CONSTANTS.DOWN_DIRECTION)

    def special_ability(self):
        if self.player is not None:
            self.player.special_ability()

    def init_world(self, organisms_count):
        for x in range(organisms_count):
            rand_x = random.randint(0, self.width - 1)
            rand_y = random.randint(0, self.height - 1)
            while self.taken(rand_x, rand_y) is not None:
                rand_x = random.randint(0, self.width - 1)
                rand_y = random.randint(0, self.height - 1)

            rand_type = random.randint(0, len(self.AVAILABLE_TYPES) - 1)
            self.add_organism(self.AVAILABLE_TYPES[rand_type](rand_x, rand_y, self))

    def get_not_taken_neighbour(self, x, y):

        available = []

        neighbours = self.get_neighbours_set(x, y)

        for neighbour in neighbours:
            if self.taken(neighbour[0], neighbour[1]) is None:
                available.append(neighbour)

        length = len(available)
        if length > 0:
            rand = random.randint(0, length - 1)
            return available[rand]
        else:
            return None

    def remove_organism(self, organism):
        self.__organisms.remove(organism)

    def get_neighbours_set(self, x, y):
        neighbors = set()
        for w in range(x - 1, x + 2):
            for h in range(y - 1, y + 2):
                if w == x and h == y:
                    break
                w = self.return_to_map_x(w)
                h = self.return_to_map_x(h)
                neighbors.add((w, h))
        return neighbors

    def add_organism(self, organism):
        self.__organisms.append(organism)
        self.__organisms.sort(key=self.__sort_by_initiative)

    def load_state_from_file(self):
        try:
            with open(CONSTANTS.SAVE_FILE, "rb") as save_file:
                self.__organisms = pickle.load(save_file)
                self.player = next((organism for organism in self.__organisms if organism.get_name() == "Human"), None)
                print("Organisms loaded")
        except FileNotFoundError:
            print("File not found")

    def save_state_to_file(self):
        with open(CONSTANTS.SAVE_FILE, "wb") as save_file:
            pickle.dump(self.__organisms, save_file)
            print("Organisms saved to file")

    @staticmethod
    def __sort_by_initiative(e):
        return e.initiative
