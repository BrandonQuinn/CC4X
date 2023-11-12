import pygame

# Contains a list of polygons, each polygon is an area that can be captured
class area():
	name = ""
	border_colour = (0, 0, 0)
	shape = [[100, 50], [50, 150], [150, 150]]

	def draw(self, screen, properties):
		self.applyOffset(properties)
		pygame.draw.polygon(screen, self.border_colour, self.shape, 2)
	
	# Shift the area by how much the game world has been offset
	def applyOffset(self, properties):
		for vector in self.shape:
			vector[0] += properties.offset[0]
			vector[1] += properties.offset[1]