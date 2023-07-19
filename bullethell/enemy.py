import pygame
from random import randint

class enemy:
    def __init__(enemy, x, y, speed):
        enemy.x = x
        enemy.y = y
        enemy.speed = speed

    def draw(enemy, screen, color):
        enemies = pygame.Rect(enemy.x, enemy.y, 15, 15)
        pygame.draw.rect(screen, color, enemies)

    def move(enemy, HEIGHT):
        enemy.y += enemy.speed

        if enemy.y > HEIGHT:
            enemy.y = 0
            enemy.x = randint(10, 750)

    def update(enemy, screen, color, HEIGHT):
        enemy.draw(screen, color)
        enemy.move(HEIGHT)

