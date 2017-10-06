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
        self.skeletons_imgs = []

    def draw_map(self, game_map):
        for row in range(len(game_map)):
            for column in range(len(game_map[row])):
                if game_map[row][column] == '0':
                    self.canvas.create_image(column * 72, row * 72, anchor=NW, image=self.floor)
                else:
                    self.canvas.create_image(column * 72, row * 72, anchor=NW, image=self.wall)

    def config_entity_image(self, hero, boss, skeleton):
        self.hero_img = ImageTk.PhotoImage(Image.open(hero.image["down"]))
        self.boss_img = ImageTk.PhotoImage(Image.open(boss.image))
        self.skel_img = ImageTk.PhotoImage(Image.open(skeleton.image))

    def draw_entities(self, hero, boss, skeletons):
        self.hero_graphic = self.canvas.create_image(hero.pos_x, hero.pos_y, anchor=NW, image=self.hero_img)
        self.boss_graphic = self.canvas.create_image(boss.pos_x * 72, boss.pos_y * 72, anchor=NW, image=self.boss_img)
        for i in range(len(skeletons)):
            i = self.canvas.create_image(skeletons[i].pos_x * 72, skeletons[i].pos_y * 72, anchor=NW, image=self.skel_img)
            self.skeletons_imgs.append(i)

    def get_canvas_items(self):
        return [self.hero_graphic, self.boss_graphic, self.skeletons_imgs]

    def update_entity(self, hero, direction):
        self.hero_img = ImageTk.PhotoImage(Image.open(hero.image[direction]))
        self.canvas.itemconfigure(self.hero_graphic, image=self.hero_img)

    def move_entity(self, entity, direction):
        offset = self.get_offset(direction)
        if entity.move == True:
            self.canvas.move(entity.canvas_item, offset[0], offset[1])

    def get_offset(self, direction):
        return {
                "down": [0, 72],
                "up": [0, -72],
                "right": [72, 0],
                "left": [-72, 0]
        }[direction]

    def show(self):
        self.root.mainloop()
