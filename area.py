import pygame
from pygame import gfxdraw

# Contains a list of polygons, each polygon is an area that can be captured
class area():
	def __init__(self):
		self.name = ""
		self.border_colour = (0, 0, 0)
		self.shape = []

	def draw(self, screen):
		try:
			pygame.gfxdraw.aapolygon(screen, self.shape, self.border_colour)
		except:
			pass # TODO: Catch

	def update(self, clock, properties):
		self.applyOffset(clock, properties)
	
	def set_area(self, shape):
		self.shape = shape

	# Shift the area by how much the game world has been offset
	def applyOffset(self, clock, properties):
		for vector in self.shape:
			vector[0] += properties.offset[0]
			vector[1] += properties.offset[1]

	def add_point(self, point):
		self.shape.append(point)