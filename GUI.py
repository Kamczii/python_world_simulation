from tkinter import *

import COLORS
import CONSTANTS


class GUI(Frame):
    """Class responsible for displaying GUI, it is closely linked with World object"""

    SIZE = CONSTANTS.SIZE

    def __init__(self, world, master=None):
        self.world = world
        self.map = []

        super().__init__(master)
        master.title("World")
        master.configure(bg=COLORS.DEFAULT_GUI_BG)
        self.master = master
        self.make_gui()
        self.init_key_bindings()
        self.draw_world()
        mainloop()

    def make_gui(self):
        frame = Frame(self.master, width=self.world.width * self.SIZE)
        label = Label(frame, bg=COLORS.DEFAULT_GUI_BG,
                      text="STUDENT INDEX: 184374\tCONTROL=←↕→\tSPECIAL=X\tSAVE=S\tLOAD=L\tQUIT=ESCAPE",
                      height=3)
        label.grid(row=0)
        frame.pack()

        main_grid = Frame(
            self.master, bg=COLORS.DEFAULT_GUI_BG, width=self.world.width * self.SIZE, height=self.world.height * self.SIZE
        )
        main_grid.pack()

        for y in range(self.world.height):
            self.map.append([])
        for y in range(self.world.height):
            for x in range(self.world.height):
                frame = Frame(main_grid, bg=COLORS.DEFAULT_TILE_COLOR, width=self.SIZE, height=self.SIZE)
                frame.grid(row=y, column=x)
                self.map[y].append(frame)

        legend = Frame(self.master, bg=COLORS.DEFAULT_GUI_BG, width=self.world.width * self.SIZE)
        Label(legend, text="HUMAN", bg=COLORS.HUMAN_COLOR)\
            .grid(row=0, column=0, padx=10, pady=5)
        Label(legend, text="ANTELOPE", bg=COLORS.ANTELOPE_COLOR) \
            .grid(row=1, column=0, padx=10, pady=5)
        Label(legend, text="CYBER SHEEP", bg=COLORS.CYBER_SHEEP_COLOR) \
            .grid(row=2, column=0, padx=10, pady=5)
        Label(legend, text="FOX", bg=COLORS.FOX_COLOR) \
            .grid(row=3, column=0, padx=10, pady=5)
        Label(legend, text="SHEEP", bg=COLORS.SHEEP_COLOR) \
            .grid(row=4, column=0, padx=10, pady=5)
        Label(legend, text="TURTLE", bg=COLORS.TURTLE_COLOR) \
            .grid(row=5, column=0, padx=10, pady=5)
        Label(legend, text="WOLF", bg=COLORS.WOLF_COLOR) \
            .grid(row=6, column=0, padx=10, pady=5)

        Label(legend, text="HUMAN SPECIAL", bg=COLORS.HUMAN_COLOR_SPECIAL) \
            .grid(row=0, column=1, padx=10, pady=5)
        Label(legend, text="DANDELION", bg=COLORS.DANDELION_COLOR) \
            .grid(row=1, column=1, padx=10, pady=5)
        Label(legend, text="GRASS", bg=COLORS.GRASS_COLOR) \
            .grid(row=2, column=1, padx=10, pady=5)
        Label(legend, text="GUARANA", bg=COLORS.GUARANA_COLOR) \
            .grid(row=3, column=1, padx=10, pady=5)
        Label(legend, text="PINE BORSCHT", bg=COLORS.PINE_BORSCHT_COLOR) \
            .grid(row=4, column=1, padx=10, pady=5)
        Label(legend, text="WOLF BERRIES", bg=COLORS.WOLF_BERRIES_COLOR) \
            .grid(row=5, column=1, padx=10, pady=5)

        legend.pack()

    def clear_map(self):
        for y in range(self.world.height):
            for x in range(self.world.height):
                self.map[y][x]['bg'] = COLORS.DEFAULT_TILE_COLOR

    def draw_world(self):
        self.clear_map()
        for organism in self.world.organisms:
            self.map[organism.y][organism.x]['bg'] = organism.color

    def left(self, event):
        self.world.move_player(CONSTANTS.LEFT)
        self.world.do_round()
        self.draw_world()

    def right(self, event):
        self.world.move_player(CONSTANTS.RIGHT)
        self.world.do_round()
        self.draw_world()

    def up(self, event):
        self.world.move_player(CONSTANTS.UP)
        self.world.do_round()
        self.draw_world()

    def down(self, event):
        self.world.move_player(CONSTANTS.DOWN)
        self.world.do_round()
        self.draw_world()

    def special_ability(self, event):
        self.world.special_ability()

    def quit(self, event):
        self.master.destroy()

    def save_to_file(self, event):
        self.world.save_state_to_file()

    def load_from_file(self, event):
        self.world.load_state_from_file()
        self.draw_world()

    def init_key_bindings(self):
        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)
        self.master.bind("<x>", self.special_ability)
        self.master.bind("<s>", self.save_to_file)
        self.master.bind("<l>", self.load_from_file)
        self.master.bind("<Escape>", self.quit)
