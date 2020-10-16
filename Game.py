import sys

from Director import *
from Moves import *
from RMoves import *
from score import *
import pygame



def Game():
    
    i=0
    width = 900
    height = 600
    colour = (227,166,162)
    empezar = True
    Gaticornio = rightGaticornio()
    auxlist = Gaticornio.get_sprites()
    

    pygame.init()                
    posX=100
    posY=320
    posTup = (posX,posY)
    screen = pygame.display.set_mode((width, height))
    segundos = 0
    pygame.display.set_caption("Puntaje: "+str(segundos))
    speed=20
    auxDirector = Director()
    auxDirector.setBuilder(GaticornioMoves())
    charac= auxDirector.getChar()
    charac.defPositions(posX,posY)
    jugando =True
    background =Background.change()

    pygame.mixer.music.load('Ragnarok.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    j=0


    while empezar:

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                score.main(segundos)
                pygame.quit()
                empezar = False
                sys.exit()
            elif i.type == pygame.constants.USEREVENT:

                pygame.mixer.music.load('Ragnarok.mp3')
                pygame.mixer.music.play()


        screen.blit(background[j],(0,0))
        charac.update()
        charac.drawCharacter(screen)
        charac.drawCaida(screen)
        pygame.display.update()
        segundos += 0.06
        pygame.display.set_caption("Puntaje: " + str(int(segundos)*2.5))
        if int(segundos)%4==0 :
            j=1
        if int(segundos)%2==1 :
            j=2

        if int(segundos)%10==0 and int(segundos)!=0:
           charac.speede()
        empezar=charac.colisiones()
        if empezar==False:
            score.main(segundos)

if __name__ == '__main__':
    Game()











        
         
        
        
        




