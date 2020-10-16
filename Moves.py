from Sprites import*


# Nuestro constructor
class Moves():
    def get_sprites(self): pass
    def set_sprites(self): pass


# Nuestro constructor concreto
class GaticornioMoves():
    def __init__(self):
        self.factory = GaticornioSprites()

    def get_sprites(self):
        return [self.factory.moveLeft(),
                self.factory.moveRight(),
                self.factory.caida()]


