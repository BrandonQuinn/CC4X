import pygame
from pygame import gfxdraw

# Contains a list of polygons, each polygon is an area that can be captured
class area():
	name = ""
	border_colour = (0, 0, 0)
	shape = []

	def draw(self, screen):
		if len(self.shape) >= 4:
			pygame.gfxdraw.aapolygon(screen, self.shape, self.border_colour)
		if len(self.shape) == 3:
			pygame.gfxdraw.aatrigon(screen, self.shape, self.border_colour)

	def update(self, clock, properties):
		self.applyOffset(clock, properties)
	
	def set_area(self, shape):
		self.shape = shape

	# Shift the area by how much the game world has been offset
	def applyOffset(self, clock, properties):
		for vector in self.shape:
			vector[0] += properties.offset[0] * (clock.get_time()/100)
			vector[1] += properties.offset[1] * (clock.get_time()/100)

	def add_point(self, point):
		self.shape.append(point)