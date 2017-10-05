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
        self.view.draw_characters(self.hero)

    def game_runner(self):
        self.event_listener()

    def instantiate_characters(self):
        self.hero = Hero()

    def event_listener(self):
        pass
    #     self.view.root.bind('<KeyPress>', self.input_handling)
    #
    # def input_handling(self, event):
    #     if event.keysym == 'Up':
    #     elif event.keysym == 'Down':
    #     elif event.keysym == 'Right':
    #     elif event.keysym == 'Left':

game = Game()
