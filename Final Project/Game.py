import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('spacebg.png')

# Background Sound
mixer.music.load('background.wav')
mixer.music.set_volume(0.5)
mixer.music.play(-1)


# Changes the Title and Icon
pygame.display.set_caption("Group's Space Invaders")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('plane.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
tieImg = []
tieX = []
tieY = []
tieX_change = []
tieY_change = []
num_of_tie = 6

for i in range(num_of_tie):
    tieImg.append(pygame.image.load('tie.png'))
    tieX.append(random.randint(0, 735))  # had enemy tie randomly spawn in different places on the x axis
    tieY.append(random.randint(50,
                               150))  # had enemy tie randomly spawn in different places on the y axis between set parameters
    tieX_change.append(0.3)
    tieY_change.append(20)

# Laser

# Ready - you cant see the laser on the screen
# Fire - the laser is currently moving
laserImg = pygame.image.load('laser.png')
laserX = 0
laserY = 480
laserX_change = 0
laserY_change = .5
laser_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 28)

textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 84)


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER!", True, (10, 240, 13))
    screen.blit(over_text, (170, 300))


def player(x, y):
    screen.blit(playerImg, (x, y))  # draws the play at set coord


def tie(x, y, i):
    screen.blit(tieImg[i], (x, y))  # draws the play at set coord


def fire_laser(x, y):
    global laser_state
    laser_state = "fire"
    screen.blit(laserImg, (x + 16, y + 10))


def isCollision(tieX, tieY, laserX, laserY):
    distance = math.sqrt(math.pow(tieX - laserX, 2) + (math.pow(tieY - laserY, 2)))  # Distance Formula
    if distance < 30:
        return True
    else:
        return False


def collide(tieX, tieY, playerX, playerY):
    player_distance = math.sqrt(math.pow(tieX - playerX, 2) + (math.pow(tieY - playerY, 2)))
    if player_distance < 30:
        return True
    else:
        return False


# Main Game Loop
running = True
while running:

    # Changes the screen color or background
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # key keystroke is pressed check to see if it is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if laser_state is "ready":
                    laser_Sound = mixer.Sound('laser.wav')
                    laser_Sound.play()
                    # Gets the current x and y coord of your ship
                    laserX = playerX
                    laserY = playerY
                    fire_laser(laserX, laserY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        # key keystroke is pressed check to see if it is up or down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    # Checking player boundaries
    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    # Checking enemy boundaries
    for i in range(num_of_tie):

        # Game Over
        player_collide = collide(tieX[i], tieY[i], playerX, playerY)
        if tieY[i] > 440 or player_collide:
            for j in range(num_of_tie):
                tieY[j] = 2000
            game_over_text()
            break

        tieX[i] += tieX_change[i]
        if tieX[i] <= 0:
            tieX_change[i] = 0.3
            tieY[i] += tieY_change[i]
        elif tieX[i] >= 736:
            tieX_change[i] = -0.3
            tieY[i] += tieY_change[i]

        # Collision
        collision = isCollision(tieX[i], tieY[i], laserX, laserY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            laserY = 480
            laser_state = "ready"
            score_value += 1
            tieX[i] = random.randint(0, 735)
            tieY[i] = random.randint(50, 150)

        tie(tieX[i], tieY[i], i)
    # Laser movement
    if laserY <= 0:
        laserY = 480
        laser_state = "ready"

    if laser_state is "fire":
        fire_laser(laserX, laserY)
        laserY -= laserY_change

    player(playerX, playerY)  # needs to be here so that it is drawn on top of the screen
    show_score(textX, textY)
    pygame.display.update()
