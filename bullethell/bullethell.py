#Screen = red
# U = black square avoiding white squares

import pygame
import sys
import os

pygame.init()

WIDTH, HEIGHT = 800,600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220, 20, 60)
color_light = (170,170,170)
color_dark = (100,100,100)

buttonFont = pygame.font.SysFont("Times New Roman", 35)
button = buttonFont.render('START' , True , WHITE)
buttonClick = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bullet Hell")
clock = pygame.time.Clock()

player = pygame.Rect(WIDTH/2, HEIGHT/2, 15, 15)

running = True
done = False
done1 = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False


    if event.type == pygame.MOUSEBUTTONDOWN:         
            #if the mouse is clicked on the
            # button the game is terminated
            if WIDTH/2-70 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2-20 <= mouse[1] <= HEIGHT/2+40:
                quit()
                buttonClick = True

    screen.fill(RED)
    mouse = pygame.mouse.get_pos()
    if not buttonClick:
        if WIDTH/2-70 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2-20 <= mouse[1] <= HEIGHT/2+40:
            pygame.draw.rect(screen,color_light,[WIDTH/2 - 70,HEIGHT/2 - 20, 140, 40])        
        else:
            pygame.draw.rect(screen,color_dark,[WIDTH/2 - 70,HEIGHT/2 - 20, 140, 40])
    else:
        if not done1:
            pygame.display.update()
            done1 = True

    if not buttonClick:
        screen.blit(button , (WIDTH/2 - 70 + 35/2,HEIGHT/2 - 20))
    else:
        if not done:
            pygame.display.update()
            done = True
    #Drawing player
    pygame.draw.rect(screen, WHITE, player)

    pygame.display.flip()

    clock.tick(60)