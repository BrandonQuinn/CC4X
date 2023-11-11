import pygame 

from gameworld import gameworld

# Controls the configuration of the window
class window():
	window_title = "CC4X"
	window_size = (800, 400)
	background_colour = (255, 255, 255)
	screen = pygame.display.set_mode(window_size)

	def __init__(self):
		pygame.display.set_caption(self.window_title)
		self.screen.fill(self.background_colour)
		pygame.display.flip()

	def get_screen(self):
		return self.screen

# Controls the main functions for updating game logic
class update():
	running = True
	gameworld = gameworld()
	window = window();

	# Update the game
	def update(self):
		while self.running:
			self.handle_input()
			self.draw()
		
	# draw the game
	def draw(self):
		self.gameworld.draw(self.window.get_screen())
		pygame.display.flip()

	# Handles all the input for the renderer
	def handle_input(self):
		for event in pygame.event.get():
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False
			
			if event.type == pygame.QUIT:
				self.running = False