from map import map

class gameworld():
    def __init__(self):
        self.map = map("World")

    def update(self, clock, properties):
        self.map.update(clock, properties)

    def draw(self, screen):
        self.map.draw(screen)