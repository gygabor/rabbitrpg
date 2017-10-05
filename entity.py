class Entity(object):
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

class Hero(Entity):
    def __init__(self, pos_x=0, pos_y=0):
        super().__init__(pos_x, pos_y)
        self.image = {"up": "./img/hero-up.png",
                      "down": "./img/hero-down.png",
                      "right": "./img/hero-right.png",
                      "left": "./img/hero-left.png"
                      }

class Boss(Entity):
    pass

class Skeleton(Entity):
    pass
