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
JUMP_STRENGTH = 300
FPS = 60
player_speed = [SPEED, SPEED]
player_size = 30
player_vel = [0, 0]
player_pos = [250/2, HEIGHT - player_size]
platformList = []

player = pg.Rect(player_size, 0, player_size, player_size)
startPlatform = platforms.platforms(0, HEIGHT - 50, 250, 50)
secondPlatform = platforms.platforms(400, HEIGHT - 300, 150, 50)
endPlatform = platforms.platforms(600, HEIGHT - 550, 100, 50)
platformList.append(startPlatform)
platformList.append(secondPlatform)
platformList.append(endPlatform)

running = True
jump = False

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Platformer")
clock = pg.time.Clock()

def is_within_range(rect1, rect2):
    # Calculate the distance between the y-coordinates of the two rectangles
    y_distance = abs(rect1.y - rect2.y)

    # Check if the distance is within 50 pixels
    if y_distance <= 30:
        return True
    else:
        return False

def check_collision_top(rect1, rect2):
    # Check if rect1's bottom collides with rect2's top
    if rect1.x > rect2.left and rect1.x < rect2.right and is_within_range(rect1, rect2):
        return rect1.bottom >= rect2.top

while running:
    dt = clock.tick(FPS) / 1000  # Delta Time = Airtime

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if player.bottom >= platformList[i].y:
                    if jump == False:
                        player_vel[1] = -JUMP_STRENGTH
                        jump = True
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
    for i in range(len(platformList)):
        #player_vel[1] = min(player_vel[1], platformList[i].y)
        player_pos[1] += player_vel[1] * dt

        test_player = pg.Rect(player_pos[0], player_pos[1] + player_vel[1] * dt, player_size, player_size)

        # if test_player.colliderect(platformList[i].rect):
        if check_collision_top(test_player, platformList[i].rect):
            jump = False
            player_pos[1] = platformList[i].y - player_size
            player_vel[1] = 0
            if i == 2:
                quit()

    # update player rect position
    player.topleft = player_pos

    screen.fill(BLACK)

    pg.draw.rect(screen, WHITE, player)
    startPlatform.draw(screen, GREEN)
    secondPlatform.draw(screen, GREEN)
    endPlatform.draw(screen, GREEN)

    if player.y > HEIGHT:
        quit()

    pg.display.flip()

    #
    # you're already tic/ing at the top of this loop, remove the last
    # clock.tick() call1to make the game less laggy
    # - random passerby
    #