import pygame
import random
import math
from pygame import mixer


# Initialize the pygame
pygame.init()



#player1 = player()  
#player2 = player()

tiefighter = enemy()






# Main Game Loop
running = True
while running:
    screen.fill((0, 0, 0))  # Changes the screen color or background
    screen.blit(background, (0, 0))  # Background image

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


       
#****************************************************************************************************************************************************************************


        #**************************************#
        #                                      #
        #   checks keyboard input              #
        #   need to check the logic            #
        #                                      #
        #**************************************#



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


       
#****************************************************************************************************************************************************************************




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
        player_collide = collide(tieX[i], tieY[i], playerX, playerY) #checks to see if player collides with enemy
        if tieY[i] > 440 or player_collide:
            for j in range(num_of_tie):
                tieY[j] = 2000
            game_over_text()
            break

        tieX[i] += tieX_change[i] #Emeny movement and once it hits side walls enemy moves down
        if tieX[i] <= 0:
            tieX_change[i] = 0.3
            tieY[i] += tieY_change[i]
        elif tieX[i] >= 736:
            tieX_change[i] = -0.3
            tieY[i] += tieY_change[i]

        # Collision with enemy and laser
        collision = isCollision(tieX[i], tieY[i], laserX, laserY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play() #plays the explosion sound if laser hits enemy 
            laserY = 480
            laser_state = "ready" # If laser hits enemy, laser resets to ready state
            score_value += 1
            tieX[i] = random.randint(0, 735)
            tieY[i] = random.randint(50, 150)

        tie(tieX[i], tieY[i], i)
    # Laser movement
    if laserY <= 0:
        laserY = 480
        laser_state = "ready"

    if laser_state is "fire": # If laser = fire then it moves up the screen until it hits enemy or top of screen then will go back to ready state
        fire_laser(laserX, laserY)
        laserY -= laserY_change

    player(playerX, playerY)  # needs to be here so that it is drawn on top of the screen
    show_score(textX, textY)
    pygame.display.update()
