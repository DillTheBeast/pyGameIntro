import pygame

class Ball:
    def __init__(self, xPos, yPos, radius, color, mass, retention, ySpeed, xSpeed, id):
        self.xPos = xPos
        self.yPos = yPos
        self.radius = radius
        self.color = color
        self.mass = mass
        self.retention = retention
        self.ySpeed = ySpeed
        self.xSpeed = xSpeed
        self.id = id
        self.circle = ' '
    

    def draw(self, screen):
        self.circle = pygame.draw.circle(screen, self.color, (self.xPos, self.yPos), self.radius)


    def check_gravity(self, HEIGHT, wall_thickness, gravity, bounceStop):
        if self.yPos < HEIGHT - self.radius - (wall_thickness/2):
            self.ySpeed += gravity
        else:  
            if self.ySpeed > bounceStop:
                self.ySpeed = self.ySpeed * -1 * self.retention
            else:
                if abs(self.ySpeed) <= bounceStop:
                    self.ySpeed = 0

        return self.ySpeed


    def updatePos(self):
        self.yPos += self.ySpeed
        self.xPos += self.xSpeed