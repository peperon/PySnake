import pygame
from direction import Direction


class SnakeHead(pygame.sprite.Sprite):

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((16, 16))
        self.image.fill((0, 250, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, direction):
        old_position = self.rect.topleft
        if direction is Direction.UP:
            self.rect.top -= 16
        elif direction is Direction.DOWN:
            self.rect.top += 16
        elif direction is Direction.LEFT:
            self.rect.left -= 16
        else:
            self.rect.left += 16
        return old_position
