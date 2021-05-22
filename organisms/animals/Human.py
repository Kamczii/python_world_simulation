import COLORS
from organisms.animals.Animal import Animal


class Human(Animal):
    def __init__(self, x, y, world):
        super().__init__(5, 4, COLORS.HUMAN_COLOR, x, y, world)
        self.__willing_to_move_x = 0
        self.__willing_to_move_y = 0
        self.__special = 0

    def copulate(self, colliding):
        pass

    def action(self):
        super().move(self.__willing_to_move_x, self.__willing_to_move_y)
        self.whole_burn()

    def willing_to_move(self, x, y):
        self.__willing_to_move_x = x
        self.__willing_to_move_y = y

    def special_ability(self):
        if self.__special == 0:
            self.color = COLORS.HUMAN_COLOR_SPECIAL
            self.__special = 10

    def whole_burn(self):
        if self.__special > 5:
            neighbours = self.world.get_neighbours_set(self.x, self.y)
            results = [organism for organism in self.world.organisms if (organism.x, organism.y) in neighbours]
            for result in results:
                self.world.remove_organism(result)
            self.__special -= 1
        elif self.__special > 0:
            self.color = COLORS.HUMAN_COLOR
            self.__special -= 1

