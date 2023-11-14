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
			
			aktobe_area = area()
			aktobe_area.add_point([150,200])
			aktobe_area.add_point([200,140])
			aktobe_area.add_point([150,90])
			aktobe_area.add_point([30,200])

			self.controlled_areas.append(kraun_area)
			self.controlled_areas.append(kesch_area)
			self.controlled_areas.append(aktobe_area)
			
		if self.name == "Dunmark":
			trusk_area = area()
			trusk_area.add_point([200,-20])
			trusk_area.add_point([450,-60])
			trusk_area.add_point([430,120])
			trusk_area.add_point([150,90])

			kriln_area = area()
			kriln_area.add_point([430,120])
			kriln_area.add_point([400,170])
			kriln_area.add_point([200,140])
			kriln_area.add_point([150,90])

			preck_area = area()
			preck_area.add_point([400,170])
			preck_area.add_point([250,270])
			preck_area.add_point([150,200])
			preck_area.add_point([200,140])

			self.controlled_areas.append(trusk_area)
			self.controlled_areas.append(kriln_area)
			self.controlled_areas.append(preck_area)
	