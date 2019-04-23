import pygame

class Human():

	def __init__(self, screen):
		"""Inicjalizacja statku kosmicznego i jego położenie
		początkowe."""
		self.screen = screen
		
		#Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta.
		self.image = pygame.image.load('images/human.jpg')
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#Każdy nowy statek kosmiczny pojawia się na dole ekranu.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.centery
		
	def blitme(self):
		"""Wyświetlenie statku kosmicznego w jego aktualnym położeniu"""
		self.screen.blit(self.image, self.rect)
