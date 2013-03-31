import pygame
import configparser


class Level(object):

    _TILE_WIDTH = 32
    _TILE_HEIGHT = 32

    def __init__(self, level_file="level1.map"):
        self._load_level(level_file)
        self.width = self.width_map * self._TILE_WIDTH
        self.height = self.height_map * self._TILE_HEIGHT

    def render(self):
        image = pygame.Surface((self.width, self.height))
        tile_image = pygame.Surface((self._TILE_WIDTH, self._TILE_HEIGHT))
        tile_image.fill((255, 0, 0))
        for y, row in enumerate(self.map):
            for x, el in enumerate(row):
                if self._is_wall(x, y):
                    point = (x * self._TILE_WIDTH, y * self._TILE_HEIGHT)
                    image.blit(tile_image, point)
        return image

    def collide(self, position):
        x_map = position[0] // self._TILE_WIDTH
        y_map = position[1] // self._TILE_HEIGHT
        return self._is_wall(x_map, y_map)

    def _load_level(self, level_file):
        self.map = []        

        parser = configparser.ConfigParser()
        parser.read(level_file)
        self.map = parser.get("level", "map").split("\n")

        self.width_map = len(self.map[0])
        self.height_map = len(self.map)

    def _is_wall(self, x, y):
        if self.map[y][x] == "w":
            return True
        else:
            return False
