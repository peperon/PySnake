import pygame


class Score(pygame.sprite.Sprite):

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 50)
        self.color = (255, 255, 255)
        self.score = 0
        self.position = position
        self.render()

    def add(self, points):
        self.score += points
        self.render()

    def reset(self):
        self.score = 0
        self.render()

    def render(self):
        text = "Score: %d" % (self.score)
        self.image = self.font.render(text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
