import pygame
import sys
import random
from pygame.locals import *
from level import Level
from snake import Snake
from food import Food
from direction import Direction
from score import Score
from save_game import SaveGame
from load_game  import LoadGame


class Game(object):

    def __init__(self, screen_height, screen_width):
        pygame.init()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.level_maps = ("./data/level1.map", "./data/level2.map", "./data/level3.map")
        self.current_level_map_index = 0
        self.pause = False
        self.won_grow_rate = 10
        height_width = (self.screen_height, self.screen_width)
        self.screen = pygame.display.set_mode(height_width)
        pygame.display.set_caption("PySnake")
        self.score = Score((0, 500))
        self.reload_game = False
        self.speed = 5

    def init_resources(self):
        self.level = Level(self.level_maps[self.current_level_map_index])
        self.snake = Snake((64, 64))
        self.move_direction = Direction.RIGHT
        self.food = None

    def start(self):
        clock = pygame.time.Clock()
        game_over = False
        won = True
        first_load = True

        while not game_over:
            clock.tick(self.speed)
            for event in pygame.event.get():
                self.event_handler(event)

            if self.reload_game:
                break

            if not self.pause:
                background = self.level.render()
                self.snake.render(background)
                if self.food == None:
                    position = self.generate_free_position()
                    self.food = Food(position, 1)

                background.blit(self.food.image, self.food.rect)
                self.screen.fill((0, 0, 0))
                self.screen.blit(background, (0, 0))
                self.screen.blit(self.score.image, self.score.rect)

                pygame.display.flip()
                if first_load:
                    first_load = False
                    self.pause = True
                    continue

                not_collide = self.snake.update(self.move_direction)
                if not not_collide or self.level.collide(self.snake.position):
                    game_over = True
                    won = False

                if self.food.rect.colliderect(self.snake.head.rect):
                    self.snake.grow(self.food.grow_rate)
                    self.score.add(100)
                    self.food = None

                if self.snake.length() == self.won_grow_rate:
                    game_over = True

        if self.reload_game:
            self.load_game()
        elif won and game_over:
            self.load_next_level()
        elif game_over:
            print("Game over")

    def event_handler(self, event):
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == KEYDOWN:
            key = pygame.key.get_pressed()
            new_direction = self.move_direction
            if key[pygame.K_LEFT]:
                new_direction = Direction.LEFT
            elif key[pygame.K_RIGHT]:
                new_direction = Direction.RIGHT
            elif key[pygame.K_UP]:
                new_direction = Direction.UP
            elif key[pygame.K_DOWN]:
                new_direction = Direction.DOWN
            elif key[pygame.K_p]:
                self.pause = not self.pause
            elif key[pygame.K_s]:
                self.pause = True
                level = self.current_level_map_index
                snake = self.snake.get_snake_coords()
                food = self.food.get_food_position()
                direction = self.move_direction
                SaveGame.save(level, snake, food, direction)
            elif key[pygame.K_l]:
                self.reload_game = True

            oposide_direction = self.opposite_direction(self.move_direction)
            if not oposide_direction == new_direction:
                self.move_direction = new_direction

    def opposite_direction(self, direction):
        if direction == Direction.UP:
            return Direction.DOWN
        elif direction == Direction.DOWN:
            return Direction.UP
        elif direction == Direction.LEFT:
            return Direction.RIGHT
        elif direction == Direction.RIGHT:
            return Direction.LEFT

    def generate_free_position(self):
        x, y = None, None

        while x is None or self.level.collide((x, y)) or self.snake.collide((x, y)):
            x = random.randrange(0, self.level.width - 32, 2)
            y = random.randrange(0, self.level.height - 32, 2)
        return (x, y)

    def load_next_level(self):
        if len(self.level_maps) - 1 == self.current_level_map_index:
            print("Game over, you win")
            return
        self.current_level_map_index += 1
        self.init_resources()
        self.start()

    def get_current_level_map(self):
        return self.level_maps[self.current_level_map_index]

    def load_game(self):
        loaded_dict = LoadGame.load()
        self.current_level_map_index = loaded_dict["level"]
        self.init_resources()
        self.snake.load_snake_from_coord(loaded_dict["snake"])
        self.food = Food(loaded_dict["food"], 1)
        self.move_direction = loaded_dict["direction"]
        self.reload_game = False
        self.start()

if __name__ == "__main__":
    game = Game(800, 600)
    game.init_resources()
    game.start()
