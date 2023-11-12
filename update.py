import pygame 

from gameworld import gameworld

# General properties that can be passed down through each draw method of
# each object drawn in the game world
class drawing_properties():
	 # How far to move everything in the game based on mouse dragging
	offset = (0, 0)

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

	def get_bg_colour(self):
		return self.background_colour

# Controls the main functions for updating game logic
class update():
	running = True
	gameworld = gameworld()
	window = window();
	draw_props = drawing_properties()

	# Update the game
	def update(self):
		while self.running:
			self.handle_input()
			self.draw()
		
	# draw the game
	def draw(self):
		self.window.get_screen().fill(self.window.get_bg_colour())
		self.gameworld.draw(self.window.get_screen(), self.draw_props)
		pygame.display.flip()

	# Handles all the input for the renderer
	def handle_input(self):
		# Calling this resets the value preventing jumping when clicking
		# anywhere on the window
		pygame.mouse.get_rel()

		for event in pygame.event.get():
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False
			
			if event.type == pygame.QUIT:
				self.running = False

		# set the offset
		if pygame.mouse.get_pressed()[0] == True:
			self.draw_props.offset = pygame.mouse.get_rel()