import pygame
#import random
#import time

#---------------colors---------------
#BLACK = (0, 0, 0)
#WHITE = (255, 255, 255)
#RED = (255, 0, 0)
#GREEN = (0, 255, 0)
#BLUE = (0, 0, 255)
#CYAN = (0, 255, 255)
#YELLOW = (255, 255, 0)
#PURPLE = (255, 0, 255)

#---------------set up the screen---------------
size = [480, 320] #RPi screen size
screen = pygame.display.set_mode(size)
#pygame.display.set_mode(size, pygame.NOFRAME)
pygame.display.set_caption("caption")

#---------------classes and functions go here---------------

#---------------main function---------------
def main():
    #initialize pygame
    pygame.init()
    
    #initialize the clock
    clock = pygame.time.Clock()
    
    screen.fill(color)
    
    done = False
    
    while not done:
        #if caption is being used, so will this
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    
    clock.tick(60)
    pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()