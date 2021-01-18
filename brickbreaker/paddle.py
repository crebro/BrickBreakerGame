import pygame
from .constants import BLACK, WIDTH, PLAYERTILE

class Paddle:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.vel = 15
		self.width = 150
		self.height = 30
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

	def draw(self, surface):
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		# pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height))
		surface.blit(PLAYERTILE, (self.x, self.y))

	def move(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
			self.x += self.vel

		if keys[pygame.K_LEFT] and self.x > 0:
			self.x -= self.vel
