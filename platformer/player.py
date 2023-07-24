import pygame as pg

class players:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)


    def draw(self, screen, color):
        pg.draw.rect(screen, color, self.rect)

    def get_rect(self):
        self.rect.topleft = (self.x, self.y)