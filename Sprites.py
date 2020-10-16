
from Products import *



class AbstractFactory():
    def moveLeft(self): pass
    def moveRight(self): pass
    def moveDown(self): pass
    def moveUp(self): pass
    def caida(self): pass



class GaticornioSprites(AbstractFactory):

    def moveLeft(self):
        left = leftGaticornio()
        return left.get_sprites()

    def moveRight(self):
        right = rightGaticornio()
        return right.get_sprites()

    def caida(self):
        caida= caidaGaticornio()
        return caida.get_sprites()



