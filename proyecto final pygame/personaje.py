import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Personaje(Sprite):
	def __init__(self, cont_size):
		Sprite.__init__(self)
		self.image = pygame.image.load("img/morraquito.png")
		self.rect = self.image.get_rect()
		self.rect.left = 240
		self.rect.top = 220
		self.vel = [0,1]
		self.saltando = False
		self.t = 0		
		

	def update(self):
		
		if self.saltando == True:
			if self.t < 17:
				if self.rect.y < 0:
					self.saltando = False
				else:
					self.rect.y -= 5
				self.t += 1
			else:
				self.saltando = False
				self.t = 0
		else:
			self.rect = self.rect.move(self.vel)

	
		

