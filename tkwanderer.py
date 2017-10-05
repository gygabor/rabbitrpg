from entity import *
from view import *
from game_map import *
from view import *

class Game(object):
    def __init__(self):
        self.game_map = GameMap()
        self.view = View()
        self.hero = None
        self.boss = None
        self.skeleton = []
        self.start()
        self.view.show()

    def start(self):
        self.view.draw_map(self.game_map.game_map)
        self.instantiate_characters()
        self.view.config_hero_image(self.hero)
        self.view.draw_characters(self.hero)
        self.hero.canvas_item = self.view.get_canvas_items()
        self.event_listener()
        # self.game_runner()

    def game_runner(self):
        pass

    def instantiate_characters(self):
        self.hero = Hero(0, 0, self.game_map)

    def event_listener(self):
        self.view.root.bind("<KeyPress>", self.input_handling)

    def input_handling(self, event):
        if event.keysym == "Up":
            self.hero.move_entity("up")
            self.view.update_entity(self.hero, "up")
            self.view.move_entity(self.hero, 0, -72)
        elif event.keysym == "Down":
            self.hero.move_entity("down")
            self.view.update_entity(self.hero, "down")
            self.view.move_entity(self.hero, 0, 72)
        elif event.keysym == "Right":
            self.hero.move_entity("right")
            self.view.update_entity(self.hero, "right")
            self.view.move_entity(self.hero, 72, 0)
        elif event.keysym == "Left":
            self.hero.move_entity("left")
            self.view.update_entity(self.hero, "left")
            self.view.move_entity(self.hero, -72, 0)

game = Game()
