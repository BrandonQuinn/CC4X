from area import area

class country():
	name = ""
	controlled_areas = []
	area_example = area()

	def __init__(self, name):
		self.name = name
		self.controlled_areas.append(self.area_example)

	def draw(self, screen, properties):
		for area in  self.controlled_areas:
			area.draw(screen, properties)
	