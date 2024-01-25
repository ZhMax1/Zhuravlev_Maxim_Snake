import pygame
import random


class Food:
    def __init__(self, map_size, snake, food_type):
        self.pos = None
        self.spawn(map_size, snake)
        self.type = food_type

    def spawn(self, map_size, snake):
        self.pos = [random.randint(0, map_size - 1), random.randint(0, map_size - 1)]
        if self.pos in snake:
            self.spawn(map_size, snake)
        self.type = random.randint(0, 5)

    def display(self, app, element_size, scale):
        if self.type == 0:
            image = pygame.image.load('data/images/food1.png')
        else:
            image = pygame.image.load('data/images/food2.png')

        scaled_image = pygame.transform.scale(image, (scale, scale))
        app.blit(scaled_image, (self.pos[0] * element_size + 1, self.pos[1] * element_size + 1))
