import pygame


class SnakeTail(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.elements = []

    def add_element_to_tail(self, position):
        image = pygame.Surface((16, 16))
        image.fill((0, 0, 250))
        rect = image.get_rect()
        rect.topleft = position

        self.elements.append({"image": image, "rect": rect})
