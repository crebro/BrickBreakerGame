import pygame
from .constants import BLACK, tiles
import random


class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 2
        self.width = 100
        self.height = 30
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = random.choice(tiles)

    def draw(self, surface):
        # pygame.draw.rect(surface, BLACK, (self.x, self.y,
        #                                   self.width, self.height), 1)
        if self.health == 1:
            surface.blit(self.image[1], (self.x, self.y))
        else:
            surface.blit(self.image[0], (self.x, self.y))
