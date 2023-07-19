import pygame

class enemy:
    def __init__(enemy, x, y, speed):
        enemy.x = x
        enemy.y = y
        enemy.speed = speed

    def draw(enemy, screen, color):
        enemies = pygame.Rect(enemy.x, enemy.y, 15, 15)
        pygame.draw.rect(screen, color, enemies)

    def move(enemy, HEIGHT):
        enemy.x -= enemy.speed

        if enemy.y < 0:
            enemy.y = HEIGHT

    def update(enemy, screen, color, HEIGHT):
        enemy.draw(screen, color)
        enemy.move(HEIGHT)

