#Screen = red
# U = black square avoiding white squares

import pygame
import sys
import os
from enemies import Enemy 
from random import randint

pygame.init()

WIDTH, HEIGHT = 800,600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220, 20, 60)
THING = (255, 255, 0)
color_light = (170,170,170)
color_dark = (100,100,100)

buttonFont = pygame.font.SysFont("Times New Roman", 35)
button = buttonFont.render('START' , True , WHITE)
buttonClick = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bullet Hell")
clock = pygame.time.Clock()

NUM_ENEMIES = 100
enemyList = []
enemyColors = []
score = 0
timeScore = 0

for i in range(NUM_ENEMIES):
    yLocation = randint(10, 750)
    enemy = Enemy(30, yLocation, 2)
    enemyList.append(enemy)
    enemyColors.append(BLACK)

player = pygame.Rect(WIDTH/2, HEIGHT/2, 10, 10)
enemy = Enemy(HEIGHT/2, 20, 2)

running = True
done = False
done1 = False
timesLooped = 0
dead = False

player_speed = [0, 0]

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
            if WIDTH/2-70 <= mouse[0] <= WIDTH/2+140 and HEIGHT - 40 <= mouse[1] <= HEIGHT+80:
                buttonClick = True

        if not dead:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player_speed[1] =- 3
                elif event.key == pygame.K_s:
                    player_speed[1] = 3
                elif event.key == pygame.K_a:
                    player_speed[0] =- 3
                elif event.key == pygame.K_d:
                    player_speed[0] = 3
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    player_speed[1] = 0
                if event.key in (pygame.K_a, pygame.K_d):
                    player_speed[0] = 0

    player.move_ip(player_speed)

    for i in range(NUM_ENEMIES):
        if player.colliderect(enemyList[i].rect):  # Modify this line
            #Player is dead
            dead = True

    screen.fill(RED)
    mouse = pygame.mouse.get_pos()
    if not buttonClick:
        if WIDTH/2-70 <= mouse[0] <= WIDTH/2+140 and HEIGHT - 40 <= mouse[1] <= HEIGHT+80:
            pygame.draw.rect(screen,color_light,[WIDTH/2 - 70,HEIGHT - 40, 140, 40])        
        else:
            pygame.draw.rect(screen,color_dark,[WIDTH/2 - 70,HEIGHT - 40, 140, 40])
    else:
        if not done1:
            pygame.display.update()
            before = pygame.time.get_ticks()
            done1 = True

    if not buttonClick:
        screen.blit(button , (WIDTH/2 - 70 + 35/2,HEIGHT - 40))
    else:
        if not done:
            pygame.display.update()
            done = True
    #Drawing player
    pygame.draw.rect(screen, WHITE, player)
    if buttonClick:
        
        for i in range(NUM_ENEMIES):
            enemyList[i].update(screen, enemyColors[i], HEIGHT)

        after = pygame.time.get_ticks() - before
        finalAfter = after/10000
        finalAfter -= timeScore
        #print(finalAfter)
        if finalAfter >= 1:
            score += 50
            timeScore += 1
            print(score)


    pygame.display.flip()

    clock.tick(60)

    if dead:
        player_speed = [0, 0]
        for i in range(NUM_ENEMIES):
            enemyList[i].restart()