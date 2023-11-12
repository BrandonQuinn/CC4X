from map import map

class gameworld():
    map = map("World")

    def init(self):
        pass

    def update(self):
        pass

    def draw(self, screen, properties):
        self.map.draw(screen, properties)