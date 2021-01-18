import pygame
pygame.font.init()

WIDTH, HEIGHT = 700, 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

BLACK = (0, 0, 0)

# Frames Per Seconds
FPS = 60

CLOCK = pygame.time.Clock()

bricks = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],


]

font = pygame.font.SysFont('comicans', 40)

tiles = [
    (pygame.transform.scale(pygame.image.load(
        'assets\\Tiles\\PNG\\01-Breakout-Tiles.png'), (100, 30)), pygame.transform.scale(pygame.image.load(
            'assets\\Tiles\\PNG\\02-Breakout-Tiles.png'), (100, 30))),
    (pygame.transform.scale(pygame.image.load(
        'assets\\Tiles\\PNG\\03-Breakout-Tiles.png'), (100, 30)), pygame.transform.scale(pygame.image.load(
            'assets\\Tiles\\PNG\\04-Breakout-Tiles.png'), (100, 30))),
    (pygame.transform.scale(pygame.image.load(
        'assets\\Tiles\\PNG\\05-Breakout-Tiles.png'), (100, 30)), pygame.transform.scale(pygame.image.load(
            'assets\\Tiles\\PNG\\06-Breakout-Tiles.png'), (100, 30))),
]


# DESTROYTILE = pygame.transform.scale(pygame.image.load(
#     'assets\\Tiles\\PNG\\02-Breakout-Tiles.png'), (100, 30))
# BLUETILE = pygame.transform.scale(pygame.image.load(
#     'assets\\Tiles\\PNG\\01-Breakout-Tiles.png'), (100, 30))
PLAYERTILE = pygame.transform.scale(pygame.image.load(
    'assets\\Tiles\\PNG\\48-Breakout-Tiles.png'), (150, 30))
HEARTFILE = pygame.transform.scale(pygame.image.load(
    'assets\\Tiles\\PNG\\60-Breakout-Tiles.png'), (40, 40))
