import pygame

class renderer:
	window_title = "CC4X"
	window_size = (1280, 720)
	background_colour = (255, 255, 255)
	screen = pygame.display.set_mode(window_size)

	def __init__(self):
		pygame.display.set_caption(self.window_title)
		self.screen.fill(self.background_colour)
		pygame.display.flip()

	def get_screen(self):
		return self.screen
