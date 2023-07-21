#Screen = red
# U = black square avoiding white squares

import pygame
import sys
import os
from enemies import Enemy 
from random import randint

pygame.init()
game = True

while game:
    running = True
    #Declaring variables
    WIDTH, HEIGHT = 800,600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (220, 20, 60)
    THING = (255, 255, 0)
    color_light = (170,170,170)
    color_dark = (100,100,100)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bullet Hell")
    clock = pygame.time.Clock()

    NUM_ENEMIES = 100
    enemyList = []
    enemyColors = []
    score = 0
    timeScore = 0
    myFont = pygame.font.SysFont("Times New Roman", 60)
    scoreShow = myFont.render(str(score), False, WHITE)
    buttonFont = pygame.font.SysFont("Times New Roman", 35)
    buttonStart = buttonFont.render('START' , True , WHITE)
    buttonQuit = buttonFont.render('Quit' , True , WHITE)
    buttonRestart = buttonFont.render('Restart' , True , WHITE)
    test = buttonFont.render('T' , True , WHITE)
    buttonClick = False
    buttonClick1 = False
    buttonClick2 = False

    #Adding all enemies to enemyList for future
    #Also generating random spot for enemies to fall
    for i in range(NUM_ENEMIES):
        yLocation = randint(10, 750)
        enemy = Enemy(30, yLocation, 2)
        enemyList.append(enemy)
        enemyColors.append(BLACK)

    player = pygame.Rect(WIDTH/2, HEIGHT/2, 10, 10)
    enemy = Enemy(HEIGHT/2, 20, 2)

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
                #if the mouse is clicked then game starts
                if WIDTH/2-70 <= mouse[0] <= WIDTH/2+140 and HEIGHT - 40 <= mouse[1] <= HEIGHT+80:
                    buttonClick = True

            if not dead:
                #Checking for input and then setting speed
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

        #Actually moving player
        player.move_ip(player_speed)

        #Checking for collisions and if so player = dead
        for i in range(NUM_ENEMIES):
            if player.colliderect(enemyList[i].rect):  # Modify this line
                #Player is dead
                dead = True

        #Filling screen and getting mouse position for start button
        screen.fill(RED)
        mouse = pygame.mouse.get_pos()
        if not buttonClick:
            #Making it so if you hover on start button then color changes
            if WIDTH/2-70 <= mouse[0] <= WIDTH/2+140 and HEIGHT - 40 <= mouse[1] <= HEIGHT+80:
                pygame.draw.rect(screen,color_light,[WIDTH/2 - 70,HEIGHT - 40, 140, 40])        
            else:
                pygame.draw.rect(screen,color_dark,[WIDTH/2 - 70,HEIGHT - 40, 140, 40])
        else:
            if not done1:
                #Updating and finding how long until game is started
                pygame.display.update()
                before = pygame.time.get_ticks()
                done1 = True

        if not buttonClick:
            #Updating start button if not clicked yet
            screen.blit(buttonStart , (WIDTH/2 - 70 + 35/2,HEIGHT - 40))
        else:
            if not done:
                pygame.display.update()
                done = True
        #Drawing player
        pygame.draw.rect(screen, WHITE, player)
        if buttonClick: 
            #If the button is clicked then game starts     
            for i in range(NUM_ENEMIES):
                enemyList[i].update(screen, enemyColors[i], HEIGHT)

            if not dead:
                #Finding time not including before start was clicked
                after = pygame.time.get_ticks() - before
                finalAfter = after/10000
                finalAfter -= timeScore
                #print(finalAfter)
                if finalAfter >= 1:
                    score += 50
                    timeScore += 1
                    print(score)
                    scoreShow = myFont.render(str(score), False, WHITE)

        screen.blit(scoreShow, (0, 0))
                

        if dead:
            #If player is dead then everything stops score is showed and buttons are showed
            player_speed = [0, 0]
            for i in range(NUM_ENEMIES):
                enemyList[i].restart()
            deadText = myFont.render("You died. Your score was " + str(score), False, WHITE)
            buttonQuitText = buttonFont.render("Quit", False, WHITE)
            buttonRestartText = buttonFont.render("Restart", False, WHITE)
            if event.type == pygame.MOUSEBUTTONDOWN:         
                #if the mouse is clicked on the
                # button the game is terminated

                #Checking for quit button or restart button clicked
                if WIDTH/2 + 250 <= mouse[0] <= WIDTH/2 + 390 and HEIGHT - 40 <= mouse[1] <= HEIGHT+40:
                    quit()

                elif WIDTH/2 - 300 <= mouse[0] <= WIDTH/2-160 and HEIGHT - 40 <= mouse[1] <= HEIGHT+40:
                    running = False

            #Checking for quiot button or restart button hovered on
            if WIDTH/2 + 250 <= mouse[0] <= WIDTH/2 + 390 and HEIGHT - 40 <= mouse[1] <= HEIGHT+40:
                pygame.draw.rect(screen,color_light,[WIDTH/2 + 300 - 50,HEIGHT - 40, 140, 40])        
            else:
                pygame.draw.rect(screen,color_dark,[WIDTH/2 + 300 - 50,HEIGHT - 40, 140, 40])


            if WIDTH/2 - 300 <= mouse[0] <= WIDTH/2 - 160 and HEIGHT - 40 <= mouse[1] <= HEIGHT+40:
                pygame.draw.rect(screen,color_light,[WIDTH/2 - 300,HEIGHT - 40, 140, 40])        
            else:
                pygame.draw.rect(screen,color_dark,[WIDTH/2 - 300,HEIGHT - 40, 140, 40])


            screen.blit(deadText, (90, 300))
            screen.blit(buttonQuitText, (WIDTH/2 + 300 - 35/2,HEIGHT - 40))
            screen.blit(buttonRestartText, (WIDTH/2 - 300 + 35/2,HEIGHT - 40))


        pygame.display.flip()

        clock.tick(60)