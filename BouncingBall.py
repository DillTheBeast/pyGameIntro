import pygame
from Ball import Ball
from Ball import Square

pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()

#Game variables
wall_thickness = 10
gravity = 0.5
bounceStop = 0.3
ball1 = Ball(50, 50, 30, 'blue', 100, .9, 0, 0, 1)
ball2 = Ball(500, 500, 50, 'green', 300, .9, 0, 0, 2)
square1 = Square(30, 300, 30, 'blue', 100, .9, 0, 0, 1)
square2 = Square(500, 500, 50, 'green', 300, .9, 0, 0, 2)

def draw_walls():
    left = pygame.draw.line(screen, 'white', (0, 0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, 'white', (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, 'white', (0, 0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, 'white', (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]
    return wall_list



#main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('black')

    walls = draw_walls()
    ball1.draw(screen)
    ball2.draw(screen)
    ball1.updatePos()
    ball2.updatePos()
    ball1.ySpeed = ball1.check_gravity(HEIGHT, wall_thickness, gravity, bounceStop)
    ball2.ySpeed = ball2.check_gravity(HEIGHT, wall_thickness, gravity, bounceStop)
    square1.draw(screen)
    square2.draw(screen)
    square1.updatePos(HEIGHT, wall_thickness)
    square2.updatePos(HEIGHT, wall_thickness)
    square1.ySpeed = ball1.check_gravity(HEIGHT, wall_thickness, gravity, bounceStop)
    square2.ySpeed = ball2.check_gravity(HEIGHT, wall_thickness, gravity, bounceStop)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.flip()
pygame.quit()