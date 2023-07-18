# Example file showing a basic pygame "game loop"
import pygame
import sys

# pygame setup
pygame.init()

WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 80
BALL_SIZE = 15
PADDLE_SPEED = 0
BALL_SPEED  = 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
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

score1 = 0
score2 = 0

smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('quit' , True , WHITE)

running = True



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        if event.type == pygame.KEYDOWN:
            PADDLE_SPEED = 2
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

    ball.move_ip(ball_speed)

    if ball.top < 0 or ball.bottom > HEIGHT:
        ball_speed[1] *=- 1
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] *=- 1

    if ball.left < 0:
        ball.center = (WIDTH/2, HEIGHT/2)
        ball_speed[0] *=- 1
    if ball.right > WIDTH:
        ball.center = (WIDTH/2, HEIGHT/2)
        ball_speed[0] *=- 1

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.rect(screen, WHITE, ball)

    # RENDER YOUR GAME HERE


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
