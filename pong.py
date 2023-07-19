# Example file showing a basic pygame "game loop"
import pygame
import sys
import os

# pygame setup
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 80
BALL_SIZE = 15
PADDLE_SPEED = 0
BALL_SPEED  = 0

score1 = 0
score2 = 0

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
color_light = (170,170,170)
color_dark = (100,100,100)

myFont = pygame.font.SysFont("Times New Roman", 60)
text1 = myFont.render(str(score1), False, WHITE)
text2 = myFont.render(str(score2), False, WHITE)

buttonFont = pygame.font.SysFont("Times New Roman", 35)
button = buttonFont.render('START' , True , WHITE)
buttonClick = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
#First = Left and right set
#Second = Up and Down set
#Last 2 = size
paddle1 = pygame.Rect(PADDLE_WIDTH, HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - PADDLE_WIDTH * 2, HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH/2, HEIGHT/2, BALL_SIZE, BALL_SIZE)
#0 = horizontal speed
paddle1_speed = [0, PADDLE_SPEED]
paddle2_speed = [0, PADDLE_SPEED]
ball_speed = [BALL_SPEED, BALL_SPEED]

running = True
done = False
done1 = False
right = True

#score = int(input("What do you want the score to be when the player wins?\n"))
scoreMax = 8

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
                BALL_SPEED = 3
                ball_speed[0] = 3
                ball_speed[1] = 3
                buttonClick = True
            
               
        if event.type == pygame.KEYDOWN:
            PADDLE_SPEED = 3
            if event.key == pygame.K_w:
                paddle1_speed[1] =- PADDLE_SPEED
            elif event.key == pygame.K_s:
                paddle1_speed[1] = PADDLE_SPEED
            elif event.key == pygame.K_UP:
                paddle2_speed[1] =- PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                paddle2_speed[1] = PADDLE_SPEED
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                paddle1_speed[1] = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                paddle2_speed[1] = 0

    paddle1.move_ip(paddle1_speed)
    paddle2.move_ip(paddle2_speed)

    if paddle1.top < 0:
        paddle1.top = 0
    if paddle1.bottom > HEIGHT:
        paddle1.bottom = HEIGHT
    if paddle2.top < 0:
        paddle2.top = 0
    if paddle2.bottom > HEIGHT:
        paddle2.bottom = HEIGHT

    if buttonClick:
        if right:
            # ball_speed[0] = -3
            # ball_speed[1] = -3
            ball.move_ip(ball_speed)
        else:
            # ball_speed[0] = 3
            # ball_speed[1] = 3
            ball.move_ip( ball_speed)

    if ball.top < 0 or ball.bottom > HEIGHT:
        print('Speed before:', ball_speed[0])
        ball_speed[1] *=- 1
        print('Speed after:', ball_speed[0])
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] *=- 1
        if abs(ball_speed[0]) == ball_speed[0]:
            #Positive number
            ball_speed[0] += 0.2
            ball_speed[1] += 0.2
        else:
            ball_speed[0] -= 0.2
            ball_speed[1] -= 0.2

    if ball.left < 0:
        ball.center = (WIDTH/2, HEIGHT/2)
        ball_speed[0] *=- 1
        score1 += 1
        right = not right
        text1 = myFont.render(str(score1), False, WHITE)
        BALL_SPEED = 3

    if ball.right > WIDTH:
        ball.center = (WIDTH/2, HEIGHT/2)
        ball_speed[0] *=- 1
        score2 += 1
        right = not right
        text2 = myFont.render(str(score2), False, WHITE)
        ball_speed[0] = 3
        ball_speed[1] = 3

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BLACK)
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

    screen.blit(text1, (0, 0))
    screen.blit(text2, (770, 0))
    if not buttonClick:
        screen.blit(button , (WIDTH/2 - 70 + 35/2,HEIGHT/2 - 20))
    else:
        if not done:
            pygame.display.update()
            done = True

    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.rect(screen, WHITE, ball)
    #pygame.display.updatew()
    if score1 == 8 or score2 == 8:
        quit()

    # RENDER YOUR GAME HERE


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
