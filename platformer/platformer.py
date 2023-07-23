import pygame as pg

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
JUMP_STRENGTH = 250
FPS = 60
player_speed = [SPEED, SPEED]
player_size = 30
player_vel = [0, 0]
player_pos = [250/2, HEIGHT - player_size]

player = pg.Rect(player_size, HEIGHT/2, player_size, player_size)
startPlatform = pg.Rect(0, HEIGHT - 50, 250, 50)
secondPlatform = pg.Rect(400, HEIGHT - 200, 250, 50)

running = True

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Platformer")
clock = pg.time.Clock()

while running:
    dt = clock.tick(FPS) / 1000  # Delta Time = Airtime

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if player.bottom >= startPlatform.top:
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
    player_vel[1] += GRAVITY * dt
    player_vel[1] = min(player_vel[1], startPlatform.top)
    player_pos[1] += player_vel[1] * dt

    if player_pos[1] >= startPlatform.top - player_size:
        player_pos[1] = startPlatform.top - player_size
        player_vel[1] = 0

    # update player rect position
    player.topleft = player_pos

    screen.fill(BLACK)

    pg.draw.rect(screen, WHITE, player)
    pg.draw.rect(screen, GREEN, startPlatform)
    pg.draw.rect(screen, GREEN, secondPlatform)

    pg.display.flip()

    clock.tick(60)  # limits FPS to 60