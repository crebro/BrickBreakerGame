import pygame
from .constants import RED, WIDTH, HEIGHT, BLACK


class Ball:
    def __init__(self, x, y, vel, radius):
        self.x = x
        self.y = y
        self.vel = vel
        self.vy = vel
        self.vx = vel
        self.radius = radius
        self.image = pygame.transform.scale(pygame.image.load(
            'assets\\Tiles\\PNG\\58-Breakout-Tiles.png'), (self.radius * 2, self.radius * 2))
        self.rect = pygame.Rect(
            self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self, surface):
        self.rect = pygame.Rect(
            self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        # pygame.draw.circle(surface, RED, (self.x, self.y), self.radius)
        surface.blit(self.image, (self.x - self.radius, self.y-self.radius))
        # pygame.draw.rect(surface, BLACK, (self.x - self.radius, self.y - self.radius, self.radius *2, self.radius *2), 1)

    def move(self, paddle, blockBricks):
        self.x += self.vx
        self.y += self.vy

        #  and self.y + self.radius - 10 > HEIGHT - paddle.height
        if self.rect.colliderect(paddle.rect) and self.y + self.radius - 10 > HEIGHT - paddle.height:
            self.vy *= -1

        # if self.y > HEIGHT - self.radius * 2:
        # 	self.vy *= -1

        elif self.x > WIDTH - self.radius * 2:
            self.vx *= -1

        elif self.x < self.radius:
            self.vx *= -1

        elif self.y < self.radius:
            self.vy *= -1

    def isOff(self):
        if self.y + self.radius > HEIGHT - self.radius:
            return True
        return False
