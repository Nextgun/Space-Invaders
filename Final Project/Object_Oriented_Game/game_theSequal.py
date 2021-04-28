# this is going to be the game loop, 
# game logic should be stored in a logic class and called accordingly


import sys, game, pygame, random, time
import Entity_Class
from Draw_Class import *

pygame.init()

# checks for the keypresses
def event_manager(event): 
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            movement_list[0] = True
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            movement_list[1] = True
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            movement_list[2] = True
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            movement_list[3] = True
        if event.key == pygame.K_SPACE: # new laser firing method with bool, needs testing
            laser_state = True
            while True:
                time.sleep(1)
                laser_list.append(Entity_Class.Laser(player1.entityX, player1.entityY))

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            movement_list[0] = False
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            movement_list[1] = False
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            movement_list[2] = False
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            movement_list[3] = False 
        if event.key == pygame.K_SPACE:
            laser_state = False

# part game logic , part player movement; need to reorganize and sort
def update_Movement():
        #fixed movement bug, pretty ugly code tho..
        # lets try to pretty it up later, but for now it works (hector)
        if movement_list[0]:
            player1.entityX_change = -player_speed
        elif not movement_list[0]:
            player1.entityX_change = 0

        if movement_list[1]:
            player1.entityX_change = player_speed
        elif not movement_list[1] and not movement_list[0]:
            player1.entityX_change = 0

        if movement_list[0] and movement_list[1]:
            player1.entityX_change = 0

        if movement_list[2]:
            player1.entityY_change = -player_speed
        elif not movement_list[2]:
            player1.entityY_change = 0

        if movement_list[3]:
            player1.entityY_change = player_speed
        elif not movement_list[3] and not movement_list[2]:
            player1.entityY_change = 0

        if movement_list[2] and movement_list[3]:
            player1.entityY_change = 0

        player1.movement() # updates player movement
        for enemies in enemy_list: # updates enemy movement for each enemy
            enemies.enemy_movement()
        for lasers in laser_list: # updates movement for each laser
            lasers.laser_move()

# game logic
def collision_detection():
        for The_enemy in enemy_list: # collision: between enemies and lasers
            for The_laser in laser_list:
                if (The_enemy.detect_collision(The_laser)):
                    enemy_list.remove(The_enemy)
                    laser_list.remove(The_laser)
                    # Draw_Class.score = self.score + 1
        for The_enemy in enemy_list:
            if (The_enemy.detect_collision(player1)):
                game_over = True # need to create game over function

# i want enemy creation to be in a do while loop, do (create enemies), while (enemy list == 0)
def enemy_creation():
    for i in range(12):
        enemy_list.append(Entity_Class.Enemy(random.randint(0, 735), random.randint(50, 150)))

def dothedraw():
    Create_Screens.draw_all( player1,  enemy_list, laser_list)

# game over is game logic throw it in there
def game_over():
        print("you lose")

player1 = Entity_Class.Player(370,480)
enemy_list = []
laser_list = []
movement_list = [False, False, False, False] # [left, right, up, down] if true move in direction :)
player_speed = 0.8
enemy_creation()

#level_1 = game.Game()

game_over = False

def GameLoop():
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

           

            collision_detection()
            event_manager(event)
            update_Movement()
            dothedraw()
      #  if collision check ():
       #     game_over = True


            pygame.display.flip()
    pygame.quit()



#creates obj of class to run game
if __name__ == "__main__":
    GameLoop()

   # the_game  = idk
