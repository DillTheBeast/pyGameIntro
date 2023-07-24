import pygame as pg

class platforms:
    def __init__(platform, x, y, width, height):
        platform.x = x
        platform.y = y
        platform.width = width
        platform.height = height
        platform.rect = pg.Rect(platform.x, platform.y, platform.width, platform.height)


    def draw(platform, screen, color):
        pg.draw.rect(screen, color, platform.rect)


    