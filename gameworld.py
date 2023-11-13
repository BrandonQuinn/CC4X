from map import map

# Contains everything in the game
class gameworld():
    def __init__(self):
        self.map = map("World")

    def update(self, clock, properties):
        self.map.update(clock, properties)

    def draw(self, screen):
        self.map.draw(screen)