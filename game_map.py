class GameMap():
    def __init__(self):
        self.game_map = []
        self.read_map()

    def read_map(self):
        f = open('./map.txt', 'r')
        map_lines = f.readlines()
        for line in map_lines:
            line = line[:-1].split(',')
            self.game_map.append(line)
        f.close()
