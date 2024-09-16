import pygame
import random

pygame.init()

hit = False
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
screenColor = (102, 178, 255)

# Scale shark and fish images to smaller sizes that fit the screen
sharkImage = pygame.image.load('Drawing.png')
sharkImage = pygame.transform.scale(sharkImage, (400, 300))  # Adjusted size to fit

sharkRect = sharkImage.get_rect()

fishImage = pygame.image.load('Goldfish.png')
fishImage = pygame.transform.scale(fishImage, (200, 100))  # Adjusted size to fit

fishRect = fishImage.get_rect()

# Randomly position the fish within visible screen boundaries
fishRect.x = random.randint(0, screen.get_width() - fishRect.width)
fishRect.y = random.randint(0, screen.get_height() - fishRect.height)

# Print out fish position and dimensions for debugging
print('Fish Rect Position - x:', fishRect.x, 'y:', fishRect.y)

sharkSpeed = [0, 0]

while True:
    screen.fill(screenColor)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                sharkSpeed[1] = -5
            if event.key == pygame.K_s:
                sharkSpeed[1] = 5
            if event.key == pygame.K_a:
                sharkSpeed[0] = -5
            if event.key == pygame.K_d:
                sharkSpeed[0] = 5

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                sharkSpeed[1] = 0
            if event.key in (pygame.K_a, pygame.K_d):
                sharkSpeed[0] = 0

    sharkRect.move_ip(sharkSpeed)

    # Boundary checks for the shark
    if sharkRect.top < 0:
        sharkRect.y = 0
    if sharkRect.bottom > screen.get_height():
        sharkRect.y = screen.get_height() - sharkRect.height
    if sharkRect.left < 0:
        sharkRect.x = 0
    if sharkRect.right > screen.get_width():
        sharkRect.x = screen.get_width() - sharkRect.width

    # Check collision between shark and fish
    if sharkRect.colliderect(fishRect) and not hit:
        hit = True

    # Draw shark and fish
    screen.blit(sharkImage, sharkRect)

    if not hit:
        screen.blit(fishImage, fishRect)

    pygame.display.flip()
    clock.tick(60)
