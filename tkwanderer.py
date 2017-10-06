from entity import *
from view import *
from game_map import *
from view import *
from random import *

class Game(object):
    def __init__(self):
        self.game_map = GameMap()
        self.view = View()
        self.hero = None
        self.boss = None
        self.skeletons = []
        self.level = 1
        self.start()
        self.view.show()

    def start(self):
        self.view.draw_map(self.game_map.game_map)
        self.instantiate_characters()
        self.view.config_entity_image(self.hero, self.boss, self.skeletons[0])
        self.view.draw_entities(self.hero, self.boss, self.skeletons)
        self.set_canvas_items()
        self.event_listener()

    def instantiate_characters(self):
        self.hero = Hero(0, 0, self.game_map)
        self.boss_start_position = self.hero.get_free_position()
        self.boss = Boss(self.boss_start_position[0], self.boss_start_position[1], self.game_map)
        skeleton_number = self.skeleton_number()
        for i in range(skeleton_number):
            skel_start_position = self.hero.get_free_position(self.boss, self.skeletons)
            skeleton = Skeleton(skel_start_position[0], skel_start_position[1], self.game_map)
            self.skeletons.append(skeleton)
            self.skeletons[0].key = True

    def skeleton_number(self):
        chance = randint(1, 10)
        if chance <= 5:
            return self.level
        elif chance > 5 and chance < 9:
            return self.level + 1
        else:
            return self.level + 2

    def set_canvas_items(self):
        self.canvas_items = self.view.get_canvas_items()
        self.hero.canvas_item = self.canvas_items[0]
        self.boss.canvas_item = self.canvas_items[1]
        for i in range(len(self.canvas_items[2])):
            self.skeletons[i].canvas_item = self.canvas_items[2][i]

    def event_listener(self):
        self.view.root.bind("<KeyPress>", self.input_handling)

    def input_handling(self, event):
        if event.keysym == "Up":
            self.hero.move_entity("up")
            self.view.update_entity(self.hero, "up")
            self.view.move_entity(self.hero, "up")
        elif event.keysym == "Down":
            self.hero.move_entity("down")
            self.view.update_entity(self.hero, "down")
            self.view.move_entity(self.hero, "down")
        elif event.keysym == "Right":
            self.hero.move_entity("right")
            self.view.update_entity(self.hero, "right")
            self.view.move_entity(self.hero, "right")
        elif event.keysym == "Left":
            self.hero.move_entity("left")
            self.view.update_entity(self.hero, "left")
            self.view.move_entity(self.hero, "left")
        self.move_monsters()

    def move_monsters(self):
        direction = choice(["up", "down", "right", "left"])
        self.boss.move_entity(direction)
        self.view.move_entity(self.boss, direction)
        for skeleton in self.skeletons:
            direction = choice(["up", "down", "right", "left"])
            skeleton.move_entity(direction)
            self.view.move_entity(skeleton, direction)

game = Game()
