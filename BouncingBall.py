import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()

#Game variables
wall_thickness = 10

def draw_walls():
    left = pygame.draw.line(screen, 'white', (0, 0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, 'white', (0, 0), (0, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, 'white', (0, 0), (0, HEIGHT), wall_thickness)
    bottom = pygame.draw.line(screen, 'white', (0, 0), (0, HEIGHT), wall_thickness)

#main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('black')

    walls = draw_walls()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.flip()
pygame.quit()