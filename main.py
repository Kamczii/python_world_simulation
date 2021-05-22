import tkinter

from GUI import GUI
from World import World
from organisms.animals.Human import Human

if __name__ == '__main__':
    root = tkinter.Tk()
    world = World(30, 30, 15)
    gui = GUI(world, master=root)

