from map import map

class gameworld():
    map = map("World")

    def init(self):
        pass

    def update(self, clock, properties):
        self.map.update(clock, properties)

    def draw(self, screen):
        self.map.draw(screen)