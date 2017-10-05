from tkinter import *
from PIL import Image, ImageTk

class View(object):
    root = Tk()
    canvas = Canvas(root, width = 800, height = 800)
    canvas.pack()

    def __init__(self):
        self.floor = ImageTk.PhotoImage(Image.open("./img/floor.png"))
        self.wall = ImageTk.PhotoImage(Image.open("./img/wall.png"))
        self.hero_graphic = None
        self.hero_img = None

    def draw_map(self, game_map):
        for row in range(len(game_map)):
            for column in range(len(game_map[row])):
                if game_map[row][column] == '0':
                    self.canvas.create_image(column * 72, row * 72, anchor=NW, image=self.floor)
                else:
                    self.canvas.create_image(column * 72, row * 72, anchor=NW, image=self.wall)

    def config_hero_image(self, hero):
        self.hero_img = ImageTk.PhotoImage(Image.open(hero.image["down"]))

    def draw_characters(self, hero):
        self.hero_graphic = self.canvas.create_image(hero.pos_x, hero.pos_y, anchor=NW, image=self.hero_img)

    def get_canvas_items(self):
        return self.hero_graphic

    def update_entity(self, hero, direction):
        self.hero_img = ImageTk.PhotoImage(Image.open(hero.image[direction]))
        self.canvas.itemconfigure(self.hero_graphic, image=self.hero_img)

    def move_entity(self, entity, x, y):
        if entity.move == True:
            self.canvas.move(entity.canvas_item, x, y)


    def show(self):
        self.root.mainloop()
