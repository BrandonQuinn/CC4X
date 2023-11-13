from area import area

# Countries are made of areas which belong to that country
# Each player players as 1 country
class country():
	def __init__(self, name):
		self.name = ""
		self.controlled_areas = []
		self.name = name
		self.configure_defaults()

	def update(self, clock, properties):
		for area in self.controlled_areas:
			area.update(clock, properties)

	def draw(self, screen):
		for area in self.controlled_areas:
			area.draw(screen)

	# Configure some default
	def configure_defaults(self):
		if self.name == "Kershkustan":
			kraun_area = area()
			kraun_area.add_point([0,0])
			kraun_area.add_point([200,-20])
			kraun_area.add_point([150,90])
			kraun_area.add_point([-50,100])

			kesch_area = area()
			kesch_area.add_point([-50,100])
			kesch_area.add_point([150,90])
			kesch_area.add_point([30,200])
			
			#aktobe_area = area()

			self.controlled_areas.append(kraun_area)
			self.controlled_areas.append(kesch_area)
			#self.controlled_areas.append(aktobe_area)
			
		if self.name == "Dunmay":
			pass
	