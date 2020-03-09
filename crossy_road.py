import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (50, 200, 255)

pygame.init()

size = [480, 320]  # RPi screen size
screen = pygame.display.set_mode(size)
pygame.display.set_mode(size, pygame.NOFRAME)

done = False

while not done:
    # initialization
    
    
    # draw start
    screen.fill(LIGHT_BLUE)
    
    # draw end
    pygame.display.flip()
    # initialization
    
    # draw start
    
    # draw end
    
pygame.quit()