
import pygame as pg
import platforms

pg.init()
pg.font.init()
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
color_light = (170,170,170)
color_dark = (100,100,100)
SPEED = 0
GRAVITY = 450
JUMP_STRENGTH = 350
FPS = 60
player_speed = [SPEED, SPEED]
player_size = 30
player_vel = [0, 0]
player_pos = [250/2, HEIGHT - player_size]
platformList = []
on_ground = False  # New variable to check if player is on a platform

player = pg.Rect(player_size, 0, player_size, player_size)
startPlatform = platforms.platforms(0, HEIGHT - 50, 250, 50)
secondPlatform = platforms.platforms(400, HEIGHT - 150, 150, 50)
platformList.append(startPlatform)
platformList.append(secondPlatform)

running = True

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Platformer")
clock = pg.time.Clock()

while running:
    dt = clock.tick(FPS) / 1000  # Delta Time = Airtime
    prev_player_pos = list(player_pos)
    on_ground = False  # Assume the player is not on a platform at the start of each loop

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if on_ground:
                    player_vel[1] = -JUMP_STRENGTH
            elif event.key == pg.K_a:
                player_speed[0] = -3
            elif event.key == pg.K_d:
                player_speed[0] = 3
        elif event.type == pg.KEYUP:
            if event.key in (pg.K_SPACE, pg.K_s):
                player_speed[1] = 0
            if event.key in (pg.K_a, pg.K_d):
                player_speed[0] = 0

    # update player position based on speed
    player_pos[0] += player_speed[0]
    player_pos[1] += player_speed[1]

    # gravity and jumping
    if not on_ground:
        player_vel[1] += GRAVITY * dt
    for i in range(len(platformList)):
        player_pos[1] += player_vel[1] * dt
        test_player = pg.Rect(player_pos[0], player_pos[1] + player_vel[1] * dt, player_size, player_size)

        # If the player is intersecting with the platform:
        if test_player.colliderect(platformList[i].rect):
            # If the previous position was above the platform:
            if prev_player_pos[1] + player_size <= platformList[i].rect.top:
                # Set the player's position to the top of the platform and stop the downward velocity:
                player_pos[1] = platformList[i].rect.top - player_size
                player_vel[1] = 0
                on_ground = True  # Player is on a platform


        if on_ground:
            print('Test')

    # update player rect position
    player.topleft = player_pos

    screen.fill(BLACK)

    pg.draw.rect(screen, WHITE, player)
    startPlatform.draw(screen, GREEN)
    secondPlatform.draw(screen, GREEN)

    pg.display.flip()
