
                            # i dont know if i need to import these or not
#import our classes
from Enemy_Class import *
from Player_Class import *
from Draw_Function import *

import pygame
import random
import math
from pygame import mixer




# Initialize the pygame
pygame.init()



player_info = ['plane.png', 3, 370, 480, 0, 0]

#   creates player 1
player1 =Player(1,player_info)

#   creates player 2
player2 = Player(2,player_info)


enemy_info = ['tie.png', 3, 370, 180, 0, 0]

#   creates enemy object tiefighter
tiefighter = Enemy(enemy_info)





            # hector
            #   for main game loop i want
            # 1  need to create the player
            # 2  i want the draw function to start drawing
            #

# Main Game Loop
running = True
while running:
    # event type loop (everything in here is checking the event type)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

           
            

       
#*******#**************************************#*******************************************************************
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
       
#**************************************************************************************************************************************************************************

        # key keystroke is pressed check to see if it is up or down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    
    # everything in here is in the outside thee for loop (outside of the event type but inside the while)

    # Check Player Boundary
    player1.CheckBoundary()






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
