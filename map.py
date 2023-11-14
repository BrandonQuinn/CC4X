from country import country

class map():
	def __init__(self, name):
		self.name = name
		self.countries = []
		self.configure_defaults()

	def update(self, clock, properties):
		for country in self.countries:
			country.update(clock, properties)

	def draw(self, screen):
		for country in self.countries:
			country.draw(screen)
	
	# create default countries
	def configure_defaults(self):
		country_kershkustan = country("Kershkustan")
		country_dunmay = country("Dunmark")

		self.countries.append(country_kershkustan)
		self.countries.append(country_dunmay)