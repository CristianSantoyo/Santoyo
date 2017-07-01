import pygame
from pygame.sprite import Sprite
from pygame.locals import *
from random import randint

class Obstaculo(Sprite):
	def __init__(self, cont_size, x1, t1):
		Sprite.__init__(self)	
		self.tipo = t1
		if self.tipo == 1:
			self.image = pygame.image.load("img/obstaculo.png")
			self.rect = self.image.get_rect()
			self.rect.left = x1
			self.rect.top = 0
		elif self.tipo == 2:
			self.image = pygame.image.load("img/banshee.png")
			self.rect = self.image.get_rect()
			self.rect.left = x1
			self.rect.top = randint(0, 360) + 75
		elif self.tipo == 3:
			self.image = pygame.image.load("img/obstaculo2.png")
			self.rect = self.image.get_rect()
			self.rect.left = x1
			self.rect.top = 0
		elif self.tipo == 4:
			self.image = pygame.image.load("img/banshee2.png")
			self.rect = self.image.get_rect()
			self.rect.left = x1
			self.rect.top = randint(0, 360) + 75
		elif self.tipo == 5:
			self.image = pygame.image.load("img/obstaculo3.png")
			self.rect = self.image.get_rect()
			self.rect.left = x1
			self.rect.top = 0	



	def cambiar(self, x1, t1):		
		self.tipo = t1
		if self.tipo == 1:
			self.image = pygame.image.load("img/obstaculo.png")
			self.rect = self.image.get_rect()
			self.rect = self.image.get_rect()
			self.rect.left = x1
			self.rect.top = 0
		elif self.tipo == 2:
			self.image = pygame.image.load("img/banshee.png")
			self.rect = self.image.get_rect()
			self.rect.left = x1
			self.rect.top = randint(0, 360) + 75
		elif self.tipo == 3:
			self.image = pygame.image.load("img/obstaculo2.png")
			self.rect = self.image.get_rect()
			self.rect.left = x1
			self.rect.top = 0
		elif self.tipo == 4:
			self.image = pygame.image.load("img/banshee2.png")
			self.rect = self.image.get_rect()
			self.rect.left = x1
			self.rect.top = randint(0, 360) + 75
		elif self.tipo == 5:
			self.image = pygame.image.load("img/obstaculo3.png")
			self.rect = self.image.get_rect()
			self.rect.left = x1
			self.rect.top = 0
		

