import pygame

class enemy:
    def __init__(enemy, x, y, speed):
        enemy.x = x
        enemy.y = y
        enemy.speed = speed

    def draw(enemy, screen, color, WIDTH, HEIGHT):
        enemies = pygame.Rect(WIDTH/2, 20, 15, 15)
        pygame.draw.rect(screen, color, enemies)

    def move(enemy, WIDTH):
        enemy.x -= enemy.speed

        if enemy.x < WIDTH:
            enemy.x = 800

    def update(enemy, screen, color, WIDTH, HEIGHT):
        enemy.draw(screen, color, WIDTH, HEIGHT)
        enemy.move(WIDTH)