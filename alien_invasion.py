import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
	#Inicjalizacja gry i utworzenie obiektu ekranu.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Inwazja obcych')
	
	#Utworzenie egzemplarza przeznaczonego do przechowywania danych
	#statystycznych dotyczących gry.
	stats = GameStats(ai_settings)
	
	#Utworzenie statku kosmicznego oraz grupy obcych.
	ship = Ship(ai_settings, screen)
	aliens = Group()
	
	#Utworzenie floty obcych.
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#Utworzenie grupy przeznaczonej do przechowywania pocisków.
	bullets = Group()
	
	#Utworzenie przycisku Gra.
	play_button = Button(ai_settings, screen, 'Gra')
	pygame.display.flip()
	pygame.display.update()
	
	#Rozpoczęcie pętli głównej gry.
	while True:
		gf.check_events(ai_settings, screen, stats, play_button, ship,
		aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens,
			bullets)
			gf.update_screen(ai_settings, screen, stats, ship, aliens, 
			bullets, play_button)
		pygame.display.flip()
		pygame.display.update()

run_game()
