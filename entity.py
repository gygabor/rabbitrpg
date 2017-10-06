from random import *

class Entity(object):
    def __init__(self, pos_x, pos_y, game_map):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.game_map = game_map
        self.canvas_item = None
        self.move = False

    def move_entity(self, direction):
        if direction == 'up' and self.check_step(self.pos_x, self.pos_y - 1):
            self.pos_y -= 1
            self.move = True
        elif direction == 'down' and self.check_step(self.pos_x, self.pos_y + 1):
            self.pos_y += 1
            self.move = True
        elif direction == 'right' and self.check_step(self.pos_x + 1, self.pos_y):
            self.pos_x += 1
            self.move = True
        elif direction == 'left' and self.check_step(self.pos_x - 1, self.pos_y):
            self.pos_x -= 1
            self.move = True
        else:
            self.move = False

    def check_step(self, pos_x, pos_y):
        if pos_x < 0 or pos_x > 9:
            return False
        elif pos_y < 0 or pos_y > 9:
            return False
        elif self.game_map.game_map[pos_y][pos_x] == '0':
            return True

    def get_free_position(self, boss=None, skeletons=None):
        start_positions = []
        find_pos = False
        while find_pos == False:
            pos_x = randint(0, 9)
            pos_y = randint(0, 9)
            if self.game_map.game_map[pos_y][pos_x] == '0' and (pos_x, pos_y) != (self.pos_x, self.pos_y):
                find_pos = True
            if boss:
                if (pos_x, pos_y) == (boss.pos_x, boss.pos_y):
                    find_pos = False
            if skeletons:
                for skeleton in skeletons:
                    if (pos_x, pos_y) == (skeleton.pos_x, skeleton.pos_y):
                        find_pos = False
        start_positions.append(pos_x)
        start_positions.append(pos_y)
        return start_positions

class Hero(Entity):
    def __init__(self, pos_x, pos_y, game_map):
        super().__init__(pos_x, pos_y, game_map)
        self.image = {"up": "./img/hero-up.png",
                      "down": "./img/hero-down.png",
                      "right": "./img/hero-right.png",
                      "left": "./img/hero-left.png"
                      }

class Boss(Entity):
    def __init__(self, pos_x, pos_y, game_map):
        super().__init__(pos_x, pos_y, game_map)
        self.image = "./img/boss.png"

class Skeleton(Entity):
    def __init__(self, pos_x, pos_y, game_map):
        super().__init__(pos_x, pos_y, game_map)
        self.image = "./img/skel.png"
