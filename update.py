import pygame 

from renderer import renderer
from gameworld import gameworld
	
class update():
	running = True
	renderer = renderer()
	gameworld = gameworld()

	# Update the game
	def update(self):
		while self.running:
			self.handle_input()
			self.draw()
		
	# draw the game
	def draw(self):
		self.gameworld.draw(renderer.get_screen())

	# Handles all the input for the renderer
	def handle_input(self):
		for event in pygame.event.get():
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False
			
			if event.type == pygame.QUIT:
				self.running = False