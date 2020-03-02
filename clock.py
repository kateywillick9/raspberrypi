from datetime import datetime
import pygame

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#initialize pygame
pygame.init()

#set up the screen
size = [480, 320]
screen = pygame.display.set_mode(size)
#removes the caption
pygame.display.set_mode(size, pygame.NOFRAME)

#this boolean will be used to tell when to stop the game
done = False

#game
while not done:
    for event in pygame.event.get():
        #stop the game when you press the X
        if event.type == pygame.QUIT:
            done = True
    #fresh screen
    screen.fill(BLACK)
    #get the current time
    now = datetime.now()
    time_hour = now.strftime("%H")
    time_hour_2 = int(time_hour)
    time_minute = now.strftime("%M")
    #convert from military
    if (time_hour_2 > 12):
        time_hour_2 -= 12
        time_hour = ("0" + str(time_hour_2))
        
    
    #make a string that holds the current time
    current_time = time_hour + ":" + time_minute
    
    #draw start
    font = pygame.font.SysFont('Calibri', 275, True, False)
    text = font.render(current_time, True, WHITE)
    screen.blit(text, [7, 50])
    #draw end
    
    pygame.display.flip()
    
pygame.quit()