import pygame
from snake_head import SnakeHead
from snake_tail import SnakeTail


class Snake:

    def __init__(self, position):
        self.position = position
        self.head = SnakeHead(position)
        self.tail = SnakeTail()
        self.tail.add_element_to_tail((position[0] - 16, position[1]))

    def render(self, surface):
        surface.blit(self.head.image, self.head.rect)
        for tail_element in self.tail.elements:
            surface.blit(tail_element["image"], tail_element["rect"])

    def update(self, direction):
        old_position = self.head.update(direction)
        if(self._collide_head()):
            return False
        self.position = self.head.rect.topleft
        for tail_element in self.tail.elements:
            temp = tail_element["rect"].topleft
            tail_element["rect"].topleft = old_position
            old_position = temp
        return True

    def collide(self, point):
        if self.head.rect.collidepoint(point):
            return True
        tail = self.tail.elements
        return any([elem for elem in tail if elem["rect"].collidepoint(point)])

    def _collide_head(self):
        point = self.head.rect.topleft
        tail = self.tail.elements
        return any([elem for elem in tail if elem["rect"].collidepoint(point)])

    def grow(self, grow_rate):
        tail_last_point = self.tail.elements[-1]["rect"].topleft
        while grow_rate:
            grow_rate -= 1
            self.tail.add_element_to_tail(tail_last_point)

    def length(self):
        return len(self.tail.elements) + 1

    def get_snake_coords(self):
        head = self.head.rect.topleft
        tail = [element["rect"].topleft for element in self.tail.elements]
        tail.append(head)
        return tail

    def load_snake_from_coord(self, coords):
        self.head = SnakeHead(coords.pop(-1))
        self.tail = SnakeTail()
        for point in coords:
            self.tail.add_element_to_tail(point)
