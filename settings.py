class Settings():
	"""Klasa przeznaczona do przechowywania wszystkich ustawień gry."""
	
	def __init__(self):
		"""Inicjalizacja danych statystycznych gry."""
		#Ustawienia ekranu.
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255, 255, 255)
		
		#Ustawienia dotyczące statku.
		self.ship_limit = 2
		
		#Ustawienia dotyczące pocisku.
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		
		#Ustawienia dotyczące obcego
		self.fleet_drop_speed = 10
		
		#Łatwa zmiana szybklości gry
		self.speedup_scale = 1.1
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		"""Inicjalizacja ustawień, które ulegają zmianie."""
		self.ship_speed_factor = 1
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 0.5
		
		#Wartość fleet_direction wynosząca 1 oznacza prawo, natomiast
		#-1 oznacza lewo.
		self.fleet_direction = 1
		
	def increase_speed(self):
		"""Zmiana ustawień dotyczących szybkości."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
