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


class Square:
    def __init__(self, xPos, yPos, size, color, mass, retention, ySpeed, xSpeed, id):
        self.xPos = xPos
        self.yPos = yPos
        self.size = size  # changed from radius to size
        self.color = color
        self.mass = mass
        self.retention = retention
        self.ySpeed = ySpeed
        self.xSpeed = xSpeed
        self.id = id
        self.rect = None  # changed from circle to rect
    
    def draw(self, screen):
        self.rect = pygame.draw.rect(screen, self.color, (self.xPos, self.yPos, self.size, self.size))

    def check_gravity(self, HEIGHT, wall_thickness, gravity, bounceStop):
        if self.yPos + self.size > HEIGHT - wall_thickness:
            if self.ySpeed > bounceStop:
                self.ySpeed = self.ySpeed * -1 * self.retention
                self.yPos = HEIGHT - wall_thickness - self.size  # set position to just above the ground
            else:
                if abs(self.ySpeed) <= bounceStop:
                    self.ySpeed = 0
        else:
            self.ySpeed += gravity

        return self.ySpeed


    def updatePos(self, HEIGHT, wall_thickness):
        self.yPos += self.ySpeed
        # Check if the square is below the ground after the update
        if self.yPos + self.size > HEIGHT - wall_thickness:
            self.yPos = HEIGHT - wall_thickness - self.size

        self.xPos += self.xSpeed

