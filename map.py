from country import country

class map():
	name = ""
	countries = []

	def __init__(self, name):
		self.name = name

		# create an example country
		country_example = country("Australia")
		self.countries.append(country_example)

	def draw(self, screen):
		for country in self.countries:
			country.draw(screen)