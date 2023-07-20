import pygame
from random import randint

class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, 20, 20)

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)

    def move(self, HEIGHT):
        self.y += self.speed

        if self.y > HEIGHT:
            self.y = 0
            self.x = randint(10, 750)

        #Updates position when x or y changes
        self.rect.center = (self.x, self.y)

    def update(self, screen, color, HEIGHT):
        self.move(HEIGHT)
        self.draw(screen, color)

