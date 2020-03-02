import pygame
import random

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320
BALL_SIZE = 25

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 4
        self.change_y = 4
        self.color = RED

def make_ball(color):
    ball = Ball()
    
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
    ball.color = color
    
    return ball

def main():
    pygame.init()
    
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("Click The Balls")
    
    done = False
    
    clock = pygame.time.Clock()
    
    ball_list = []
    
    count = 0
    
    ball = make_ball(RED)
    ball_list.append(ball)
    ball = make_ball(GREEN)
    ball_list.append(ball)
    ball = make_ball(BLUE)
    ball_list.append(ball)
    
        
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif pygame.mouse.get_pressed()[0]:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                for ball in ball_list:
                    if mouse_x > ball.x - 25 and mouse_x < ball.x + 25 and mouse_y > ball.y - 25 and mouse_y < ball.y + 25:
                        ball_list.remove(ball)
        if len(ball_list) == 0:
            ball = make_ball(RED)
            ball_list.append(ball)
            ball = make_ball(GREEN)
            ball_list.append(ball)
            ball = make_ball(BLUE)
            ball_list.append(ball)
        for ball in ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y
            
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1
                
            screen.fill(BLACK)
        
        for ball in ball_list:
            pygame.draw.circle(screen, ball.color, [ball.x, ball.y], BALL_SIZE)
            
        clock.tick(60)
            
        pygame.display.flip()
            
    pygame.quit()

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    