from RMoves import *
class Director():
    __builder = None

    def setBuilder(self, builder):
        self.__builder= builder
    
    def getChar(self):
        charac = Character()
        charac.set_sprites(self.__builder.get_sprites())
        return charac

    
