import pygame

# Contains a list of polygons, each polygon is an area that can be captured
class area():
	name = ""
	border_colour = (0, 0, 0)
	shape = ((100, 50), (50, 150), (150, 150))

	def draw(self, screen):
		pygame.draw.polygon(screen, self.border_colour, self.shape, 2)