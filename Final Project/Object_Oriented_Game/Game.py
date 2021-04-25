import Entity_Class
import pygame
from threading import Timer
import random
import math
from pygame import mixer
from Draw_Class import Create_Screens

# todo list
# fix movement bug (jack)
# collision, done (hector)
#
# need to create different "screens" to draw, and change screens depending on game state
# i.e. game over = screen3, game = screen2, title screen = screen1


# do while # do the gaem loop # while the character is alive
# enemies killed # sum number of enemies
# average the scores

#  game class should hold all the game logic,
#   ie spawing enemies etc, movement checks, no drawing
class Game:
    def __init__(self):
        pygame.init()

        #screen and background and font
        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load('assets/spacebg.png')
        self.font = pygame.font.Font('assets/FreeSansBold.ttf', 28)

        # Background Sound
        mixer.music.load('assets/background.wav')
        mixer.music.set_volume(0.04)
        mixer.music.play(-1)

        # Changes the Title and Icon
        pygame.display.set_caption("Group's Space Invaders")
        icon = pygame.image.load('assets/alien.png')
        pygame.display.set_icon(icon)


        #object creation
        self.player_list = [] # i want to throw players in a list as well, to have players 1, 2, 3, 4
        self.player1 = Entity_Class.Player(370, 480)
        self.enemy_list = []
        self.enemy_creation()
        self.laser_list = []

        self.movement_list = [False, False, False, False] # [left, right, up, down] if true move in direction :)
        self.player_speed = 0.7

        self.run = True # bool for main loop to start
        laser_state = True
        
        self.mainLoop() # runs the main loop function

    
    def read_file(self):
        # read a file into the game
        list = []
        pass
   
    def write_file(self):
        # write the new score into file
        pass
        
        
    # trying to get a delay to work for laser
    def thelaserstate(self):
        laser_state = True
    
    # checks for the keypresses
    def event_manager(self):

        # trying to get a delay to work for laser
        laser_state = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.movement_list[0] = True
                if event.key == pygame.K_RIGHT:
                    self.movement_list[1] = True
                if event.key == pygame.K_UP:
                    self.movement_list[2] = True
                if event.key == pygame.K_DOWN:
                    self.movement_list[3] = True
                if event.key == pygame.K_SPACE:

                    self.laser_list.append(Entity_Class.Laser(self.player1.entityX, self.player1.entityY))

                    # i want to cry
                    #if laser_state == True:
                        #(self.laser_list.append(Entity_Class.Laser(self.player1.entityX, self.player1.entityY)))
                        #laser_state = False
                        #L = Timer(2.0,thelaserstate)              
                        #L.start() # want to add delay between laser to prevent spam, but delays whole game
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.movement_list[0] = False
                if event.key == pygame.K_RIGHT:
                    self.movement_list[1] = False
                if event.key == pygame.K_UP:
                    self.movement_list[2] = False
                if event.key == pygame.K_DOWN:
                    self.movement_list[3] = False
        if self.enemy_list == 0:
            self.enemy_creation()

    def update_Movement(self):
        #fixed movement bug, pretty ugly code tho..
        if self.movement_list[0]:
            self.player1.entityX_change = -self.player_speed
        elif not self.movement_list[0]:
            self.player1.entityX_change = 0

        if self.movement_list[1]:
            self.player1.entityX_change = self.player_speed
        elif not self.movement_list[1] and not self.movement_list[0]:
            self.player1.entityX_change = 0

        if self.movement_list[0] and self.movement_list[1]:
            self.player1.entityX_change = 0

        if self.movement_list[2]:
            self.player1.entityY_change = -self.player_speed
        elif not self.movement_list[2]:
            self.player1.entityY_change = 0

        if self.movement_list[3]:
            self.player1.entityY_change = self.player_speed
        elif not self.movement_list[3] and not self.movement_list[2]:
            self.player1.entityY_change = 0

        if self.movement_list[2] and self.movement_list[3]:
            self.player1.entityY_change = 0

        self.player1.movement() # updates player movement
        for enemies in self.enemy_list: # updates enemy movement for each enemy
            enemies.enemy_movement()
        for lasers in self.laser_list:
            lasers.laser_move()

    def collision_detection(self):
        for The_enemy in self.enemy_list: # collision: between enemies and lasers
            for The_laser in self.laser_list:
                if (The_enemy.detect_collision(The_laser)):
                    self.enemy_list.remove(The_enemy)
                    self.laser_list.remove(The_laser)
        for The_enemy in self.enemy_list:
            if (The_enemy.detect_collision(self.player1)):
                self.game_over() # need to create game over function
                
    def game_over(self):
        print("you lose")
        

    def mainLoop(self):
        while self.run:
            self.collision_detection()
            Create_Screens.draw_all(self, self.background, self.player1, self.screen, self.enemy_list, self.laser_list)
            self.event_manager()
            self.update_Movement()
            pygame.display.flip()
        pygame.quit()


    def enemy_creation(self):
        for i in range(12):
            self.enemy_list.append(Entity_Class.Enemy(random.randint(0, 735), random.randint(50, 150)))
            
            

#creates obj of class to run game
if __name__ == "__main__":
    game1 = Game()

   # the_game  = idk

