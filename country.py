from area import area

# Countries are made of areas which belong to that country
# Each player players as 1 country
class country():
	def __init__(self, name):
		self.name = ""
		self.controlled_areas = []
		self.name = name
		self.configure_defaults()
		self.country_colour = (0, 0, 0)

	def update(self, clock, properties):
		for area in self.controlled_areas:
			area.update(clock, properties)

	def draw(self, screen):
		for area in self.controlled_areas:
			area.draw(screen)

	# Configure some default
	def configure_defaults(self):
		if self.name == "Kershkustan":
			self.country_colour = (140, 100, 140)

			kraun_area = area()
			kraun_area.add_point([0,0])
			kraun_area.add_point([200,-20])
			kraun_area.add_point([150,90])
			kraun_area.add_point([-50,100])
			kraun_area.set_colour(self.country_colour)

			kesch_area = area()
			kesch_area.add_point([-50,100])
			kesch_area.add_point([150,90])
			kesch_area.add_point([30,200])
			kesch_area.set_colour(self.country_colour)
			
			aktobe_area = area()
			aktobe_area.add_point([150,200])
			aktobe_area.add_point([200,140])
			aktobe_area.add_point([150,90])
			aktobe_area.add_point([30,200])
			aktobe_area.set_colour(self.country_colour)

			self.controlled_areas.append(kraun_area)
			self.controlled_areas.append(kesch_area)
			self.controlled_areas.append(aktobe_area)
			
		if self.name == "Dunmark":
			self.country_colour = (100, 100, 140)

			trusk_area = area()
			trusk_area.add_point([200,-20])
			trusk_area.add_point([450,-60])
			trusk_area.add_point([430,120])
			trusk_area.add_point([150,90])
			trusk_area.set_city_location([250, 30]);
			trusk_area.set_colour(self.country_colour)

			kriln_area = area()
			kriln_area.add_point([430,120])
			kriln_area.add_point([400,170])
			kriln_area.add_point([200,140])
			kriln_area.add_point([150,90])
			kriln_area.set_colour(self.country_colour)

			preck_area = area()
			preck_area.add_point([400,170])
			preck_area.add_point([250,270])
			preck_area.add_point([150,200])
			preck_area.add_point([200,140])
			preck_area.set_colour(self.country_colour)

			self.controlled_areas.append(trusk_area)
			self.controlled_areas.append(kriln_area)
			self.controlled_areas.append(preck_area)
	