import pygame

# Contains a list of polygons, each polygon is an area that can be captured
class area():
	name = ""
	border_colour = (255, 0, 0)
	shape = (border_colour, (100, 50), (50, 150), [150, 150], True)

	def draw(self, screen):
		pygame.draw.polygon(screen, self.shape)