from tkinter import *
from PIL import Image, ImageTk

class View(object):
    root = Tk()
    canvas = Canvas(root, width = 800, height = 800)
    canvas.pack()

    def __init__(self):
        self.floor = PhotoImage(file="./img/floor.png")
        self.wall = PhotoImage(file="./img/wall.png")
        self.hero_graphic = None
        self.hero_img = None

    def draw_map(self, game_map):
        for row in range(len(game_map)):
            for column in range(len(game_map[row])):
                if game_map[row][column] == '0':
                    self.canvas.create_image(column * 72, row * 72, anchor=NW, image=self.floor)
                else:
                    self.canvas.create_image(column * 72, row * 72, anchor=NW, image=self.wall)

    def config_hero_image(self, hero, direction):
        self.hero_img = PhotoImage(file=hero.image[direction])

    def draw_characters(self, hero, direction):
        self.config_hero_image(hero, direction)
        self.hero_graphic = self.canvas.create_image(hero.pos_x, hero.pos_y, anchor=NW, image=self.hero_img)

    def update_entity(self):
        self.canvas.itemconfigure(self.hero_graphic, image=img)

    def move_entity(self, entity, direction=""):
        if direction != "":
            self.config_hero_image(entity, direction)
            self.update_entity(entity.image[direction])

    def show(self):
        self.root.mainloop()
