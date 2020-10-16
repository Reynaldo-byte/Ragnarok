import pygame

class score:



    def main(segundos):
        # inicializa Pygame
        white = (255, 255, 255)
        pygame.init()

        # fuente de letra
        font = pygame.font.Font(None, 30)

        # crea la ventana y establece sus propiedades
        pygame.display.set_caption("puntuacion")  # título
        screen = pygame.display.set_mode((300, 300))  # tamaño

        # retorna el rectángulo de la pantalla
        screen_rect = screen.get_rect()

        # convierte un texto en un objeto 'Surface'
        text_surface = font.render("tu puntaje fue: "+str(int(segundos)*2.5), True, white)
        # retorna el rectángulo del texto
        text_rect = text_surface.get_rect()

        # centra el rectángulo del texto
        text_rect.center = screen_rect.center

        # dibuja el texto
        screen.blit(text_surface, text_rect)

        # actualiza la pantalla
        pygame.display.flip()

        # bucle principal (maneja los eventos)
        while True:
            # retorna un solo evento de la cola de eventos
            event = pygame.event.wait()

            # detiene el bucle cuando el botón CERRAR de la ventana es presionado
            if event.type == pygame.QUIT:
                break

        # finaliza Pygame
        pygame.quit()

