import pygame
from pygame import gfxdraw

# Contains a list of polygons, each polygon is an area that can be captured
class area():
	def __init__(self):
		self.name = ""
		self.colour = (0, 0, 0)
		self.shape = []
		self.city_location = [0, 0]

	def draw(self, screen):
		self.draw_border(screen)
		self.draw_city(screen)
	
	def draw_city(self, screen):
		pygame.gfxdraw.filled_circle(screen, 
			self.city_location[0], 
			self.city_location[1], 
			4, (0, 0, 0))

	def draw_border(self, screen):
		pygame.gfxdraw.filled_polygon(screen, self.shape, self.colour)
		pygame.gfxdraw.aapolygon(screen, self.shape, (0, 0, 0))
	
	def update(self, clock, properties):
		self.applyOffset(clock, properties)

	# Set the list of polygons that make up the border
	def set_area(self, shape):
		self.shape = shape

	# Add a point to the border polygon list
	def add_point(self, point):
		self.shape.append(point)

	# Takes in the point [x, y] location of the city in the area,
	# it's required that an attacking player puts units here to capture the area
	def set_city_location(self, city_location):
		self.city_location = city_location

	# change the countrys colour
	def set_colour(self, colour):
		self.colour = colour

	# Shift the area by how much the game world has been offset
	def applyOffset(self, clock, properties):
		self.city_location[0] += properties.offset[0]
		self.city_location[1] += properties.offset[1]

		for vector in self.shape:
			vector[0] += properties.offset[0]
			vector[1] += properties.offset[1]