import pygame
from level import Level
from snake import Snake


class Food(pygame.sprite.Sprite):

    def __init__(self, position, grow_rate):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.grow_rate = grow_rate

    def get_food_position(self):
        return self.rect.topleft

    def set_food_position(self, position):
        self.rect.topleft = position
